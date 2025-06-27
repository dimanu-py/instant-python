## 0.6.1 (2025-06-27)

### 🐛 Bug Fixes

- correct links to README.md

## 0.6.0 (2025-06-27)

### ✨ Features

- **configuration**: remove white spaces from slug
- **configuration**: raise error for bounded context if specify_bounded_context is true and no DDD template is set or if either bounded context or aggregate name are set
- **commands**: set ipy.yml as the default configuration file
- **shared**: add SupportedBuiltInFeatures enum for built-in feature management
- **configuration**: add method to retrieve supported templates
- **configuration**: add CUSTOM template type to SupportedTemplates
- **shared**: add SupportedLicenses enum with method to retrieve supported licenses
- **shared**: add SupportedPythonVersions enum with method to retrieve supported versions
- **shared**: add method to retrieve list of supported managers
- **cli**: add config command to CLI for configuration management
- **commands**: add command to generate configuration file for new projects
- **configuration**: add save_on_current_directory method to save configuration in the current directory
- **configuration**: implement QuestionWizard class to manage question steps and parse answers
- **configuration**: add parse_from_answers method to differentiate when parsing comes from user answers
- **configuration**: add Step interface for all concrete implementations and Steps container to manage configuration steps
- **configuration**: implement DependenciesStep to manage user input for dependency installation
- **configuration**: add TemplateStep to manage template selection and built-in features
- **configuration**: implement GitStep to handle git initialization questions
- **configuration**: implement GeneralQuestionStep to store all questions that will allow the user to build the general section of the config file
- **configuration**: implement ConditionalQuestion
- **configuration**: implement MultipleChoiceQuestion
- **configuration**: implement FreeTextQuestion
- **configuration**: implement ChoiceQuestion for questions where user has to select one option between some
- **configuration**: implement boolean question
- **configuration**: create base Question class defining common logic for all concrete type of questions
- **configuration**: add wrapper of questionary library to be able to test easily question classes
- **cli**: include new "init" command in general application
- **commands**: allow the option of passing a custom template to generate a project with a custom structure
- **project-creator**: allow FileSystem to handle normal files apart from boilerplate files
- **renderer**: implement CustomProjectRenderer
- **commands**: move configuration file to project
- **configuration**: add method to move configuration file to generated project
- **configuration**: add config file path attribute and named constructor to create ConfigurationSchema from file
- **configuration**: automatically compute "year" value in general configuration
- **commands**: rename new project command to "init" so the use is ipy init
- **commands**: integrate GitConfigurer to set up repository during project command
- **git**: automate initial commit during repository setup
- **git**: set user information during repository initialization
- **git**: add repository initialization method to GitConfigurer
- **git**: do nothing if git is not set to be configured
- **git**: add "setup_repository" method to GitConfigurer
- **git**: create GitConfigurer class with basic init arguments
- **configuration**: add methods to compute flag and name of dependencies inside DependencyConfiguration to not violate encapsulation
- **templates**: add new templates using new configuration nomenclature
- **commands**: add logic to instantiate and setup virtual environment using user dependency manager selection
- **configuration**: add property to expose python version easily
- **dependency-manager**: implement factory method to encapsulate instantiation of dependency manager based on user selection
- **configuration**: add dependency_manager property to configuration schema
- **dependency-manager**: implement concrete version of dependency manager  using pdm
- **dependency-manager**: create DependencyManager interface
- **dependency-manager**: implement "setup_environment" method to orchestrate all steps to install manager and dependencies
- **dependency-manager**: add command to create virtual environment in case no additional dependencies are specified
- **dependency-manager**: add logic to install dependencies with uv
- **dependency-manager**: implement "_install_python" method to install user python version using uv
- **dependency-manager**: implement "_install" method delegating command execution to a helper "_run_command" method
- **dependency-manager**: add _install method to UvDependencyManager
- **dependency-manager**: create UvDependencyManager class
- **project-creator**: implement "write_on_disk" method for FileSystem
- **project-creator**: let FileSystem constructor receive project structure as an argument
- **project-creator**: remove unnecessary arguments for FileSystem now that project structure gets injected
- **project-creator**: treat "create_folders_and_files" method as a named constructor that is in charge of creating the file system tree
- **project-creator**: add children to Directory __repr__ method
- **project-creator**: modify file system logic to receive rendered project structure injected instead of be coupled to how it gets generated
- **project-creator**: implement logic to fill file system files
- **project-creator**: raise error when file has not been created and its tried to be filled
- **project-creator**: implement FileHasNotBeenCreated application error
- **project-creator**: implement File fill method to be able to write template content inside
- **project-creator**: add template path attribute to File class to be able to locate the template with its content
- **project-creator**: implement FileSystem class to generate the directories and files of the project
- **configuration**: add property to expose project folder name based on configuration
- **project-creator**: create inner directories in Directory
- **project-creator**: inject children argument to Directory
- **project-creator**: when directory is defined as python module, create '__init__' file inside
- **project-creator**: implement logic to create directories
- **project-creator**: create Directory class with basic attributes
- **project-creator**: create boilerplate file at desired path
- **project-creator**: add '__repr__' method to BoilerplateFile class
- **project-creator**: implement BoilerplateFile extracting file name
- **project-creator**: define basic interface for different nodes
- **commands**: render project structure based on parsed configuration file
- **builder**: include 'has_dependency' custom filter in jinja environment
- **project-generator**: implement 'has_dependency' custom filter for jinja environment
- **configuration**: add ConfigurationSchemaPrimitives typed dict to type better to_primitives return
- **configuration**: add "template_type" property to know which template the user has selected
- **builder**: implement "get_project" method in JinjaProjectRender class
- **builder**: define interface of JinjaProjectRender
- **builder**: implement basic ProjectRender class with constructor to avoid linter fail
- **builder**: implement "render_template" method to be able to process a jinja template and render its content
- **builder**: include custom filter in jinja environment
- **builder**: initialize jinja environment
- **commands**: add new command that receives config file
- **configuration**: parse template configuration
- **configuration**: handler missing mandatory fields for git configuration
- **configuration**: parse git configuration
- **configuration**: parse dependencies configuration
- **configuration**: ensure all mandatory fields are present in general configuration
- **configuration**: parse general configuration
- **configuration**: verify all required keys are present in config file
- **configuration**: handle EmptyConfigurationNotAllowed error for empty config files
- **configuration**: create Parser class with parser method that raises single error
- **configuration**: add ConfigurationSchema to encapsulate general, dependency, template, and git configurations
- **configuration**: add template configuration management with validation for templates and built-in features
- **configuration**: implement GitConfiguration class to manage user settings
- **configuration**: add validation to ensure non-dev dependencies are not included in groups
- **configuration**: add DependencyConfiguration class to store dependencies parameters
- **configuration**: validate supported dependency managers in GeneralConfiguration
- **configuration**: add InvalidDependencyManagerValue error for unsupported dependency managers
- **configuration**: validate supported Python versions in GeneralConfiguration
- **configuration**: add InvalidPythonVersionValue error for unsupported Python versions
- **configuration**: validate passed license is supported by the application
- **configuration**: create application error when invalid license is passed
- **errors**: add configuration error to possible error types
- **configuration**: add GeneralConfiguration dataclass for project settings
- **configuration**: add configuration template for project setup

