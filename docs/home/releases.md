# Releases

Instant Python is made available through both GitHub releases and PyPI. The GitHub releases also come with a summary of changes
through a CHANGELOG file, which is automatically generated based on the commit history.

The entire process is automated through the [release](https://github.com/dimanu-py/instant-python/blob/main/.github/workflows/release.yml)
and [publish](https://github.com/dimanu-py/instant-python/blob/main/.github/workflows/publish.yml) GitHub Actions. 

## Versioning

Instant Python version is managed automatically through the [`commitizen`](https://github.com/commitizen-tools/commitizen) tool, which
enforces conventional commit messages. This tool generates the version number based on the commit history and sets the new version
following [semantic versioning](https://semver.org/).

## Publishing & Release Process

In Instant Python, we work following trunk base development, trying to work always on the `main` branch. To generate a new version
and release of the project, the [release](https://github.com/dimanu-py/instant-python/blob/main/.github/workflows/release.yml) workflow
has te be triggered manually.

When this workflow is finished, it will trigger the [_publish_](https://github.com/dimanu-py/instant-python/blob/main/.github/workflows/publish.yml)
pipeline, which is responsible for publishing the new version to PyPI.

### Release step

When a new version is ready to be released, the release step is triggered manually through the GitHub Actions interface. This step is responsible for:

- Bumping the version number using `commitizen`.
- Generating a changelog based on the conventional commits since the last release.
- Creating a new GitHub release with the changelog associated with the new version.

### Publish step

When a new version is released, the _publish_ step is triggered automatically. This step is responsible for:

- Building the package using `uv`.
- Publishing the package to PyPI.