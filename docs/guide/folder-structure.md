# Creating the folder structure

## Commands overview

The other command that can be used with `instant-pyton` is the `folder` command. This command
will allow you to create all the folders and files you want for your project.

This command has two subcommands that you can use to create a new project:

- `ipy folder new`: will generate a question wizard that will guide you through all steps to create the folders of 
your project.
- [COMING SOON] `ipy folder template <template>`: will allow you to use a custom template where you specify the folder structure
you want to have.

## New

The `new` subcommand will use the default templates that come with the library and that the user can select
to create the folder structure of the project.

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
- Default templates
- Out of the box implementations (value objects, exceptions, GitHub actions, makefile, logger, FastAPI, SQL Alchemy, Alembic, event bus)

[//]: # (## Template)

[//]: # ()
[//]: # (The `template` subcommand will only create the folder structure of the project using a custom template that the user)

[//]: # (provides.)

[//]: # ()
[//]: # (!!! important)

[//]: # (    With this option the user will only be able to create directories. No additional configuration will be made and)

[//]: # (    no additional files will be created.)

[//]: # ()
[//]: # ()
[//]: # (When using this subcommand you would be able to configure the following out of the box implementations that you)

[//]: # (can check in the [features]&#40;features.md&#41; section:)

[//]: # ()
[//]: # (- Project slug)