### 🐛 Bug Fixes

- **template**: correct reference to built_in_features in YAML clean architecture template
- **configuration**: rename TemplateStep key from 'template' to 'name'
- **renderer**: manually include pyproject.toml boilerplate file when making a project with custom template to be able to create virtual environment
- **templates**: correct accessing general information in LICENSE template
- **commands**: pass configuration dependencies directly when setting up environment
- **project-creator**: include TemplateTypes in context when rendering files
- **templates**: correct indentantions in new templates
- **dependency-manager**: correct test that verifies dependency installation command is called with group flag
- **dependency-manager**: do not use --dev and --group flag
- **project-creator**: correct boilerplate template example for test to have correct format
- **project-creator**: modify test method that extracts project file system structure to iterate the folders in order and avoid test failing only for different order
- **builder**: modify how test examples files are accessed to use a full path all the times
- **configuration**: return empty list of dependencies when configuration file has no dependencies specified
- **commands**: correct requirements access to slug variable
- **error**: correct message formatting in NotDevDependencyIncludedInGroup exception
- **configuration**: make dependencies field a list of DependencyConfiguration

### ♻️ Code Refactoring

- **dependency-manager**: do not print installed dependency in pdm manager
- **templates**: include default dependencies when github actions is selected and write a message in the README to inform the project has been created using ipy
- **errors**: remove errors folder
- **errors**: move ApplicationError and ErrorTypes to shared module
- **render**: move UnknownTemplateError to render module
- **project-creator**: move UnknownNodeTypeError to project_creator module
- **dependency-manager**: move UnknownDependencyManagerError to the dependency manager module
- **renderer**: move TemplateFileNotFoundError import to the render module
- **dependency-manager**: move CommandExecutionError import to dependency manager module
- **project-creator**: update type hints to ensure backward compatibility with older python versions
- **configuration**: replace hardcoded options with dynamic retrieval from SupportedLicenses, SupportedManagers, SupportedPythonVersions, and SupportedBuiltInFeatures
- **configuration**: update type hints to ensure backward compatibility with older python versions
- **configuration**: replace hardcoded template name with SupportedTemplates enum
- **configuration**: replace hardcoded built-in features with dynamic retrieval from SupportedBuiltInFeatures
- **configuration**: move SupportedTemplates to shared module
- **configuration**: replace hardcoded supported templates with dynamic retrieval from SupportedTemplates
- **configuration**: rename TemplateTypes to SupportedTemplates
- **configuration**: update supported licenses to use SupportedLicenses enum
- **configuration**: update supported python versions to use respective enums
- **configuration**: update supported dependency managers to use get_supported_managers method
- **shared**: rename Managers enum to SupportedManagers
- **configuration**: update supported dependency managers to use Managers enum
- **dependency-manager**: move Managers enum to shared folder
- **templates**: rename new_templates folder to templates now that old templates folder have been removed
- **templates**: remove old templates files
- **installer**: remove old installer folder
- **dependency-manager**: move managers enum to dependency_manager folder
- **installer**: remove old installer files
- **prompter**: remove old question prompter folder
- **project-creator**: use TemplateTypes enum from configuration
- **project-generator**: remove old project generator folder
- **renderer**: move jinja_custom_filters.py to renderer folder
- **project-generator**: remove old files for generating the project
- **prompter**: remove old questions and steps
- **commands**: rename project file with init command to init
- **commands**: remove folder_cli and project_cli commands
- **cli**: remove folder_cli and project_cli from CLI application
- **configuration**: rename question step files for consistency and clarity
- **configuration**: set default value for _config_file_path in ConfigurationSchema
- **parser**: extract configuration parsing logic into separate method for improved readability
- **parser**: rename parse method to parse_from_file for clarity
- **configuration**: refactor question steps to inherit from Step interface
- **configuration**: move steps to its own folder inside configuration
- **parser**: use ConfigurationSchema named constructor to generate parsed config from user file
- **git**: enhance repository setup with informative messages
- **dependency-manager**: avoid accessing dependency configuration internal data and delegate behavior to it
- **dependency-manager**: modify uv dependency manager type hint to receive a list of DependencyConfiguration
- **dependency-manager**: move "_run_command" method to DependencyManager class to be reused by other implementations
- **dependency-manager**: let UvDependencyManager implement DependencyManager interface
- **dependency-manager**: add attribute _uv to store the name of uv command
- **dependency-manager**: add print statements to inform the user about what is happening
- **dependency-manager**: reorganize the logic to build the command for installing dependencies
- **dependency-manager**: extract "_build_dependency_install_command" method to encapsulate the logic of creating the command needed to install a dependency
- **dependency-manager**: extract "_create_virtual_environment" method to express what uv sync command is doing
- **commands**: update project command to use new "write_on_disk" file system method to create the project on disk
- **project-creator**: remove unused create_folders_and_files method
- **project-creator**: rename "build_tree" method to "build_node"
- **project-creator**: store in a list all the files that are created in the project file system
- **project-creator**: when creating a File save its path to be able to recover it when filling it
- **project-creator**: extract setup_method for file tests to clean up file creation
- **commands**: allow to execute new project command
- **commands**: change how new project command is handled using directly FyleSystem class
- **render**: rename JinjaProjectRender to JinjaProjectRenderer
- **render**: modify JinjaProjectRender return type hint
- **configuration**: modify configuration parser test for happy paths using approvaltests to verify expected configuration gets parsed correctly instead of making lots of separate tests for each section of the configuration
- **render**: remove expected project json files for tests
- **render**: modify tests to use approvaltest and don't need expected project json files
- **project-creator**: update teardown_method to delete correctly directories generated on tests
- **project-creator**: modify directory tests to use object mother
- **render**: modify resources test projects to not contain "root" key
- **project-creator**: make Directory inherit from Node interface
- **project-creator**: remove children argument from directory
- **project-creator**: modify teardown_method to delete files inside directory after test
- **project-creator**: rename boilerplate file to file
- **commands**: add type hint to project command
- **render**: rename builder module to render
- **builder**: remove old project_render.py and test
- **builder**: parametrize jinja project render tests
- **builder**: modify main_structure.yml.j2 for test case with dependency
- **builder**: load expected project structure from JSON file instead of hardcoding
- **builder**: rename config file to 'clean_architecture_config.yml' and update test to reflect the change
- **builder**: set template base dir as argument of 'render_project_structure' method instead of argument to constructor
- **builder**: rename constant for main structure template
- **builder**: remove 'main_structure_template' argument from render constructor as the main file must always be named main_structure.yml.j2
- **builder**: modify JinjaProjectRender arguments for test to point to test example project yml
- **builder**: rename "get_project" method to express better the intention of the method
- **builder**: move example template yml of project for test
- **builder**: parametrize base dir for template and main file to not be coupled to production structure when testing
- **configuration**: use typed dict to type "to_primitives" return method
- **configuration**: avoid possibility of accessing GeneralConfiguration class variables
- **builder**: add setup method to jinja environment test class to clean up jinja env instantiation
- **builder**: pass package name and template directory to jinja environment to be able to differentiate between production templates and test templates
- **cli**: rename instant_python_typer correctly and add missing type hints
- **template**: modify domain error templates to avoid repeating implementation of type and message properties
- modify all application errors to pass message and type error to base error and not implement neither type or message properties
- **error**: modify ApplicationError to pass the message and type and avoid repeating the same pattern to return the message and type of error
- **configuration**: handle when template config mandatory field is missing
- **configuration**: modify config.yml file to only include template name
- **configuration**: modify config examples for test to have git fields with same name as class argument
- **configuration**: pass parsed arguments to configuration classes using ** operator with dicts and handle TypeError to detect missing mandatory fields
- **configuration**: automatically cast attributes value to string in case yaml reading gets interpreted as a float
- **configuration**: modify config examples for test to have is_dev field with same name as class argument
- **configuration**: modify test assertion to compare expected dependencies with parsed dependencies configuration
- **tests**: update config file path handling to remove file extension
- **configuration**: extract helper function to build config file path for tests
- **configuration**: remove unnecessary empty check in tests
- **configuration**: temporarily set dependencies, template and git configs to not needed when initializing ConfigurationSchema to be able to test it step by step
- **configuration**: convert constants to class variables
- **configuration**: modify configuration errors to pass wrong value and supported values instead of accessing them
- **configuration**: create auxiliar methods for better readability when extracting config file content
- **configuration**: extract semantic method to encapsulate reading configuration file
- **configuration**: modify parse method to open config file
- **configuration**: reorganize configuration files in subfolders to expose clearer the concepts of the configuration
- **configuration**: join unsupported values test in a parametrized test
- **configuration**: move supported constants to a separate file to avoid circular import errors
- **prompter**: rename project_slug to slug for consistency across templates
- **cli**: move folder and project cli commands to specific command module

