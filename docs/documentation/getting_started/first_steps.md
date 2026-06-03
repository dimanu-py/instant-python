Once you have [installed `instant-python`](installation.md), you can check that is available by running:

```bash
ipy --help
```

This will display the help message where you can see the available command and options.

!!! note "Prerequisites"
    - `instant-python` is [installed](installation.md) and available in your terminal
    - You have a terminal/command prompt open in the directory where you want to create your project

## Your first project

To create your first Python project using `instant-python`, you need to follow two simple steps:

- First run `ipy config` to create the configuration file through an interactive wizard.
- Then run `ipy init` to create your project.

!!! tip "A configuration file is required"
    To be able to create a project, `instant-python` needs a configuration file. You can create the file manually, however
    we recommend using the `ipy config` command to create it through an interactive wizard and avoid mistakes.

### Generate the configuration file

`instant-python` delegates all its data to a configuration file. You can create this file manually and fill
it with the allowed parameters, or you can use the `config` command to fill it by an interactive wizard.

- `ipy config`: Creates an _ipy.yml_ configuration file in the current directory.

The wizard will ask you a series of questions about your project. A full description and explanation
of all these options can be found in the [Command Config] section. Here is a small summary
of the main options you will be asked:

| Field                       | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| Slug                        | The name of your project folder and package.                               |
| Source Directory            | The folder where your source code will be located.                         |
| Description                 | A short description of your project.                                       |
| Version                     | The initial version of your project.                                       |
| Author                      | The author of the project.                                                 |
| License                     | The license of the project.                                                |
| Python Version              | The Python version to use in the project.                                  |
| Project Environment Manager | The project manager to use (choose between `uv` or `pdm`).                 |
| Default Template | Choose a default template to use as a base for your project structure.     |
| Built in Features | Choose additional ready to use implementations to include in your project. |
| Git Initialization          | Whether to initialize a Git repository in the project folder.              |
| Dependencies                | Define initial dependencies to install in the project.                     |


### Create a project

With a valid configuration file, you can generate a new project using the `init` command. 
This command will create a new folder and place all your project files inside of it.

- `ipy init`: Creates a new project in the current directory using the default configuration file _ipy.yml_.

`instant-python` also allows you to create full customize projects using your own project structure and your own
templates for common implementations if you have specific needs. To see a detailed guide on how to 
create custom projects go to the [Customizing Projects] section.

## Next steps

Now that you have a basic understanding of how to use `instant-python` you can advance to the [Advanced Usage and Customization]
section to learn more about the features that `instant-python` provides and how to create custom projects.

### Recommended Learning Path

- **[Config Command]** - Understand all configuration options
- **[Default Features]** - Explore the built-in project templates and implementations
- **[Init Command]** - Learn advanced options for project initialization
- **[Custom Projects]** - (Optional) Learn how to create your own project templates

### Common Questions

**Can I add more dependencies after creating my project?**  
→ Yes! You can use your project manager (`uv` or `pdm`) to add dependencies after creation.

**How do I use a different project structure?**  
→ See the [Custom Projects] guide to create your own project structure.

[Command Config]: ../guide/command_config.md#configuration-file-structure-and-restrictions
[Customizing Projects]: ../guide/custom_projects.md
[Advanced Usage and Customization]: ../guide/index.md
[Config Command]: ../guide/command_config.md
[Default Features]: ../guide/default_features.md
[Init Command]: ../guide/command_init.md
[Custom Projects]: ../guide/custom_projects.md
