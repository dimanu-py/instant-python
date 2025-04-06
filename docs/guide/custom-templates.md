# Custom Templates [COMING SOON]

Both commands available with `instant-python` allow the option of providing a custom template to generate
the project folder structure instead of using the default templates provided by the library.

This custom template must follow a specific structure and syntax to be able to generate the project correctly.

- You must use a yaml file to define the folder structure.
- The first level of the yaml will always be `root`
- The rest of the hierarchy will be declared as a list of elements with the following structure:
  - `name`: The name of the folder or file to create.
  - `type`: The type of the element, right now only `directory` is available for custom templates.
  - `python`: If the directory is a python module to include the `__init__.py` file.
  - `children`: A list of elements that will be created inside the folder.

The available templates can be found in the [features](../getting-started/features.md) section. The library
offers a Domain Driven Design, Clean Architecture and Standard templates.
Let's imagine that you want to create a new project using a custom template with Hexagonal Architecture. 
You can create a yaml file with the following content:

```yaml
root:
  - name: src
    type: directory
    python: true
    children:
      - name: domain
        type: directory
        python: true
      - name: application
        type: directory
        python: true
      - name: ports
        type: directory
        python: true
      - name: adapters
        type: directory
        python: true
  - name: test
    type: directory
    python: true
    children:
      - name: domain
        type: directory
        python: true
      - name: application
        type: directory
        python: true
      - name: ports
        type: directory
        python: true
      - name: adapters
        type: directory
        python: true
```