## 0.5.2 (2025-04-16)

### 🐛 Bug Fixes

- **template**: fix project slug placeholder in README template

## 0.5.1 (2025-04-15)

### 🐛 Bug Fixes

- **cli**: manage and detect correctly raised exceptions and exit the application with exit code 1

## 0.5.0 (2025-04-15)

### ✨ Features

- **cli**: create main application based on custom implementation and add error handlers
- **cli**: implement a custom version of Typer application to be able to handle exceptions in FastAPI way using decorators
- **errors**: add UnknownTemplateError for handling unknown template types
- **errors**: add TemplateFileNotFoundError for missing template files and extend ErrorTypes with GENERATOR
- **errors**: add ErrorTypes enum for categorizing error types
- **errors**: add CommandExecutionError for handling command execution failures
- **errors**: add UnknownDependencyManagerError for handling unknown dependency managers
- **installer**: remove unused PYENV manager from Enum
- **errors**: create application error to be able to capture all expected errors

### 🐛 Bug Fixes

- **errors**: correct typo in UnknownTemplateError message

### ♻️ Code Refactoring

- **project-generator**: manage when a command fails by raising custom CommandExecutionError
- **installer**: manage when a command fails by raising custom CommandExecutionError
- **cli**: enhance error handling with rich console output
- **project-generator**: raise UnknownTemplateError for unknown template types
- **project-generator**: move UnknownErrorTypeError to errors module and inherit from ApplicationError
- **project-generator**: raise TemplateFileNotFoundError for missing template files
- **errors**: use ErrorTypes enum for error type in CommandExecutionError and UnknownDependencyManagerError
- **installer**: add stderr handling for subprocess calls
- **installer**: raise UnknownDependencyManagerError for unknown user managers

