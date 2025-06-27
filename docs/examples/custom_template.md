# Custom Template

Let's imagine that you want to create a new project using a custom template with Cockburn-style Hexagonal Architecture,
including a gitignore, README and mypy configuration files.
You can create a yaml file with the following content:

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
- name: mypy
  type: file
  extension: .ini
```