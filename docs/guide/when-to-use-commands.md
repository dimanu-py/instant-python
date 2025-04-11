# Choosing the Right Command for Your Needs

When working with `instant-python` you may ask when should you use the `project` or `folder` commands or even
when you should use the `new` or `template` subcommands. In this section we will try to clarify the differences
and needs of each command and subcommand.

## Project Command and Subcommands

The `project` command is intended not only to generate the folder structure of your project, but also to
configure a complete environment.

If you want to set a git repository, install dependencies easily at the start, have GitHub actions, makefile, or
some other implementation right away, this is the command you should use.

If you want to use some of the [default templates](https://dimanu-py.github.io/instant-python/guide/features/#default-templates) that are
available in the library or include some default implementations, you would want to use the `new` subcommand. However, if you have a specific 
folder structure you want to use, and it's not available, or you want a custom version of one of the default templates, then you should use
the `template` subcommand.

!!! warning
    Notice that with the `template` subcommand you will have a limitation of not being able to configure all the options that
    the `new` subcommand offers. You can read more about the available options in the [project command section](./creating-a-project.md).

## Folder Command and Subcommands

The `folder` command is only intended to generate the folder structure of your project. It will not configure any additional aspect
of the project.

If you just want to generate the folders and some empty files fast and be able to begin configuring your project yourself, this is the command 
you should use.

If you want to use some of the [default templates](https://dimanu-py.github.io/instant-python/guide/features/#default-templates) that are
available in the library or include some default implementations, you would want to use the `new` subcommand. However, if you have a specific
folder structure you want to use, and it's not available, or you want a custom version of one of the default templates, then you should use
the `template` subcommand.

!!! warning
    Notice that with the `template` subcommand you will have a limitation of not being able to configure all the options that
    the `new` subcommand offers. You can read more about the available options in the [project command section](./folder-structure.md).