## 0.4.0 (2025-04-11)

### ✨ Features

- **template**: add README template and include in main structure

## 0.3.0 (2025-04-11)

### ✨ Features

- **project-generator**: add support for creating user File instances in folder tree
- **project-generator**: create new File class to model user files
- **project-generator**: create JinjaEnvironment class to manage independently jinja env

### 🐛 Bug Fixes

- **template**: correct IntValueObject template to call super init
- **template**: remove unnecessary newline in template import
- **template**: correct typo in jinja template

### ♻️ Code Refactoring

- **template**: modify all template file types
- **project-generator**: rename File class to BoilerplateFile to be able to differentiate a normal file introduced by the user and a file of the library that contains boilerplate
- **cli**: update template command parameter from template_name to template_path
- **cli**: rename configuration variable name from user_requirements to requirements
- **prompter**: modify configuration file name from user_requirements.yml to ipy.yml
- **prompter**: rename UserRequirements to RequirementsConfiguration
- **project-generator**: rename DefaultTemplateManager to JinjaTemplateManager
- **project-generator**: delegate jinja env management to JinjaEnvironment in DefaultTemplateManager

## 0.2.0 (2025-04-08)

### ✨ Features

- **template**: add new rabbit mq error when user selects event bus built in feature
- **template**: create rabbit_mq_connection_not_established_error.py boilerplate

