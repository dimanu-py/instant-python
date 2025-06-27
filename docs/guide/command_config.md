# Config

`instant-python` relies on a YAML file to know how your project should be generated. The `config` command walks 
you through an interactive wizard and produces this file for you.

```bash
ipy config
```

Running it will create an **ipy.yml** file in the current directory containing all your answers. 
Later this file can be used with the [`init`](command_init.md) command.

## File format

The configuration file contains four top level keys:

- **general** – project information
- **dependencies** – packages that must be installed
- **git** – repository settings
- **template** – project structure and built‑in features

!!! warning
    These keys are all required, if any of them is missing, the command will raise an error.

## Restrictions

The configuration file has some restrictions that vary depending on the section.

### General

- All the fields in the `general` section are required.
- The `slug` of the project cannot contain spaces or special characters, it must fulfill toml specifications.
- The `license` field must one of the following values: `MIT`, `Apache` or `GPL`. These are the more popular licenses, but you can use any
other license changing the `LICENSE` file later.
- The `python_version` must be one of the following values: `3.10`, `3.11`, `3.12` or `3.13`. 
  This is the version that will be used to create the virtual environment and install the dependencies.
- The `dependency_manager` must be either `uv` of `pdm`. These are the two supported dependency managers that we
found more useful. Future versions may support more dependency managers.

### Dependencies

- If you don't want to install any dependencies, you can leave the `dependencies` section empty. But it's important
to keep the section in the file.
- If a dependency is specified, the `name` and `version` fields are required.
- Only dependencies marked as development dependencies can be assigned to a `group`. Otherwise,
the command will raise an error.

### Git

- The `initialize` field is required, and must be either `true` or `false`.
- If `initialize` is set to `true`, the `username` and `email` fields must be provided.

### Template

- The `name` field is required, and must be one of the available templates: `standard`, `domain_driven_design`, `clean_architecture` or `custom`.
- When the template is `domain_driven_design` is it possible to specify the name for a `bounded_context` and its `aggregate_root`. If any
of these fields is specified for other templates, the command will raise an error.
- The `built_in_features` field is optional, but if specified, it must be a list of features that are available in the template.
The list of available features can be found in the [out-of-the-box section](command_init.md#out-of-the-box-implementations).