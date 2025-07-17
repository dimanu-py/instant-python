# Init

Use the `init` command to turn a configuration file into a ready to use project.

```bash
ipy init
```

By default `instant-python` will look for **ipy.yml** in the current directory. A different file can be provided with `--config` or `-c` flags. 

Additionally, a [custom template](#using-custom-template) for your project structure can be used, you tell `ipy` to use that
template with the `--template` or `-t` flag and providing the path to the template file.

```bash
ipy init -t /path/to/template.yml
```

!!! important
    When using a [custom template](#using-custom-template), the possibility of using [out-of-the-box implementations](#out-of-the-box-implementations)
    is not available. The custom template will only create the folder structure and files defined in it.

## Overview 

The command performs the following steps:

1. Creates the project folder structure based on the selected template or your custom template.
2. **Only when the template is not custom**, writes boilerplate code for any [built‑in features](#out-of-the-box-implementations) enabled in the configuration.
3. Sets up the chosen dependency manager and installs dependencies under the selected Python version.
4. Initializes a git repository if requested and configures your username and email.
5. Moves the configuration file inside the new project folder for future reference.

## Configuring a dependency manager

Choose between two of the most popular dependencies and project manager for Python:

- [_uv_](https://docs.astral.sh/uv)
- [_pdm_](https://pdm-project.org/en/latest/)

Instant Python will automatically download the selected dependency manager and create a virtual environment. This will
allow you to install your dependencies and run tasks out of the box.

## Creating a git repository

You will be able to configure your project as a git repository automatically. Instant Python will use the `username` and
`email` fields from the configuration file to set up your git identity.

If you choose to create a git repository, it will create a _README.md_ file and the _.gitignore_ file
configured for Python projects.

## Default templates

There are some project templates already configured that you can use to create your project. These templates
will create the folder structure of your project following a specific pattern.

!!! important
    These templates do not reflect your architecture, but the folder structure of your project. There is a key difference between these concepts.

### Domain Driven Design

Follows DDD pattern and screaming architecture organization.

Separates the source code and test folder in bounded contexts and aggregates.
Each aggregate will contain the known _domain_, _application_ and _infra_ layers. This template will allow you to create your first bounded context and aggregate.

```
├── src
│  ├── bounded_context_name
│  │  └── aggregate_name
│  │  │  ├── application
│  │  │  ├── domain
│  │  │  └── infra
│  │  └── shared
│  ├── shared
│  └── delivery
│     └── api
└── tests
   ├── bounded_context_name
   │  └── aggregate_name
   │  │  ├── application
   │  │  ├── domain
   │  │  └── infra
   │  └── shared
   ├── shared
   └── delivery
      └── api
```

### Clean Architecture

Will create your folders following the clean architecture pattern.

Separates the source code and test folder in _domain_, _application_, _infrastructure_ and _delivery_ layers.

```
├── src
│  ├── application
│  ├── domain
│  ├── infra
│  └── delivery
│     └── api
└── tests
   ├── acceptance
   ├── unit
   └── integration
```

### Standard project

Will create your project with the common pattern of source code and test folder.

```
├── src
└── tests
```

## Out-of-the-box implementations

When creating a new project, you will be able to include some boilerplate and implementation code
that will help you to start your project.

!!! tip
    These implementations are completely subjective and personal. This does not mean that you must implement
    them in the same way or that they are the best way to implement them. You can use them as a starting point
    and iterate them as you need.

!!! warning
    These implementations are only available when using one of the [default templates](#default-templates).

### Value objects and exceptions

Value objects are a common pattern to encapsulate primitives and encapsulate domain logic. If
you choose this option, it will include the following value objects:

A base class for all aggregates of your project with some common methods and utilities.

???+ example "Aggregate"

    ```python
    class Aggregate(ABC):
        @abstractmethod
        def __init__(self) -> None:
            raise NotImplementedError
    
        @override
        def __repr__(self) -> str:
            attributes = []
            for key, value in sorted(self._to_dict().items()):
                attributes.append(f"{key}={value!r}")
    
            return f"{self.__class__.__name__}({', '.join(attributes)})"
    
        @override
        def __eq__(self, other: Self) -> bool:
            if not isinstance(other, self.__class__):
                return NotImplemented
    
            return self._to_dict() == other._to_dict()
    
        def _to_dict(self, *, ignore_private: bool = True) -> dict[str, Any]:
            dictionary: dict[str, Any] = {}
            for key, value in self.__dict__.items():
                if ignore_private and key.startswith(f"_{self.__class__.__name__}__"):
                    continue  # ignore private attributes
    
                key = key.replace(f"_{self.__class__.__name__}__", "")
    
                if key.startswith("_"):
                    key = key[1:]
    
                dictionary[key] = value
    
            return dictionary
    
        @classmethod
        def from_primitives(cls, primitives: dict[str, Any]) -> Self:
            if not isinstance(primitives, dict) or not all(
                    isinstance(key, str) for key in primitives
            ):
                raise TypeError(f'{cls.__name__} primitives <<<{primitives}>>> must be a dictionary of strings. Got <<<{type(primitives).__name__}>>> type.')  # noqa: E501  # fmt: skip
    
            constructor_signature = signature(obj=cls.__init__)
            parameters: dict[str, Parameter] = {parameter.name: parameter for parameter in constructor_signature.parameters.values() if parameter.name != 'self'}  # noqa: E501  # fmt: skip
            missing = {name for name, parameter in parameters.items() if parameter.default is _empty and name not in primitives}  # noqa: E501  # fmt: skip
            extra = set(primitives) - parameters.keys()
    
            if missing or extra:
                cls._raise_value_constructor_parameters_mismatch(
                    primitives=set(primitives), missing=missing, extra=extra
                )
    
            return cls(**primitives)
    
        @classmethod
        def _raise_value_constructor_parameters_mismatch(
                cls,
                primitives: set[str],
                missing: set[str],
                extra: set[str],
        ) -> None:
            primitives_names = ", ".join(sorted(primitives))
            missing_names = ", ".join(sorted(missing))
            extra_names = ", ".join(sorted(extra))
    
            raise ValueError(f'{cls.__name__} primitives <<<{primitives_names}>>> must contain all constructor parameters. Missing parameters: <<<{missing_names}>> and extra parameters: <<<{extra_names}>>>.')  # noqa: E501  # fmt: skip
    
        def to_primitives(self) -> dict[str, Any]:
            primitives = self._to_dict()
            for key, value in primitives.items():
                if isinstance(value, Aggregate) or hasattr(value, "to_primitives"):
                    value = value.to_primitives()
    
                elif isinstance(value, Enum):
                    value = value.value
    
                elif isinstance(value, ValueObject) or hasattr(value, "value"):
                    value = value.value
    
                    if isinstance(value, Enum):
                        value = value.value
    
                primitives[key] = value
    
            return primitives
    ```

A base value object class that will automatically be able to gather all methods decorated with `@validate` to be able
to validate any pre-condition of the value object. This class is also configured to be immutable, meaning that once
initialized, the value cannot be changed.

???+ example "Base ValueObject"

    ```python
    class ValueObject[T](ABC):
        __slots__ = ("_value",)
        __match_args__ = ("_value",)
    
        _value: T
    
        def __init__(self, value: T) -> None:
            self._validate(value)
            object.__setattr__(self, "_value", value)
    
        def _validate(self, value: T) -> None:
            """Gets all methods decorated with @validate and calls them to validate all domain conditions."""
            validators: list[Callable[[T], None]] = []
            for cls in reversed(self.__class__.__mro__):
                if cls is object:
                    continue
                for name, member in cls.__dict__.items():
                    if getattr(member, "_is_validator", False):
                        validators.append(getattr(self, name))
    
            for validator in validators:
                validator(value)
    
        @property
        def value(self) -> T:
            return self._value
    
        @override
        def __eq__(self, other: Self) -> bool:
            return self.value == other.value
    
        @override
        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self._value!r})"
    
        @override
        def __str__(self) -> str:
            return str(self._value)
    
        @override
        def __setattr__(self, name: str, value: T) -> None:
            """Prevents modification of the value after initialization."""
            if name in self.__slots__:
                raise AttributeError("Cannot modify the value of a ValueObject")
    
            public_name = name.replace("_", "")
            public_slots = [slot.replace("_", "") for slot in self.__slots__]
            if public_name in public_slots:
                raise AttributeError("Cannot modify the value of a ValueObject")
    
            raise AttributeError(
                f"Class {self.__class__.__name__} object has no attribute '{name}'"
            )
    ```

Some common value objects that will be placed at _usables_ folder.

???+ example "UUID"

    ```python
    class Uuid(ValueObject[str]):
        @validate
        def _ensure_has_value(self, value: str) -> None:
            if value is None:
                raise RequiredValueError
    
        @validate
        def _ensure_value_is_string(self, value: str) -> None:
            if not isinstance(value, str):
                raise IncorrectValueTypeError(value)
    
        @validate
        def _ensure_value_has_valid_uuid_format(self, value: str) -> None:
            try:
                UUID(value)
            except ValueError:
                raise InvalidIdFormatError
    ```

???+ example "StringValueObject"

    ```python
    class StringValueObject(ValueObject[str]):
        @validate
        def _ensure_has_value(self, value: str) -> None:
            if value is None:
                raise RequiredValueError
    
        @validate
        def _ensure_is_string(self, value: str) -> None:
            if not isinstance(value, str):
                raise IncorrectValueTypeError(value)
    ```
???+ example "IntValueObject"

    ```python
    class IntValueObject(ValueObject[int]):
        @validate
        def _ensure_has_value(self, value: int) -> None:
            if value is None:
                raise RequiredValueError
    
        @validate
        def _ensure_value_is_integer(self, value: int) -> None:
            if not isinstance(value, int):
                raise IncorrectValueTypeError(value)
    
        @validate
        def _ensure_value_is_positive(self, value: int) -> None:
            if value < 0:
                raise InvalidNegativeValueError(value)
    ```

Along with these value objects, it will include a base exception class that you can use to create your own exceptions and
some common exceptions that you can use in your project:

???+ example "Base Error"

    ```python
    class Error(Exception, ABC):
        def __init__(self, message: str, error_type: str) -> None:
            self._message = message
            self._type = error_type
            super().__init__(self._message)
    
        @property
        def type(self) -> str:
            return self._type
    
        @property
        def message(self) -> str:
            return self._message
    
        def to_primitives(self) -> dict[str, str]:
            return {
                "type": self.type,
                "message": self.message,
            }
    ```

???+ example "Domain Error"

    ```python
    class DomainError(Error):
        ...
    ```

???+ example "IncorrectValueTypeError"

    ```python
    T = TypeVar("T")
    
    
    class IncorrectValueTypeError(DomainError):
        def __init__(self, value: T) -> None:
            self._message = f"Value '{value}' is not of type {type(value).__name__}"
            self._type = "incorrect_value_type"
            super().__init__(message=self._message, error_type=self._type)
    ```

???+ example "InvalidIdFormatError"

    ```python
    class InvalidIdFormatError(DomainError):
        def __init__(self) -> None:
            self._message = "User id must be a valid UUID"
            self._type = "invalid_id_format"
            super().__init__(message=self._message, error_type=self._type)
    ```

???+ example "InvalidNegativeValueError"

    ```python
    class InvalidNegativeValueError(DomainError):
        def __init__(self, value: int) -> None:
            self._message = f"Invalid negative value: {value}"
            self._type = "invalid_negative_value"
            super().__init__(message=self._message, error_type=self._type)
    ```

???+ example "RequiredValueError"

    ```python
    class RequiredValueError(DomainError):
        def __init__(self) -> None:
            self._message = "Value is required, can't be None"
            self._type = "required_value"
            super().__init__(message=self._message, error_type=self._type)
    ```

### Makefile

A Makefile is a common tool to run tasks in your project. This feature is specially useful when automating tasks and
avoid remembering all the commands.

!!! warning
    If you are running `instant-python` in a Windows environment, the Makefile will not work out of the box. You would need
    to install a tool like [GNU Make for Windows](https://gnuwin32.sourceforge.net/packages/make.htm) or use a different task runner.
The default Makefile will include the following commands:

| Command             | Description                                 |
|---------------------|---------------------------------------------|
| `make help`         | Show available commands                     |
| `make local-setup`  | Set up the local development environment    |
| `make install`      | Install all dependencies                    |
| `make update`       | Update all dependencies                     |
| `make add-dep`      | Add a new dependency                        |
| `make remove-dep`   | Remove a dependency                         |
| `make test`         | Run all tests                               |
| `make unit`         | Run all unit tests                          |
| `make integration`  | Run all integration tests                   |
| `make acceptance`   | Run all acceptance tests                    |
| `make coverage`     | Run coverage tests                          |
| `make watch`        | Run tests in watch mode                     |
| `make check-typing` | Runs type checker                           |
| `make check-lint`   | Checks lint code with Ruff                  |
| `make lint`         | Fixes lint errors code with Ruff            |
| `make check-format` | Checks format code with Ruff                |
| `make format`       | Format code with Ruff                       |
| `make secrets`      | Analyzes source code for leakage of secrets |
| `make audit`        | Identifies vulnerabilities in dependencies  |
| `make clean`        | Cleans up the project metadata files        |
| `make show`         | Show all installed dependencies             |
| `make search`       | Show details of a specific package          |

!!! info
    The commands `unit`, `integration` and `acceptance` are defined based on the assumption that you will mark your tests with 
    the `@pytest.mark.unit`, `@pytest.mark.integration` and `@pytest.mark.acceptance` decorators.
    If this is not your case, you change the commands as needed in the Makefile to match your test structure.

Some of these commands will be added only based on the features and/or dependencies you set in the configuration file:

| Command             | Condition                                                                                         |
|---------------------|---------------------------------------------------------------------------------------------------|
| `make test`         | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make unit`         | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make integration`  | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make acceptance`   | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make coverage`     | If `pytest` is install or if either `makefile` or `github_actions` built in features are selected |
| `make watch`        | If `pytest-watch` is install                                                                      |
| `make check-lint`   | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make lint`         | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make check-format` | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make format`       | If `ruff` is install or if either `makefile` or `github_actions` built in features are selected   |
| `make secrets`      | If `precommit_hook` built in feature is selected                                                  |
| `make audit`        | If `github_actions` built in feature is selected                                                  |


### GitHub actions and workflows

!!! info
    When selecting this feature, by default, the library will include `mypy` as a type checker, `ruff` as a linter and formatter, and
    `pytest` as a test runner. If you want to use different tools, you can change them later in the workflow file.

A common feature in projects is to have a CI/CD pipeline that will run some tasks. This option will include the following:

- A GitHub action that will set up your Python environment in your pipeline using the dependency manager you selected.
- A workflow that will check linting, formatting, and statyc analysis of your code. Make an analysis of your code quality, audit
your dependencies, analyze for any leakage of secrets and run all tests generating a coverage report.
- A workflow that will create a new version tag for your project, update a CHANGELOG.md file and generates a new release in GitHub using
`semantic-release`. You can get a deeper understanding of this workflow in the [releases section](../home/releases.md).

!!! info
    Some of the steps in this workflow uses some of the make commands presented in the [previous section](#makefile).

### GitHub Issues Templates

This feature will include two GitHub issues templates that you can use to create issues in your project:

- A bug report template that will help you to report bugs in your project.
- A feature request template that will help you to request new features in your project.

### Logger

Logging messages in an application it's a common task.

This boilerplate will include a basic logger that creates a handler for
production with logging ERROR level and a handler for development with logging DEBUG
level. These handlers will be logging messages into a file that will be rotated every day.

It will also include a json formatter that formats the message with the time the logg was made,
the level, the name or title of the message and the message itself.

### FastAPI

[FastAPI](https://fastapi.tiangolo.com/) has become one of the most popular frameworks to create APIs in Python. This boilerplate will include:

- A main file where the FastAPI is created
- Two error handlers configured, one that captures unexpected errors that will raise a 500 status code, and another 
handler that catches `DomainError` instances and raises a 400 status code by default.
- When logger built-in feature is selected, it will include a middleware that will log all requests and a handler to
be able to log Pydantic validation errors.
- A lifespan that will execute the migrations with alembic when the application starts.
- A decoupled implementation to model your success and error responses.

### Asynchronous SQL Alchemy

SQL Alchemy is a popular ORM for Python, and with the introduction of async and await in Python, it has become
a powerful tool to manage databases. This boilerplate will include:

- A basic implementation of a repository pattern that will allow you to create a repository for each entity in your project.
- A class to encapsulate postgres settings

### Asynchronous migrations

Along with SQL Alchemy it's typical to use Alembic to manage database migrations. This boilerplate will include everything
needed to configure the migrations and run them asynchronously.

### Event bus

In complex applications, it's common to use an event bus to communicate between different parts of the application. This boilerplate
will set up a decoupled implementation of an event bus using RabbitMQ. This implementation will include:

- An `EventAggregate` class that will allow you to create your aggregates and publish events automatically.

    ???+ example "EventAggregate"
    
        ```python
        class EventAggregate(Aggregate):
            _domain_events: list[DomainEvent]
        
            def __init__(self) -> None:
                self._domain_events = []
        
            def record(self, event: DomainEvent) -> None:
                self._domain_events.append(event)
        
            def pull_domain_events(self) -> list[DomainEvent]:
                recorded_domain_events = self._domain_events
                self._domain_events = []
        
                return recorded_domain_events
        ```

- Modeled domain events that will be published through the event bus.
- Interface for the event bus and subscriber.
- Concrete implementation of the event bus using RabbitMQ

### Precommit hooks

Precommit hooks are a great way to ensure that your code is always in a good state before committing it to the repository.

This boilerplate will include a precommit hook that will run the following tasks before committing your code:

- Check for any large files that should not be committed to the repository.
- Check for files that have the same name but only differ in case, which can cause issues in some file systems.
- Check the format of toml and yaml files
- Check for any merge conflicts that have not been resolved.
- Check for any secrets that have been leaked in the code.
- Check for the format of commit messages, ensuring they follow the conventional commit format.

Additionally, it will include two pre-push hooks:

- One that will check for any linting error
- One to check for any formatting error

### Security file

This feature will include a _SECURITY.md_ file that will help the users of your project
to report security issues in your project. It will include:

- Steps explaining how to report security issues.
- How we will handle security issues and disclosure.

### Citation file

When working on open source projects, it's common to include a _CITATION.cff_ file that will 
allow users to cite your project when using it in their research or projects.

This feature will include a _CITATION.cff_ file that will help users to cite your project.

## Using custom template

You can create a new project using a custom template instead of one of the [default templates](#default-templates).

!!! important
    When using a custom template, the possibility of using [out-of-the-box implementations](#out-of-the-box-implementations)
    is not available.

This custom template must follow a specific structure and syntax to be able to generate the project correctly.

- You must use a yml file to define the folder structure.
- The hierarchy of your project will be declared as a list of elements with the following structure:
    - `name`: The name of the folder or file to create.
    - `type`: The type of the element, which can be `directory` or `file`.
    - `python`: **Only for directories**. Set its value to True if the directory is a python module to include the `__init__.py` file, otherwise
      ignore this field.
    - `extension`: **Only for files**. The extension of the file to create. If the file do not have an extension, you can ignore
      this field.
    - `children`: A list of elements that will be created inside the folder. This can be either another directory or files.