### 🐛 Bug Fixes

- **template**: correct domain event type not found error import and class name
- **template**: set event bus publish method async
- **template**: correct imports in value objects boilerplate

### ♻️ Code Refactoring

- **installer**: add virtual environment creation before installing dependencies
- **template**: conditionally include bounded context based on specify_bounded_context field
- **template**: add specify_bounded_context field to user requirements
- **prompter**: be able to execute nested conditional questions
- **template**: update subquestions structure to use ConditionalQuestion for bounded context specification
- **prompter**: extend ConditionalQuestion subquestions type hint
- **prompter**: remove note when prompting built in features for the user to select and remove temporarily synch sql alchemy option
- **template**: modify project structure templates to include logger and alembic migrator automatically if fastapi application is selected
- **template**: modify DomainEventSubscriber boilerplate to follow generic type syntax depending on python version

## 0.1.1 (2025-04-08)

### 🐛 Bug Fixes

- **template**: correct typo in ExchangeType enum declaration
- **template**: correct typo on TypeVar declaration

### ♻️ Code Refactoring

- **question**: use old generic type syntax to keep compatibility with old python versions
- **template**: update boilerplates so they can adhere to correct python versions syntax
- **project-generator**: standardize path separator in file name construction
- **installer**: remove unused enum OperatingSystems
- **prompter**: change TemplateTypes class to inherit from str and Enum for improved compatibility
- **project-generator**: change NodeType class to inherit from str and Enum for improved compatibility
- **installer**: change Managers class to inherit from str and Enum for better compatibility
- **project-generator**: remove override typing decorator to allow lower python versions compatibility

