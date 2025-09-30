# CHANGELOG

<!-- version list -->

## v0.11.0 (2025-09-30)

### ✨ Features

- **templates**: Add ruff linter and formatter rules in pyproject.toml template file
  ([`b600f62`](https://github.com/dimanu-py/instant-python/commit/b600f62ab807d0ed5309ee199fd6b772dad55317))

### 🪲 Bug Fixes

- **templates**: Correct imports when selected template was standard project
  ([`4d8bda4`](https://github.com/dimanu-py/instant-python/commit/4d8bda4fb246a59e5556c78b5317845614e3f8b5))

### ♻️ Refactoring

- **templates**: Modify makefile template file simplifying add-dep and remove-dep commands
  ([`eb883f3`](https://github.com/dimanu-py/instant-python/commit/eb883f31aba41faf8b38908317ea02b53e700874))

- **templates**: Rename template file for base error
  ([`3a30d3d`](https://github.com/dimanu-py/instant-python/commit/3a30d3d3533bc88fe70f0822f204d34e3ad4280a))

- **commands**: Move ipy configuration file to project folder before creating first commit
  ([`8997e98`](https://github.com/dimanu-py/instant-python/commit/8997e984b2384e70ca2418e4cf7eb21aa3d7bdad))


## v0.10.0 (2025-09-30)

### ✨ Features

- **templates**: Add 'changelog_file' entry to semantic release section in pyproject template to
  avoid warning
  ([`0a80d5a`](https://github.com/dimanu-py/instant-python/commit/0a80d5a4dc1cec80259d4d6e9ba0ac0a9581fc6a))

### 🪲 Bug Fixes

- **templates**: Correct errors import in fastapi application template
  ([`e42cfbb`](https://github.com/dimanu-py/instant-python/commit/e42cfbb0116fa52596be60121a27bb6ee39e10cf))

- **templates**: Correct errors in release.yml template
  ([`65b96f0`](https://github.com/dimanu-py/instant-python/commit/65b96f0a0c890e18e597fb4edc4c8402b733d84d))

### ⚙️ Build System

- Add 'dev' dependency group for improved development workflow
  ([`37d4c25`](https://github.com/dimanu-py/instant-python/commit/37d4c250696c07cb22b8a594b5d68309a1659c83))

- Update dependencies
  ([`31572ab`](https://github.com/dimanu-py/instant-python/commit/31572ab38b253abfee97f3e8926499e0a8f57a00))


## v0.9.1 (2025-07-18)

### 🪲 Bug Fixes

- **cli**: Update command in tox.ini file to be able to make reference to new location for application entry point ([`a8baef2`](https://github.com/dimanu-py/instant-python/commit/a8baef2eb88018cb6a0210122348e753dc10cacb))

- **templates**: Update pyproject.toml template to include optional build dependencies when github actions built-in feature is selected ([`b765ec8`](https://github.com/dimanu-py/instant-python/commit/b765ec81f3e61ce170873eaed371910e41e2e871))

- **templates**: Update release action template to work running build command to update uv.lock ([`9824451`](https://github.com/dimanu-py/instant-python/commit/982445188567c61d31ffc11d04ccdab163fb1ee4))

### ⚙️ Build System

- Update changelog section in semantic release config ([`7a413cf`](https://github.com/dimanu-py/instant-python/commit/7a413cf7a95b4da30ef23efafdf94cb2e2118168))

- Update application entry point ([`8b5330a`](https://github.com/dimanu-py/instant-python/commit/8b5330a99ae432dc0e04c19f67ccc55e5ee9fe5a))

### ♻️ Refactoring

- **cli**: Move cli files to its own folder ([`81b8c3c`](https://github.com/dimanu-py/instant-python/commit/81b8c3c3839bf548a5ffac3432615d392ad2a05e))

- **templates**: Update name of test workflow ([`80225f5`](https://github.com/dimanu-py/instant-python/commit/80225f51014aef1d06660803aa0fec65633f41bd))

## v0.9.0 (2025-07-18)

### ✨ Features

- **templates**: Add github action release to project structure for github actions ([`9e3309f`](https://github.com/dimanu-py/instant-python/commit/9e3309f8154a72954427f947ae61753d37253060))

- **templates**: Include python semantic release library in default dependencies if github actions is selected ([`5374ba4`](https://github.com/dimanu-py/instant-python/commit/5374ba4e77f8790dc6d5b691d3f511889df87f24))

- **shared**: Add github issues template as possible built in feature ([`9d97ce5`](https://github.com/dimanu-py/instant-python/commit/9d97ce53baded8ed6e782ea437daa9110c74c316))

- **templates**: Add template for release with python semantic release ([`23569a0`](https://github.com/dimanu-py/instant-python/commit/23569a0bafb33b1726beab47bf11e6f7fde95065))

- **templates**: Include github issues template into project structure templates ([`36a2975`](https://github.com/dimanu-py/instant-python/commit/36a2975e726db3172965e2f8866b2af48488c193))

- **templates**: Add templates for github issues templates ([`fec68e4`](https://github.com/dimanu-py/instant-python/commit/fec68e48418875c57e98a16dbc041e3eeeffdea9))

- **templates**: Include pip audit and precommit as default dependencies if they are selected as built in features ([`86a8af5`](https://github.com/dimanu-py/instant-python/commit/86a8af5592c03046d0228131beb4b9718bd00f57))

- **templates**: Include audit command in makefile template if github actions is selected ([`8035fab`](https://github.com/dimanu-py/instant-python/commit/8035fab7a66b1735da07d6a750bc754b1f6c4d48))

- **templates**: Modify project structure for github action including joined ci workflow ([`4ae4bd7`](https://github.com/dimanu-py/instant-python/commit/4ae4bd77d292697761dd4b631a6f87b32dc0796e))

- **templates**: Join lint and test github workflows into one single file and include more security and code quality jobs ([`a21eafe`](https://github.com/dimanu-py/instant-python/commit/a21eafebc11da2fe2d440acdfc96e3d6910e8bdc))

- **shared**: Include security as supported built in feature ([`5cfa228`](https://github.com/dimanu-py/instant-python/commit/5cfa228abca91b5e0d09ca7f68baa0a910f5da26))

- **templates**: Include security template into project structures ([`65c9b84`](https://github.com/dimanu-py/instant-python/commit/65c9b849f2b37faf5c0fcae8993e9981b71da829))

- **templates**: Create security file template ([`21b1bb0`](https://github.com/dimanu-py/instant-python/commit/21b1bb0257e1caa23db66e645e9e047010c10920))

- **shared**: Add citation as supported built in feature ([`893abab`](https://github.com/dimanu-py/instant-python/commit/893abab4e16a66b0da7e8b9e26d2f2ed452453d5))

- **templates**: Add citation project structure template to default templates ([`0a798d5`](https://github.com/dimanu-py/instant-python/commit/0a798d57642eb990f42b2e614d840f543829c767))

- **templates**: Add citation file template ([`888e8c6`](https://github.com/dimanu-py/instant-python/commit/888e8c696ad1ab2ce9916fa4a85c6ceae529cf14))

- **shared**: Add precommit option in SupportedBuiltInFeatures enum ([`f69cadb`](https://github.com/dimanu-py/instant-python/commit/f69cadb733634a6ecb4e9ab092e2a2bb375f98c9))

- **templates**: Include precommit template project structure in all default templates ([`8601841`](https://github.com/dimanu-py/instant-python/commit/8601841cb74c7a3a68b1d06daa89c25b3b23c0f3))

- **templates**: Include specific make commands in template based on installed dependencies and selected built in features ([`62688c0`](https://github.com/dimanu-py/instant-python/commit/62688c072cb6bfa1d00e7f6a08f82a1ed975aa8e))

- **templates**: Include pre commit hook in makefile if it's selected as built in features ([`2c391fb`](https://github.com/dimanu-py/instant-python/commit/2c391fb6c1c69990ae551c6bf8621bb1b40811d1))

- **templates**: Update pre commit config file to be included as built in feature ([`972aaa4`](https://github.com/dimanu-py/instant-python/commit/972aaa4131e54d3e875b14e3d117ea30a23bc0e9))

- **templates**: Include new base aggregate in value objects and when in EDA project structure ([`4f038ef`](https://github.com/dimanu-py/instant-python/commit/4f038ef59fd4f0c54ba2880c4a505984560a4254))

- **templates**: Create base aggregate class and make aggregate for event driven architecture inherit from it ([`44f843d`](https://github.com/dimanu-py/instant-python/commit/44f843de0c6fcf739309f37350e9ba8b4c7bc650))

- **templates**: Include error handlers in fastapi application template for project structure ([`add3634`](https://github.com/dimanu-py/instant-python/commit/add36343fb11e4be42c96dca42ef00153d178187))

- **templates**: Separate template files for fastapi error handlers ([`cfd7d14`](https://github.com/dimanu-py/instant-python/commit/cfd7d14cd1f515b513774df5f25f2180baee2cb3))

- **templates**: Include new model for value objects in project structure ([`39d2ba1`](https://github.com/dimanu-py/instant-python/commit/39d2ba101aab089addd80ce38ee1753c0dff7883))

- **templates**: Update value object templates to use new version that autovalidates using @validate decorator ([`186ecd5`](https://github.com/dimanu-py/instant-python/commit/186ecd518b8c9ca685a4db04598eb55e27fc3316))

- **templates**: Update project structure templates that were using old version of domain error an include error base class as well as rename the folder to errors instead of exceptions ([`5c363b6`](https://github.com/dimanu-py/instant-python/commit/5c363b6e126942531f6bb1ca5990ede9dc92bf18))

- **templates**: Implement new error template as base class for errors and let domain error inherit from it ([`1e15d5d`](https://github.com/dimanu-py/instant-python/commit/1e15d5d58dbb583fb681df648ddda573ef2c1679))

- **templates**: Update logger project structure template to include new handler and new logger implementation ([`b33bd1e`](https://github.com/dimanu-py/instant-python/commit/b33bd1e4021006b236607d28dd7472431bfc3ddf))

- **templates**: Include log middleware in fastapi application project structure if logger is selected ([`4ca7641`](https://github.com/dimanu-py/instant-python/commit/4ca76411a0f906ec51aac38653ec29cec9cdf9b1))

- **templates**: Update fastapi main application template to include log middleware if logger is selected too ([`c92810c`](https://github.com/dimanu-py/instant-python/commit/c92810ce79b199892a03ce7e29dd03daacf00130))

- **templates**: Create fastapi log middleware template ([`b196afc`](https://github.com/dimanu-py/instant-python/commit/b196afce1838180439c2a4a900816fdda5063ef5))

- **templates**: Modify fastapi main application template with new logger ([`021039d`](https://github.com/dimanu-py/instant-python/commit/021039de56a92bf018dbbbd68d57bc60bbd2126d))

- **templates**: Add new templates for logger implementation ([`d937478`](https://github.com/dimanu-py/instant-python/commit/d9374786fd1cb95c89933331b678ef6fa0e2d7cf))

- **templates**: Remove http_response and status_code templates ([`5f75969`](https://github.com/dimanu-py/instant-python/commit/5f759699f15818cf0b73e9c88e13cc4ff567dc57))

- **templates**: Use new response model in fastapi error handlers ([`ef4e543`](https://github.com/dimanu-py/instant-python/commit/ef4e54308ae783360fb0eaa75fab8642c896a0d7))

- **templates**: Substitute http_response and status_code templates from fastapi infra for success and error responses model ([`2c086be`](https://github.com/dimanu-py/instant-python/commit/2c086bebdb646d34447f82f2cdf93aef894b0e66))

- **templates**: Add ErrorResponse and SuccessResponse templates for fastapi application ([`9ec98f1`](https://github.com/dimanu-py/instant-python/commit/9ec98f1e8db59386f76c636825f889f117ff9871))

### 🪲 Bug Fixes

- **templates**: Add semantic release config to pyproject template if github actions is selected ([`a6533ce`](https://github.com/dimanu-py/instant-python/commit/a6533ceeb62b2877b5698f4ca39eb1e4cdb2a374))

- **templates**: Fix indentations in github actions templates ([`cd0d882`](https://github.com/dimanu-py/instant-python/commit/cd0d88293612e4e83206615b903ff40af69b5dac))

- **templates**: Add {% raw %} and {% endraw %} tags in github actions templates when they access repository variables ([`46ec5c1`](https://github.com/dimanu-py/instant-python/commit/46ec5c1489b937065b6ebd8a1723ae581adc9445))

- **templates**: Correct forma of helper scripts when makefile built in feature is selected and include custom hooks only if precommit feature is not selected ([`fe15d7e`](https://github.com/dimanu-py/instant-python/commit/fe15d7e7521bd70879490e1a96973477524518f3))

- **templates**: Correct error in conditional in makefile template ([`b126eed`](https://github.com/dimanu-py/instant-python/commit/b126eed146787cf254070e4169afbde1433b5ce2))

- **templates**: Use selected dependency manager for new make commands ([`80bf833`](https://github.com/dimanu-py/instant-python/commit/80bf8333d06facae66b3f15992f0d59bc5bab785))

- **templates**: Include makefile if precommit built in feature is selected ([`9dcec97`](https://github.com/dimanu-py/instant-python/commit/9dcec97973b1a91a78d2bdf11a3bd20e097e8c68))

- **templates**: Write correct name for aggregate template file in value objects project structure ([`d651243`](https://github.com/dimanu-py/instant-python/commit/d651243d7baf602f262ed63d31bc4b0d0c2c2952))

- **render**: Create jinja environment with autoscape argument enabled to avoid potential XSS attacks ([`976d459`](https://github.com/dimanu-py/instant-python/commit/976d459538ae8eea403c65300304e6405fec46b6))

- **templates**: Format correctly if statement in application.py template ([`409d606`](https://github.com/dimanu-py/instant-python/commit/409d6064d97ef016c34dab57d3c9456a47e6542f))

- **templates**: Include logger and migrator in fastapi application only if they are selected too for DDD and standard project templates ([`f5a8087`](https://github.com/dimanu-py/instant-python/commit/f5a80870d0ecdd2f47419ad5e51d20131649b422))

- **templates**: Include logger and migrator in fastapi application only if they are selected as built in feature too in clean architecture template ([`191d81f`](https://github.com/dimanu-py/instant-python/commit/191d81fd8ace560f3a6359bc9cf767c73c310d50))

### ⚙️ Build System

- Modify release job and semantic release configuration to be able to update uv.lock with the new version ([`2d52828`](https://github.com/dimanu-py/instant-python/commit/2d5282804956e4e5ab31c20b320663f9184f0a84))

- Update version in uv.lock ([`9d1bd2c`](https://github.com/dimanu-py/instant-python/commit/9d1bd2c380293c7e1635a03da0654e7084b9e1eb))

- Update semantic release to not update major version if is zero and to allow 0 major version ([`34d251e`](https://github.com/dimanu-py/instant-python/commit/34d251e8a57eafa595a0c54e314238f389218dd6))

- Remove test hook in precommit config ([`b8d451d`](https://github.com/dimanu-py/instant-python/commit/b8d451db1a024ae41a6958dbf9513801f3b69627))

- Remove final echo from makefile commands to let output of the command itself inform the user ([`cd895ad`](https://github.com/dimanu-py/instant-python/commit/cd895adacfe1e470a746165380369c9c365996e8))

- Remove -e command from echo in makefile ([`6a624a3`](https://github.com/dimanu-py/instant-python/commit/6a624a3cacf8b96adaeba20bb635b7e43d853002))

- Exclude resources folder from being formatted or linted ([`cf00038`](https://github.com/dimanu-py/instant-python/commit/cf000382ba13a0bc4dbda8eb346e9cdeb4fe4541))

- Remove AST check from pre commit hook ([`b46437e`](https://github.com/dimanu-py/instant-python/commit/b46437e804a1d54f13444e92827bd15d9fb2fd57))

- Add docs-serve command to makefile ([`9430934`](https://github.com/dimanu-py/instant-python/commit/943093498f168f49cc8b2593ea17911321f2e012))

- Improve messages of make command and add build and clean commands ([`6a0e428`](https://github.com/dimanu-py/instant-python/commit/6a0e4285d3bb43f9e88dad32fd2f93732ab271c8))

- Remove commitizen config as is not longer needed ([`0ed6a8b`](https://github.com/dimanu-py/instant-python/commit/0ed6a8bd50c6ebf30b71e4734fd3e4a81123b280))

### ♻️ Refactoring

- **templates**: Improve format of github action template ([`a01b4b0`](https://github.com/dimanu-py/instant-python/commit/a01b4b0c5f57ecbc5c66995abda26157b923ecd8))

- **templates**: Improve formatting of makefile and reorganize commands ([`efa8de5`](https://github.com/dimanu-py/instant-python/commit/efa8de5c5bae2bd79c8e4a0a01ef4aa016b0e54c))

- **templates**: Convert local setup and custom hooks into python scripts ([`12af46c`](https://github.com/dimanu-py/instant-python/commit/12af46c7cf2bd437f2f81b412ceb615a7cd563e5))

- **templates**: Convert add and remove dependency scripts into python scripts instead of bash scripts ([`0d29c14`](https://github.com/dimanu-py/instant-python/commit/0d29c14a7aa7a113fe365d1e30055ead52908b29))


## v0.8.2 (2025-07-16)

### 🪲 Bug Fixes

- **render**: Create jinja environment with autoscape argument enabled to avoid potential XSS
  attacks
  ([`976d459`](https://github.com/dimanu-py/instant-python/commit/976d459538ae8eea403c65300304e6405fec46b6))

- **templates**: Format correctly if statement in application.py template
  ([`409d606`](https://github.com/dimanu-py/instant-python/commit/409d6064d97ef016c34dab57d3c9456a47e6542f))

- **templates**: Include logger and migrator in fastapi application only if they are selected too
  for DDD and standard project templates
  ([`f5a8087`](https://github.com/dimanu-py/instant-python/commit/f5a80870d0ecdd2f47419ad5e51d20131649b422))

- **templates**: Include logger and migrator in fastapi application only if they are selected as
  built in feature too in clean architecture template
  ([`191d81f`](https://github.com/dimanu-py/instant-python/commit/191d81fd8ace560f3a6359bc9cf767c73c310d50))

### ⚙️ Build System

- Update semantic release to not update major version if is zero and to allow 0 major version
  ([`34d251e`](https://github.com/dimanu-py/instant-python/commit/34d251e8a57eafa595a0c54e314238f389218dd6))

- Remove test hook in precommit config
  ([`b8d451d`](https://github.com/dimanu-py/instant-python/commit/b8d451db1a024ae41a6958dbf9513801f3b69627))

- Remove final echo from makefile commands to let output of the command itself inform the user
  ([`cd895ad`](https://github.com/dimanu-py/instant-python/commit/cd895adacfe1e470a746165380369c9c365996e8))

- Remove -e command from echo in makefile
  ([`6a624a3`](https://github.com/dimanu-py/instant-python/commit/6a624a3cacf8b96adaeba20bb635b7e43d853002))

- Exclude resources folder from being formatted or linted
  ([`cf00038`](https://github.com/dimanu-py/instant-python/commit/cf000382ba13a0bc4dbda8eb346e9cdeb4fe4541))

- Remove AST check from pre commit hook
  ([`b46437e`](https://github.com/dimanu-py/instant-python/commit/b46437e804a1d54f13444e92827bd15d9fb2fd57))

- Add docs-serve command to makefile
  ([`9430934`](https://github.com/dimanu-py/instant-python/commit/943093498f168f49cc8b2593ea17911321f2e012))

- Improve messages of make command and add build and clean commands
  ([`6a0e428`](https://github.com/dimanu-py/instant-python/commit/6a0e4285d3bb43f9e88dad32fd2f93732ab271c8))

- Remove commitizen config as is not longer needed
  ([`0ed6a8b`](https://github.com/dimanu-py/instant-python/commit/0ed6a8bd50c6ebf30b71e4734fd3e4a81123b280))

## 0.8.1 (2025-07-01)

### 🐛 Bug Fixes

- **git**: modify command to make initial commit so Windows system does not interpret it as three different commands

## 0.8.0 (2025-07-01)

### ✨ Features

- **dependency-manager**: get dependency manager installation command based on system os
- **dependency-manager**: set different commands for dependency executable based on system os
- **dependency-manager**: add os information in dependency manager to be able to modify installation depending on user os

### ♻️ Code Refactoring

- **dependency-manager**: add message for the user to notify uv should be added to the path when installing it on windows
- **dependency-manager**: notify the user when all dependencies have been installed
- **dependency-manager**: extract method to set executable path setting based on system os

## 0.7.0 (2025-06-30)

### ✨ Features

- **commands**: call project formatter in 'init' command once the file system has been generated
- **formatter**: add project formatter to be able to format included code in the project

### 🐛 Bug Fixes

- **templates**: include DomainError template when using fastapi application built in feature

## 0.6.2 (2025-06-30)

### 🐛 Bug Fixes

- **configuration**: ask built in template question only if selected template is not custom
- **templates**: use valid checkout action in test_lint.yml github action template
- **templates**: correct test path folder in makefile commands
- **templates**: rename _log_ folder that gets created when logger built in feature is selected to _logger_ to avoid git ignore its content
- **templates**: include faker library by default when template is not custom
- **templates**: include basic dependencies for makefile when is selected in built in features

### ♻️ Code Refactoring

- **templates**: separate template github action in two different workflows, one for test and one for linting and checks
- **templates**: include makefile by default if github actions built in feature has been selected to be able to reuse its commands
- **templates**: remove test execution in parallel by default in makefile template
- **templates**: remove unit and integration commands from makefile
- **templates**: remove insert_templates command from makefile template
- **configuration**: do not use Self typing to ensure compatibility with older python versions

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
