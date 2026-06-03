With a valid [configuration file], use the `init` command to turn
that configuration file into a ready to use project.

## Overview

The command performs the following steps:

1. Creates the project folder structure based on the selected template or your custom template.
2. **Only when the template is not custom**, writes boilerplate code for any [Out-of-the-box Implementations] enabled in the configuration.
3. Sets up the chosen dependency manager and installs dependencies under the selected Python version.
4. Initializes a git repository if requested and configures your username and email.
5. Moves the configuration file inside the new project folder for future reference.

## Usage

To create a new Python project using the `instant-python` tool, run the following command in your terminal:

```bash
ipy init
```

The help message of the command provides more information about its usage and available options:

```bash
ipy init --help
```

| Option         | Short | Description | Example |
|----------------|-------|-------------|---------|
| `--config`     | `-c` | Path to your configuration file | `ipy init -c /path/to/config.yml` |
| `--templates`  | `-t` | Path to your custom templates folder | `ipy init -t /path/to/templates` |

### Using the Config Path Option

By default `instant-python` will look for **ipy.yml** in the current directory. If you have created your configuration file manually with a
different name, or you have it stored in a different location, you can specify its path using the `--config` or `-c` flag:

```bash
ipy init -c /path/to/config.yml
```

### Using Custom Templates

`instant-python` comes with a set of [Default Templates] that you can use to create your 
projects out of the box.
These templates cover a wide range of common project structures and file templates that you may need, but if you want to create
a project with a custom structure or specific file templates, you can do so by providing your own template folder through the
`--templates` or `-t` flags.

!!! warning "Out-of-the-box implementations not available"
    When using custom templates, the possibility of using the [Out-of-the-box Implementations]
    is not available.

```bash
ipy init -t /path/to/templates/folder
```

!!! info "More about custom projects"
    Project customization has acquired its own dedicated section in the documentation as now it allows the user
    to create fully custom projects using their own project structure and file templates.
    For more information, visit the [Custom Projects] guide.


[Out-of-the-box Implementations]: default_features.md#out-of-the-box-implementations
[Default Templates]: default_features.md#default-project-structures
[Custom Projects]: custom_projects.md
[configuration file]: command_config.md#configuration-file-structure-and-restrictions