## 0.1.0 (2025-04-06)

### 🐛 Bug Fixes

- **project-generator**: add template types values to be able to use enum in jinja templates
- **template**: write correct option when fastapi built in feature is selected
- **template**: generate correctly the import statement in templates depending on the user selection
- **installer**: correct answers when installing dependencies
- **prompter**: modify DependenciesQuestion to not enter an infinite loop of asking the user
- **cli**: temporarily disable template commands
- **prompter**: extract the value of the base answer to check it with condition
- **prompter**: remove init argument from year field
- **cli**: access project_name value when using custom template command
- **prompter**: set default value for git field in UserRequirements to avoid failing when executing folder command
- **prompter**: include last question in TemplateStep if selected template is domain_driven_design
- **project-generator**: instantiate DefaultTemplateManager inside File class
- **build**: change build system and ensure templates directory gets included
- **project-generator**: substitute FileSystemLoader for PackageLoader to safer load when using it as a package
- **prompter**: correct default source folder name
- **template**: correct license field from pyproject.toml template
- **template**: use project_slug for project name inside pyproject.toml
- **project-generator**: correct path to templates
- **project-generator**: correct extra blocks that where being created when including templates

### ♻️ Code Refactoring

- **template**: include mypy, git and pytest configuration files only when the user has selected these options
- **template**: include dependencies depending on user built in features selection
- **prompter**: update answers dictionary instead of add manually question key and answer
- **prompter**: return a dictionary with the key of the question and the answer instead of just the answer
- **cli**: modify cli help commands and descriptions
- **prompter**: modify default values for UserRequirements
- **cli**: use new GeneralCustomTemplateProjectStep in template command
- **cli**: add name to command and rename command function
- **prompter**: substitute template and ddd specific questions in TemplateStep for ConditionalQuestion
- **prompter**: substitute set of question in GitStep for ConditionalQuestion
- **prompter**: remove should_not_ask method from Step interface
- **prompter**: remove DomainDrivenDesignStep
- **cli**: remove DDD step and add TemplateStep
- **prompter**: remove boilerplate question from DependenciesStep
- **prompter**: remove template related questions from GeneralProjectStep
- **prompter**: move git question to GitStep and remove auxiliar continue_git question
- **cli**: rename function names for better clarity
- **cli**: move new command to its own typer app
- **cli**: move folder command to its own typer app and separate the app in two commands
- **project-generator**: let DefaultTemplateManager implement TemplateManager interface
- **project-generator**: rename TemplateManager to DefaultTemplateManager
- **cli**: add template argument to both command to begin allow the user to pass a custom path for the project structure
- **cli**: add help description to both commands
- **prompter**: move python and dependency manager from dependencies step to general project step as it's information that is needed in general to fill all files information
- **cli**: rename generate_project command to new
- **prompter**: add file_path field to user requirements class
- **cli**: pass project slug name as the project directory that will be created
- **project-generator**: pass the directory where the project will be created to FolderTree
- **cli**: remove checking if a user_requirements file exists
- **template**: remove writing author and email info only if manager is pdm
- **installer**: avoid printing executed commands output by stdout
- **template**: use git_email field in pyproject.toml
- **prompter**: remove email field from UserRequirements and add git_email and git_user_name
- **prompter**: remove email question from general project step
- **project-generator**: remove condition of loading the template only when is domain driven design
- **template**: use include_and_indent custom macro inside domain_driven_design/test template
- **template**: include always mypy and pytest ini configuration
- **prompter**: rename empty project template to standard project
- **cli**: use DependencyManagerFactory instead of always instantiating UvManager
- **installer**: remove ShellConfigurator and ZshConfigurator
- **cli**: remove shell configurator injection
- **installer**: remove the use of ShellConfigurator inside installer
- **prompter**: warn the user that project name cannot contain spaces
- **prompter**: remove project name question and just leave project slug
- **installer**: remove executable attribute from UvManager
- **installer**: specify working directory to UvManager so it installs everything at the generated project
- **cli**: pass generated project path to UvManager
- **installer**: inline uv install command attribute as is not something reusable
- **cli**: inject folder tree and template manager to project generator
- **project-generator**: set the directory where user project will be generated as FolderTree attribute and expose it through a property
- **project-generator**: pass folder_tree and template_manager injected into ProjectGenerator
- **cli**: pass user dependencies to installer
- **prompter**: substitute fixed default dependencies by dynamic ones that will be asked to the user
- **prompter**: remove question definition lists and basic prompter
- **cli**: substitute BasicPrompter for QuestionWizard
- **prompter**: remove python manager and operating system questions
- **prompter**: extract helper method to know if template is ddd
- **prompter**: delegate ask logic to each question instead of letting prompter what to do depending on flags
- **prompter**: redefine questions using concrete implementations
- **prompter**: make Question abstract and add ask abstract method
- **project-generator**: rename Directory's init attribute to python_module and remove default value for children
- **project-generator**: move children extraction only when node is a directory
- **src**: remove old src folder with cookiecutter project and convert current instant_python module into src
- **cli**: generate user requirements only if no other file has been already generated.
- **template**: move makefile template to scripts folder as this folder only makes sense if it's use with the makefile
- **template**: move base from sync sqlalchemy to persistence folder as it would be the same for both sync and async
- **template**: move sqlalchemy sync templates to specific folder
- **template**: move exceptions templates to specific folder
- **template**: move value object templates to specific folder
- **template**: move github actions templates to specific folder
- **template**: move logger templates to specific folder
- **project-generator**: modify File class to be able to manage the difference between the path to the template and the path where the file should be written
- **template**: change all yml templates to point to inner event_bus folder boilerplate
- **template**: move all boilerplate related to event bus inside specific folder
- **prompter**: change github information for basic name and email
- **prompter**: move default dependencies question to general questions and include the default dependencies that will be included
- **prompter**: remove converting to snake case all answers and set directly those answers in snake case if needed
- **templates**: use raw command inside github action instead of make
- **templates**: modify error templates to use DomainError
- **templates**: change all python-module types to directory and add python flag when need it
- **project-generator**: make Directory general for any type of folder and remove python module class
- **project-generator**: remove python_module node type
- **templates**: set all files of type file and add them the extension variable
- **project-generator**: add extension field to node and remove deprecated options
- **project-generator**: create a single node type File that will work with any kind of file
- **project-generator**: substitute python file and yml file node type for single file
- **templates**: use new operator to write a single children command in source
- **project-generator**: include new custom operator in jinja environment
- **templates**: remove populated shared template
- **templates**: include value objects template when is specified by the user
- **templates**: import and call macro inside project structures templates
- **prompter**: format all answers to snake case
- use TemplateTypes instead of literal string
- **project-generator**: change template path name when generating project
- **templates**: move ddd templates inside project_structure folder
- **prompter**: migrate BasicPrompter to use questionary instead of typer to make the questions as it manages multiple selections better
- **cli**: instantiate BasicPrompter instead of using class method
- **prompter**: simplify ask method by using Question object an iterating over the list of defined questions
- **templates**: modularize main_structure file
- **project-generator**: create project structure inside a temporary directory
- **project-generator**: delegate template management to TemplateManager
- **cli**: call BasicPrompter and ProjectGenerator inside cli app


