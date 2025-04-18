# Custom Templates

Both commands available with `instant-python` allow the option of providing a custom template to generate
the project folder structure instead of using the default templates provided by the library.

This custom template must follow a specific structure and syntax to be able to generate the project correctly.

- You must use a yaml file to define the folder structure.
- The first level of the yaml will always be `root`
- The rest of the hierarchy will be declared as a list of elements with the following structure:
  - `name`: The name of the folder or file to create.
  - `type`: The type of the element, which can be `directory` or `file`.
  - `python`: **Only for directories**. Set its value to True if the directory is a python module to include the `__init__.py` file, otherwise
     ignore this field.
  - `extension`: **Only for files**. The extension of the file to create. If the file do not have an extension, you can ignore
     this field.
  - `children`: A list of elements that will be created inside the folder. This can be either another directory or files.

The available templates can be found in the [features](./features.md) section. The library
offers a Domain Driven Design, Clean Architecture and Standard templates.

## Examples

Let's imagine that you want to create a new project using a custom template with Cockburn-style Hexagonal Architecture,
including a gitignore, README and mypy configuration files. 
You can create a yaml file with the following content:

```yaml
root:
  - name: src
    type: directory
    python: True
    children:
      - name: driven_adapters
        type: directory
        python: True
        children:
          - name: adapter_for_paying_spy
            type: file
            extension: .py
          - name: adapter_for_obtaining_grates_stub
            type: file
            extension: .py
      - name: driving_adapters
        type: directory
        python: True
        children:
          - name: adapter_for_checking_cars_test
            type: file
            extension: .py
      - name: tax_calculator_app
        type: directory
        python: True
        children:
          - name: driven_ports
            type: directory
            python: True
            children:
              - name: for_paying
                type: file
                extension: .py
          - name: driving_ports
            type: directory
            python: True
            children:
              - name: for_checking_cars
                type: file
                extension: .py
          - name: tax_calculator
            type: directory
            python: True
  - name: .gitignore
    type: file
  - name: README
    type: file
    extension: .md
  - name: mypy
    type: file
    extension: .ini
```