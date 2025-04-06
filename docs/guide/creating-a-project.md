# Creating a new project

## Commands overview

One of the main commands you can use with `instant-pyton` is the `project` command. This command
will allow you to create and configure a complete new project from scratch.

!!! note 
    The `project` command it won't only create the folder structure of your project, but it will also
    allow you to generate a bunch of boilerplate, install the Python version you want to use, install
    dependencies and even configure a git repository for your project.


This command has two subcommands that you can use to create a new project:

- `ipy project new`: will generate a question wizard that will guide you through all the questions and
available options you can configure to create your project.
- [COMING SOON] `ipy project template <template>`: will generate a question wizard like the previous command, but
you could use a custom template to create the folder structure of your project.

## New

The `new` subcommand will use a question wizard that will guide you through all the questions and available
options you can configure to create your project.

When using this subcommand you would be able to configure the following out of the box implementations that you
can check in the [features](features.md) section:

- Project slug
- Source name
- Description
- Version
- Author
- License
- Python version
- Dependency manager
- Git
- Default templates
- Out of the box implementations (value objects, exceptions, GitHub actions, makefile, logger, FastAPI, SQL Alchemy, Alembic, event bus)
- Install dependencies

[//]: # (## Template)

[//]: # ()
[//]: # (The `template` subcommand will delegate all the logic of creating the folder structure to the custom file that the user)

[//]: # (provides.)

[//]: # ()
[//]: # (When using this subcommand you would be able to configure the following out of the box implementations that you)

[//]: # (can check in the [features]&#40;features.md&#41; section:)

[//]: # ()
[//]: # (- Project slug)

[//]: # (- Description)

[//]: # (- Version)

[//]: # (- Author)

[//]: # (- License)

[//]: # (- Python version)

[//]: # (- Dependency manager)

[//]: # (- Git)

[//]: # (- Install dependencies)
