To ensure a clean and isolated environment, we recommend installing `instant-python` using a virtual environment. At your
own risk, you can install it at your system Python installation, but this is not recommended.
Below are the preferred installation methods.

!!! note "Supported Python Versions"
    Instant Python tries to support the latest Python versions, we officially support from Python 3.10 to 3.13.
    Older versions of Python may work, but they are not guaranteed to be compatible.

## Installation Methods

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

## Next steps

Now that you have installed `instant-python` you can advance to the [first steps](first_steps.md)
section to learn the basic features of `instant-python` and create your first project.