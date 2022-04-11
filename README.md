# template-python-types

###(For the instructions below, the original packagename will be assumed to be `foo-bar`. Adapt this to your use case)

Step-by-step instructions on using this template:

- Create a new repository using this template. Name it `types-foo-bar`. 
  - Set up anything that may not carry over from the template (branch permissions, enabling the renovate bot, etc)
  - You can use [this](https://app.gitbook.com/o/kE0i1aiE1u2yiaP5k3xM/s/B8iaOECpmPzLCKc8nF0p/development/github-repository-init-checklist) for a full list (although some steps do not apply, like the `next` branch or the `unit-tests` action)
  - Set the repository to `public` access. Take a second to think through the implications of this. Extra care will be needed to avoid leaking any information
- Replace all instances of `changeme` strings as follows:
    - Replace these:
        - `changeme-package-name` => `foo-bar` (name of the original package)
        - `changeme-types-package-name` => `types-foo-bar` (name of your stubs package; **must** start with `types-`)
        - `changeme-package-name-stubs` => `foo-bar-stubs` (name of the stubs root folder; **must** end with `-stubs`)
    - In the following files:
        - `README.md`
        - `.releaserc`
        - `.pre-commit-config.yaml`
        - `setup.py`
- Rename the folder `changeme-package-name-stubs` to `foo-bar-stubs`. This will be the root folder for all the stub files
- In `foo-bar-stubs/METADATA.toml`, change the version from `"X.Y.*"` to the version of the original package for which your stubs are meant for (usually the latest one)
- Update the package's information in `setup.py`
  - Add/Update the [classifiers](https://pypi.org/classifiers/) to help people find the package
  - Add some keywords (like the original package name, related frameworks, etc) to help people find the package
  - Change the versions in `python_requires` if necessary. Make sure it matches the versions listed in the classifiers
- Add the dependencies:
  - Add your dependencies to the `Pipfile` with an exact version
  - Run `$ pipenv install -d` to update the `Pipfile.lock`
  - Run `$ pipenv shell` to switch to a shell within the virtual environment
  - Run `$ pipenv-setup sync --pipfile --dev` to sync the dependencies to the `setup.py`
- Install the pre-commit hook (see below, in the `Developing` section)
- Add your stubs
  - [Optional] Mark the `foo-bar-stubs` directory as `Sources Root` and the `.mypy_cache` directory as `Excluded`
  - The stubs can be generated with [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html#stubgen) with the command `$ stubgen -p foo-bar`, and will only need to be filled in
  - The files need to use the root of the `foo-bar-stubs` as their root, and only have sub-folders as necessary to match the structure of the original package
- Test your stubs
  - If you add the stubs root directory (`foo-bar-stubs`) to `mypy`'s path, it should pick up and use your stubs automatically. You can tell this is the case when it gives off a warning about the `type: ignore[import]` comment for that specific package being unused (doesn't complain about the package not having stubs available)
- Uncomment the action in `.github/workflows/on-push-to-main.yml` to allow the package to be released
- Remove these instructions from `README.md` (they will still be available in the template repo for the next steps)
- A search through the whole project (CTRL + Shift + F in PyCharm) should find no results for `changeme`
- Release the package
  - Merge your changes into the `main` branch (preferably via PR)
  - Wait for the GH Action to run, and the package to be released
  - The package should be available at https://pypi.org/project/types-foo-bar/
  - Download your package and test it again as a final check

# changeme-types-package-name

This is a package containing type annotations
for [changeme-package-name](https://pypi.org/project/changeme-package-name/).

### Installing:

Simply run the following in the environment in which you want to install this package:

```shell
# install changeme-types-package-name
$ python -m pip install changeme-types-package-name
```

or add it to your requirements file.

### Developing

This is a partial stub package, only covering a part of the functions and objects available in `changeme-package-name`.
Contributions (both in adding stubs for more functions, or keeping up to date with `changeme-package-name` itself) are
welcome.

All the formatting is done using [pre-commit](https://pre-commit.com/). To use this, run the following:

```shell
# install pre-commit
$ python -m pip install pre-commit

# Set up the hooks (so pre-commit automatically runs when you do a commit)
$ cd root/directory/of/the/pulled/repository
$ pre-commit install

# This will run automatically whenever a commit is created
# To run it manually, use:
$ pre-commit run --all-files
```
