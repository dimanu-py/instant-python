# Custom Templates

Let's imagine that you want to create a new project using a custom template with Cockburn-style Hexagonal Architecture,
including a gitignore, README and pyproject files.

!!! important
    Remember that the _pyproject.toml_ file is always required for `instant-python` to be able to set up the environment of your project.

```yaml
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
- name: pyproject
  type: file
  extension: .toml
```

If you have normalized some implementation that you always repeat in your projects, you can create a file in your custom templates folder
and let `instant-python` use it when generating the project structure. Let's imagine that you always want to include an authentication
logic in your projects, and you have a standard way of implementing it. 
You can create a file named `authentication.py` in your custom templates folder and place there your own implementation:

```python
# authentication.py
def authenticate_user(username: str, password: str) -> bool:
    # Standard authentication logic
    return username == "admin" and password == "secret"
```

Then, in your *main_structure.yml.j2* file, you can reference this file so that it gets included in every new project you create:

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

When you generate a new project using this custom template, the `authentication.py` file will be included in the `src` directory with 
your predefined logic. This way, you can ensure consistency across your projects and save time on repetitive tasks!
