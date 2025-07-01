# Getting Started

To get started with `instant-python` we would cover some of the basic topics that will allow you
to quickly begin using the library.

- [Installing `instant-python`](#installation)
- [Overview of available commands](#features-overview)
- [Next steps](#next-steps)

If you want to go directly to the guides and learn all the possibilities that the library offers, you can
check the [Commands](../guide/command_config.md) section.

## Installation

To ensure a clean and isolated environment, we recommend installing `instant-python` using a virtual environment. At your
own risk, you can install it at your system Python installation, but this is not recommended.
Below are the preferred installation methods.

### Using `pipx`

The recommended way to install `instant-python` is using `pipx`. `pipx` installs Python applications in isolated environments, ensuring that
they do not interfere with other Python applications.

```bash
pipx install instant-python
```

If you do not have `pipx` installed, you can install it using `pip`.

```bash
pip install --user pipx
```

### Using `pyenv`

If you already manage your Python versions using a tool like Pyenv, you can install `instant-python` using `pip` with
pyenv's global Python version.

```bash
pip install instant-python
```

A guide to install and configure pyenv can be found [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

## Features Overview

Once you have [installed `instant-python`](#installation), you can check that is available by running:

```bash
ipy --help
```

This will display the help message where you could see the available command and options.

### Create the configuration file

With the new version, `instant-python` delegates all its data to a configuration file. You can create this file manually and fill
it with the allowed parameters, or you can use the `config` command to fill it by an interactive wizard.

- `ipy config`: Creates an _ipy.yml_ configuration file in the current directory.

### Create a project

Generate a new project using the `init` command. This command will create a new folder and place all your project files inside it.

- `ipy init`: Creates a new project in the current directory using the default configuration file _ipy.yml_.

If a different file is used or is placed in a different location, you can specify the path to it with the `--config` or `-c` option.

## Next steps

Now that you have a basic understanding of how to use `instant-python` you can advance to the [commands](../guide/command_config.md) 
section to learn more about `instant-python` commands and how to use them in more detail to create your Python projects.