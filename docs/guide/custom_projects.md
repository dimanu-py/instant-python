!!! tip "New in version 0.15.0"
    This level of customization using custom templates was introduced in version 0.15.0 of `instant-python`.

## Overview

Custom templates allow you to personalize your project generation by creating your own project structure and file templates. This feature is perfect if you have:

- A standardized project structure you always use
- Reusable code snippets or boilerplate you want to include in all projects
- Specific architectural patterns (like Hexagonal Architecture) you want to enforce

!!! warning "Out-of-the-box implementations not available"
    When using custom templates, the possibility of using [out-of-the-box implementations](default_features.md#out-of-the-box-implementations)
    is not available. Any [option](default_features.md#out-of-the-box-implementations) you've selected in the configuration file will be ignored.

## Create Your Custom Project

Follow these steps to create and use your first custom template:

1. Create the Template Folder Structure: create a folder to store all your custom templates (e.g., `my_templates`):

    ```
    my_templates/
    ├── main_structure.yml.j2    (required: defines your project structure)
    ├── authentication.py         (optional: custom file templates)
    ├── database.py              (optional: more templates)
    └── config.py                (optional: more templates)
    ```

2. Define Your Project Structure: create a file named `main_structure.yml.j2` in your template folder. 

    !!! warning "File *main_structure.yml.j2* is required"
        This is the **required** file that defines what your projects will look like.

3. (Optional) Add Custom File Templates: create any additional template files (like `authentication.py`, `config.py`, etc.) that 
you want to reuse.

4. Generate Your Project: when running the [init](command_init.md) command, provide the path to your custom template folder:

    ```bash
    ipy init --templates /path/to/my_templates
    # or
    ipy init -t /path/to/my_templates
    ```

## Understanding the Restrictions

Your custom template must follow specific rules to generate projects correctly. Here's what you need to know:

### File Naming & Location

- **File name:** Your main structure file **must** be named exactly `main_structure.yml.j2`
- **Location:** This file **must** be at the root of your custom templates folder
- **Format:** Must be a YAML file (`.yml` extension)

### Required Elements

- **pyproject.toml:** You **must** include a `pyproject.toml` file in your `main_structure.yml.j2` structure. This 
is required for the dependency manager to work. If missing, `instant-python` will raise an error.

### Structure Definition Format

Each element in your project structure must follow this format:

```yaml
- name: element_name           # The name of the folder or file
  type: directory              # Either "directory" or "file"
  python: True                 # [Directories only] Set to True to add __init__.py
  extension: .py               # [Files only] File extension (e.g., .py, .md, .toml)
  template: template_file.py   # [Files only] Name of template file to use
  children:                    # [Directories only] List of items inside
    - name: child_item
      type: file
      extension: .py
```

To define a new **directory** you need to reference the following fields:

- `name`: The directory name
- `type`: Must be `directory`
- `python` *(optional)*: Set to `True` to automatically create an `__init__.py` file inside this directory, making it a Python module
- `children` *(optional)*: A list of files or subdirectories to create inside

To define a new **file** you need to reference the following fields:

- `name`: The file name (without extension)
- `type`: Must be `file`
- `extension`: The file extension (e.g., `.py`, `.md`, `.toml`, `.txt`). If not provided, the file will have no extension
- `template` *(optional)*: The name of a template file in your custom templates folder to use as content. If not provided, the library 
will try to follow the [Template Resolution Logic](#template-resolution-logic) to find a template or create an empty file.

### Template Resolution Logic

When you specify a `template` field for a file:

1. **First:** `instant-python` looks in your custom templates folder
2. **Second:** If not found, it checks the built-in default templates
3. **Third:** If still not found, it creates an empty file

This means you can optionally use built-in templates without having to provide your own.

## Examples

### Hexagonal Architecture Project

Let's imagine that you want to create a new project using a custom template with Cockburn-style Hexagonal Architecture, including a 
gitignore, README and pyproject files.

!!! important
    Remember that the _pyproject.toml_ file is always required for `instant-python` to be able to set up the environment of your project.

Create a file named `main_structure.yml.j2` in your templates folder with the following content:

```yaml
- name: src
  type: directory
  python: True
  children:
    - name: adapters
      type: directory
      python: True
      children:
        - name: driven_adapters
          type: directory
          python: True
          children:
            - name: for_storing_users_with_postgres
              type: file
              extension: .py
        - name: driving
          type: directory
          python: True
          children:
            - name: user_creator_controller
              type: file
              extension: .py
    - name: ports
      type: directory
      python: True
      children:
        - name: driven
          type: directory
          python: True
          children:
            - name: for_storing_users
              type: file
              extension: .py
        - name: driving
          type: directory
          python: True
          children:
            - name: user_creator_use_case
              type: file
              extension: .py
    - name: social_network_application
      type: directory
      python: True
      children:
        - name: user
          type: file
          extension: .py
- name: .gitignore
  type: file
- name: README
  type: file
  extension: .md
- name: pyproject
  type: file
  extension: .toml
```

**What this structure does:**

- Creates a `src/` directory with three sub-packages: `adapters/`, `ports/`, and `social_network_application/`
- Adds Python modules (with `__init__.py` files) to each directory
- Creates adapter and port files following Hexagonal Architecture patterns
- Includes project configuration files (.gitignore, README.md, pyproject.toml)

### Example 2: Reusable Template Files

If you have normalized implementations that you repeat across projects, you can create template files and reference them in your structure.

**Step 1:** Create a file named `authentication.py` in your templates folder with your standard authentication logic:

```python
# authentication.py
def authenticate_user(username: str, password: str) -> bool:
    # Standard authentication logic
    return username == "admin" and password == "secret"
```

**Step 2:** Reference this template in your `main_structure.yml.j2`:

```yaml
- name: src
  type: directory
  python: True
  children:
    - name: auth
      type: file
      extension: .py
      template: authentication.py
    # ... rest of the structure
```

**Result:** When you generate a new project using this custom template, the `authentication.py` file will be included in the `src` 
directory with your predefined logic. This ensures consistency across all your projects and saves time on repetitive tasks!
