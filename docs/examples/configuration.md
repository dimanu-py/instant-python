# Configurations

## Without initializing a git repository

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: 0.1.0
  author: John Doe
  license: MIT
  python_version: 3.13
  dependency_manager: uv
git:
  initialize: false
dependencies:
template:
  name: standard
  built_in_features:
```

## Initializing a git repository

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: 0.1.0
  author: John Doe
  license: MIT
  python_version: 3.13
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: standard
  built_in_features:
```

## Domain Driven Design without specifying bounded context

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: 0.1.0
  author: John Doe
  license: MIT
  python_version: 3.13
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: domain_driven_design
  specify_bounded_context: false
  built_in_features:
```

## Domain Driven Design specifying bounded context

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: 0.1.0
  author: John Doe
  license: MIT
  python_version: 3.13
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: domain_driven_design
  specify_bounded_context: true
  bounded_context: backoffice
  aggregate_name: user
  built_in_features:
```

## Selecting built-in features

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: 0.1.0
  author: John Doe
  license: MIT
  python_version: 3.13
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
template:
  name: clean_architecture
  built_in_features:
    - value_objects
    - github_actions
    - makefile
```

## Installing dependencies

```yaml
general:
  slug: python-project
  source_name: src
  description: Python Project Description
  version: 0.1.0
  author: John Doe
  license: MIT
  python_version: 3.13
  dependency_manager: uv
git:
  initialize: true
  username: johndoe
  email: johndoe@gmail.com
dependencies:
  - name: ty
    version: latest
    is_dev: true
    group: lint
  - name: pytest
    version: latest
    is_dev: true
    group: test
  - name: fastapi
    version: latest
template:
  name: standard
  built_in_features:
    - value_objects
    - github_actions
    - makefile
```