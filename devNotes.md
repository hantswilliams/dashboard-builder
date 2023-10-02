# Local Dev Notes

## Updating 
To publish a new version, and also update the existing documentation can use the following:
```bash
./build.bash
```
This will do a couple things:
- update the version number for the build in the `pyproject.toml` and the version number in the associated mkdocs documentation inside the `docs/index.md` 
- add, commit, and publish these changes to github
- vercel is setup to automatically re-deploy with git push, so the official documentation will then also be updated

## Ruff 
For running linting tests, can run ruff locally in the root directory of the folder: 
```bash
ruff check .
```

## Pytest 

Pytest is installed as a local dev. Current test are found within `/tests`. Need to continue building out, but for now there are a few. 

To run the pytests, inside the root directory can run the following:
```bash
poetry run pytest
```

## Documentation

Note for below - should just put this inside of the `build.bash` script so it automatically deploys and creates an updated version of the documentation so everything stays in sync.

Using mkdocs for autodocumentation of key components and features. Mostly utilized based off of [this tutorial](https://realpython.com/python-project-documentation-with-mkdocs/#step-4-prepare-your-documentation-with-mkdocs). Can run the demo instance with:
```bash
poetry run mkdocs serve
```

To build:
```bash
poetry run mkdocs build
```

Then to deploy the build to github:
```bash
poetry run mkdocs gh-deploy
```

Quick notes for where to find additional help for specific parts of the documentation process: 
    - [Sharing Code](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)
    - [Snippets of Code](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/)

## Poetry and Deployment 

I'm new to poetry so putting this information here so I dont forgot. Using 
poetry for managing dependencies and deploying. On my local machine 
also using pyenv for python version controll manager. So start up the remote 
environment, can do the following below from [this blog post](https://www.freecodecamp.org/news/how-to-build-and-publish-python-packages-with-poetry/):

1. Set the python version - currently 3.10 for this project: `pyenv global 3.10.0`

2. Tell poetry to use that: `poetry env use $(pyenv which python)`. 

3. This should then pick up the correct version of python. You can then confirm 
this by doing `poetry env info`, and you should then see something like 
below:

```bash
Virtualenv
Python:         3.10.0
Implementation: CPython
Path:           
/Users/hantswilliams/Library/Caches/pypoetry/virtualenvs/dashboard-builder-HW6rzWnP-py3.10
Executable:     
/Users/hantswilliams/Library/Caches/pypoetry/virtualenvs/dashboard-builder-HW6rzWnP-py3.10/bin/python
Valid:          True

System
Platform:   darwin
OS:         posix
Python:     3.10.0
Path:       /Users/hantswilliams/.pyenv/versions/3.10.0
Executable: /Users/hantswilliams/.pyenv/versions/3.10.0/bin/python3.10
``` 

4. To get a list of the poetry env created, can use: `poetry env list` 

5. Then can add things, e.g., `poetry add requests` 

Once done there, can then generate the requirements.txt file with:

```bash
poetry export --output requirements.txt
```

For publishing: 
1. Package the updates: 

```bash 
poetry build

``` 
2. Once it has finished packing, can run below to get the latest version on pypi: 

```bash
poetry publish
``` 

3. For subsequent builds, need to update the version number first in the .toml file, otherwise the build will fail. Once .toml version is updated, can even do the build/publish in the same command like so:

```bash
poetry published --build
```
