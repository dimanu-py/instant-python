![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=for-the-badge&logo=python) ![License](https://img.shields.io/github/license/dimanu-py/instant-python?style=for-the-badge)

# Welcome to Instant Python!

Welcome to the [**Instant Python**](https://github.com/dimanu-py/instant-python-ddd) library, a powerful Python library to quickly
scaffold a modern Python project with best practices and a clean architecture. This template includes ready-to-use scripts, project
structure options, and automated setup commands to help you kickstart your Python projects.

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  /* give the container a fixed size */
  .chart-container {
    width: 600px;
    height: 350px;
    margin: auto;
  }
  /* make sure the canvas fills that container */
  .chart-container canvas {
    width: 100%  !important;
    height: 100% !important;
  }
</style>

<div class="chart-container">
  <canvas id="downloads-chart"></canvas>
</div><script>
  const raw =  {{ download_data("instant-python") | tojson }};
  // Filter out the 'with_mirrors' series—keep only real-user downloads:
  const daily = raw.filter(d => d.category === 'without_mirrors');
  const labels = daily.map(d => d.date);
  const counts = daily.map(d => d.downloads);

  // Render the chart:
  new Chart(
    document.getElementById('downloads-chart').getContext('2d'),
    {
      type: 'bar',
      data: {
        labels,
        datasets: [{
          label: 'Daily downloads',
          data: counts,
          fill: false
        }]
      },
      options: {
        scales: {
          x: { type: 'category' , ticks: { display: false } },
          y: { beginAtZero: true }
        }
      }
    }
  );
</script>


## Installation

Install `instant-python` from PyPI:

```bash
# With pipx
pipx install instant-python
```

```bash
# With pip in pyenv
pip install instant-python
```

## Documentation Structure

- [Getting Started](./getting-started/index.md)
    - [Installation](./getting-started/installation.md)
    - [First Steps](./getting-started/first-steps.md)
    - [Features Overview](./getting-started/features_overview.md)
- [Guide](./guide/index.md)
    - [Choosing between templates](./guide/when-to-use-commands.md)
    - [Creating a new project](./guide/creating-a-project.md)
    - [Creating a folder structure](./guide/folder-structure.md)
    - [Features](./guide/features.md)
    - [Custom Templates](./guide/custom-templates.md)
- [Contributing](./contributing.md)

## Features

With `instant-python` there is a lot of features you can customize easily so you can start coding on your project
as soon as possible. An overview of the features is given below, but you can find a more detailed explanation in the
[documentation](https://dimanu-py.github.io/instant-python/guide/features/).

- Project slug: Configure the name of the main folder of your project.
- Source name: Configure the name of the source code folder of your project.
- Description: Include a description about your project.
- Version: Set the initial version of your project.
- Author: Set the author of the project.
- License: Choose between _MIT_, _Apache_ or _GPL_ licenses to set your project.
- Python version: Select the Python version you want to use for your project between versions 3.13 to 3.10.
- Dependency manager: Choose between _uv_ or _pdm_ dependency managers.
- Git: configure your project as a git repository automatically.
- Default templates: select your project template between Domain Driven Design, Clean Architecture or Standard Project to
  automatically generate your project folders and files.
- Out of the box implementations: include some boilerplate and implementations code that will help you to start your project faster.
  Some of the most popular implementations are value objects, domain error modelling, makefile and Async SQL Alchemy.
- Dependencies: install dependencies automatically in your project.