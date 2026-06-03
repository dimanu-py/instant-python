# Releases

Instant Python is made available through both GitHub releases and PyPI. The GitHub releases also come 
with a summary of changes through a CHANGELOG file, which is automatically generated based on the commit history.

The entire process is automated through the [release](https://github.com/dimanu-py/instant-python/blob/main/.github/workflows/release.yml)
GitHub Action. 

## Versioning

Instant Python version is managed automatically through the [`python-semantic-release`](https://python-semantic-release.readthedocs.io/en/stable/index.html) 
tool, which enforces conventional commit messages. 
This tool generates the version number based on the commit history and sets the new version following [semantic versioning](https://semver.org/).

## Publishing & Release Process

In Instant Python, we work following trunk base development, trying to work always on the `main` branch. To generate a new version
and release of the project, the [release](https://github.com/dimanu-py/instant-python/blob/main/.github/workflows/release.yml) workflow
has te be triggered manually.

### Release step

When a new version is ready to be released, the release workflow is triggered manually through the GitHub Actions interface. 
The very first step of this workflow is responsible for:

- Bumping the version number using `python-semantic-versioning`.
- Generating a changelog based on the conventional commits since the last release.
- Creating a new GitHub release with the changelog associated with the new version.

### Publish step

Once the release step has been completed successfully, the workflow proceeds:

- Build the package using `uv`.
- Publish the package to PyPI.