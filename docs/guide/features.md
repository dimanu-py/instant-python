# Features

When using the subcommand `new` with either the `project` or `folder` command, you will be able to configure
different aspects of your project through a set of questions that will guide you through the process.

!!! note
    Depending on the main command you use, you will be able to configure differnt kind of things. Here
    is an overview of all the options that can be configured.


## Project slug

Configure the name of the main folder of your project. This name will be used in the _pyproject.toml_ file too.

When writing the project slug, you must convey _pyproject.toml_ conventions, so you should not write spaces
between words.

## Source name

Configure the name of the source code of your project.

The most typical option for this folder is _src_, but you can change it to whatever you want: _source_, _code_, _app_, etc.


## Description

Include a description about your project that will be included in the _pyproject.toml_ file.

## Version

If you want to version your releases you would want to set this value correctly. By default, it will be set to `0.1.0`,
but you can change it to any value or format you want.

## Author

Set the author of the project. You can write your personal name or your GitHub username.

This value will be included in the _pyproject.toml_ and _LICENSE_ files.

## License

Choose between _MIT_, _Apache_ or _GPL_ licenses to set your project. By default, 
it will place you on _MIT_ option to be the most popular license.

If you want to use a different license, unfortunately, you will have to change it manually in the _LICENSE_ file.

## Python version

Select the Python version you want to use for your project between versions 3.13 to 3.10. 
By default, it will place you on the latest version available.

## Dependency manager

Choose between two of the most popular dependencies and project manager for Python: 
 - [_uv_](https://docs.astral.sh/uv)
 - [_pdm_](https://pdm-project.org/en/latest/)

## Git

You will be able to configure your project as a git repository automatically.

You would be able to specify your GitHub username and your email to configure git for this folder, this way
you can use your own profile to push your code.

If you choose to create a git repository, it will create an empty _README.md_ file and the _.gitignore_ file 
configured for Python projects.

## Default templates

There are some project templates already configured that you can use to create your project. These templates
will create the folder structure of your project following a specific pattern.

### Domain Driven Design
 
Follows DDD pattern and screaming architecture. 

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

## Out of the box implementations

When creating a new project, you will be able to include some boilerplate and implementations code
that will help you to start your project

### Value objects and exceptions

Value objects are a common pattern in DDD to encapsulate primitives and encapsulate domain logic. If 
you choose this option, it will include the following value objects:

- Base ValueObject
- UUID
- StringValueObject
- IntValueObject

Along with these value objects, it will include a base exception class that you can use to create your own exceptions and
some common exceptions that you can use in your project:

- Base DomainError
- IncorrectValueTypeError
- InvalidIdFormatError
- InvalidNegativeValueError
- RequiredValueError

### GitHub actions and workflows

A common feature in projects is to have a CI/CD pipeline that will run some tasks. This option will include the following:

- A GitHub action that will set up your Python environment in your pipeline using the dependency manager you selected.
- A workflow that will execute all the test, lint, type check and code formatting tasks.

### Makefile

A Makefile is a common tool to run tasks in your project. This feature is specially useful when automating tasks and
avoid remembering all the commands. The default Makefile will include the following commands:

| Command                | Description                              |
|------------------------|------------------------------------------|
| `make help`            | Show available commands                  |
| `make test`            | Run all tests                            |
| `make unit`            | Run unit tests for changed files         |
| `make all-unit`        | Run all unit tests                       |
| `make integration`     | Run integration tests for changed files  |
| `make all-integration` | Run all integration tests                |
| `make all-acceptance`  | Run all acceptance tests                 |
| `make coverage`        | Run coverage tests                       |
| `make install`         | Install all dependencies                 |
| `make update`          | Update all dependencies                  |
| `make add-dep`         | Add a new dependency                     |
| `make remove-dep`      | Remove a dependency                      |
| `make check-typing`    | Runs type checker                        |
| `make check-lint`      | Checks lint code with Ruff               |
| `make lint`            | Fixes lint errors code with Ruff         |
| `make check-format`    | Checks format code with Ruff             |
| `make format`          | Format code with Ruff                    |
| `make local-setup`     | Set up the local development environment |
| `make show`            | Show all installed dependencies          |
| `make search`          | Show details of a specific package       |

### Logger

Logging messages in an application it's a common task. 

This boilerplate will include a basic logger that creates a handler for
production with logging ERROR level and a handler for development with logging DEBUG 
level. These handlers will be logging messages into a file that will be rotated every day.

It will also include a json formatter that formats the message with the time the logg was made,
the level, the name or title of the message and the message itself.

### FastAPI

FastAPI has become one of the most popular frameworks to create APIs in Python. This boilerplate will include:

- A main file where the FastAPI is created and two error handlers are set up, one that captures unexpected errors that will
raise a 500 status code, and another handler that catches `DomainError` instances and raises a 400 status code by default.
- A lifespan that will execute the migrations with alembic when the application starts.
- A decoupled implementation to model your status codes and http responses.

!!! info
    When selecting this feature, you will need to have the logger boilerplate included.


### Asynchronous SQL Alchemy

SQL Alchemy is a popular ORM for Python, and with the introduction of async and await in Python, it has become
a powerful tool to manage databases. This boilerplate will include:

- A basic implementation of a repository pattern that will allow you to create a repository for each entity in your project.
- A class to encapsulate postgres settings

### Asynchronous migrations

Along with SQL Alchemy it's typical to use Alembic to manage database migrations. This boilerplate will include everything
needed to configure the migrations and run them asynchronously.

### Event bus

In complex applications it's common to use an event bus to communicate between different parts of the application. This boilerplate
will set up a decoupled implementation of an event bus using RabbitMQ. This implementation will include:

- An `AggregateRoot` class that will allow you to create your aggregates and publish events automatically.
- Modelled domain events that will be published through the event bus.
- Interface for the event bus and subscriber.
- Concrete implementation of the event bus using RabbitMQ

## Dependencies

You will be able to install dependencies automatically in your project.

When selecting to install any dependency you will:

- Write the name of the dependency you want to install.
- Check that is written correctly.
- Choose if you want to install it as a dev dependency.
- Choose if you want to organize it in a group.

All dependencies will automatically add them to the _pyproject.toml_ file and a virtual environment will be created.
