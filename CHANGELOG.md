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