### ✨ Features

- **project-generator**: create new custom function to generate import path in templates
- **prompter**: implement general project step that will only be used when custom template is passed
- **cli**: add template command for project_cli.py to let users create a project using a custom template
- **prompter**: implement ConditionalQuestion
- **prompter**: implement TemplateStep to group all questions related to default template management
- **project-generator**: implement CustomTemplateManager to manage when user passes a custom template file
- **project-generator**: create TemplateManager interface
- **cli**: add folder command to allow users to just generate the folder structure of the project
- **project-generator**: format all project files with ruff once everything is generated
- **cli**: remove user_requirements file once project has been generated
- **prompter**: add remove method to UserRequirements class
- **cli**: call to git configurer when user wants to initialize a git repository
- **installer**: implement GitConfigurer
- **cli**: include git step into cli steps
- **prompter**: implement step to ask the user information to initialize a git repository
- **template**: add clean architecture template project structure
- **template**: add standard project project structure templates
- **installer**: create factory method to choose which dependency manager gets instantiated
- **installer**: implement PdmInstaller
- **project-generator**: expose generated project path through ProjectGenerator
- **installer**: add project_directory field to UvManager to know where to create the virtual environment
- **installer**: add install_dependencies step to Installer
- **installer**: implement logic to install dependencies selected by the user in UvManager
- **installer**: add install_dependencies method to DependencyManger interface
- **prompter**: implement DependencyQuestion to manage recursive question about what dependencies to install
- **prompter**: implement DependenciesStep with all questions related to python versions, dependencies etc.
- **prompter**: implement DomainDrivenDesignStep with bounded context questions.
- **prompter**: implement GeneralProjectStep that will have common questions such as project name, slug, license etc.
- **prompter**: implement Steps collection and Step interface
- **prompter**: implement QuestionWizard to separate questions into steps and be more flexible and dynamic
- **cli**: install uv by default and python version specified by the user
- **installer**: implement Installer that will act as the manager class that coordinates all operation required to fully install the project
- **installer**: implement zsh shell configurator
- **installer**: create ShellConfigurator interface
- **installer**: implement UvManager that is in charge of installing uv and the python version required by the user
- **installer**: add dependency manager interface
- **installer**: include enums for managers options and operating systems
- **prompter**: add question to know user's operating system
- **prompter**: create MultipleChoiceQuestion for questions where the user can select zero, one or more options
- **prompter**: create BooleanQuestion for yes or no questions
- **prompter**: create FreeTextQuestion for those questions where the user has to write something
- **prompter**: create ChoiceQuestion to encapsulate questions that have different options the user needs to choose from
- **project-generator**: create custom exception when node type does not exist
- **cli**: make sure user_requirements are loaded
- **prompter**: add load_from_file method to UserRequirements
- **template**: include mock event bus template for testing
- **template**: add scripts templates
- **prompter**: add fastapi option to built in features
- **template**: include templates for fasta api application with error handlers, http response modelled with logger
- **prompter**: add async alembic to built in features options
- **template**: include templates for async alembic
- **prompter**: add async sqlalchemy to built in features options
- **template**: add templates for async sqlalchemy
- **prompter**: include logger as built in feature
- **template**: add template for logger
- **prompter**: include event bus as built in feature
- **templates**: add project structure template for event bus
- **templates**: add LICENSE template
- **prompter**: add year to user requirements fields with automatic computation
- **templates**: include mypy and pytest init files when default dependencies are selected
- **templates**: add .python-version template
- **templates**: add .gitignore template
- **templates**: add pyproject template
- **templates**: add makefile template
- **templates**: add invalid id format error template
- **templates**: add domain error template
- **prompter**: add synchronous sqlalchemy option to built in features question
- **templates**: add synchronous sqlalchemy template
- **project-generator**: create custom operator to be applied to jinja templates
- **prompter**: add pre commit option to built in features question
- **templates**: add pre commit template
- **prompter**: add makefile option to built in features question
- **templates**: add makefile template
- **templates**: separate value objects folder template in a single yml file
- **templates**: add macro to include files easier and more readable
- **project-generator**: add TemplateTypes enum to avoid magic strings
- **prompter**: add question to know which features the user wants to include
- **prompter**: implement new function to have multiselect questions
- **prompter**: define all questions in a separate file
- **prompter**: create Question class to encapsulate questions information
- **project-generator**: create YamlFile class to create yaml files
- **project-generator**: create Directory class to create simple folders
- **templates**: add templates to create github actions and workflows
- **project-generator**: create NodeType enum to avoid magic strings
- **templates**: add python files boilerplate
- **project-generator**: implement logic to create python files with boilerplate content
- **project-generator**: create specific class to manage jinja templates
- **prompter**: add save_in_memory method to UserRequirements
- **project-generator**: implement logic to create python modules
- **templates**: create DSL to set the folder structure
- **project-generator**: create classes to model how python files and modules would be created
- **project-generator**: delegate folder generation to folder tree class
- **project-generator**: create manager class in charge of creating all project files and folders
- **prompter**: create class to encapsulate user answers
- **prompter**: create basic class that asks project requirements to user
- **cli**: create basic typer application with no implementation

