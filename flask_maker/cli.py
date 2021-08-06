import os
import click
from .contents import *
from slugify import slugify
from .context import make_dir, open_dir
from .helpers import create_file

TEMPLATES_DIR = "templates"
STATIC_DIR = "static"


@click.group(chain=True)
def cli():
    """Flask-maker"""


@cli.command("startproject")
@click.option("--name", "-n", help="Project name", default="")
def start_project(name):
    """Creates a flask project"""
    if not name:
        print("Project Name : ", end="")
        name = input()

    folder_name = slugify(name)
    app_name = folder_name.replace("-", "_")

    with make_dir(folder_name, back=False, empty=True) as _:
        create_file("app.py", APP_TEXT, {"{app_name}": app_name})

        with make_dir(app_name, back=False) as _:
            create_file("__init__.py", INIT_TEXT, {"{app_name}": app_name})
            create_file("config.py", CONFIG_TEXT, {"{secret}": app_name})

            with make_dir(TEMPLATES_DIR, back=True) as _:
                create_file("index.html", INDEX_TEXT)

            with make_dir(STATIC_DIR, back=True) as _:
                create_file("style.css", STYLE_TEXT)

    print(
        f"Flask project created. Use `cd {folder_name}` and open with your favourite code editor."
    )


@cli.command("startapp")
@click.option("--name", "-n", help="App/Blurprint name", default="")
def start_app(name):
    """Creates a app inside a flask app"""
    if not name:
        print("App Name : ", end="")
        name = input()

    app_name = slugify(name).replace("-", "_")
    folders = [f.path for f in os.scandir(os.getcwd()) if f.is_dir()]

    project_dir = ""
    is_project = False

    for folder in folders:
        files = os.listdir(folder)
        if "config.py" in files and "__init__.py" in files:
            is_project = True
            project_dir = folder
            break

    if not is_project:
        return print(
            "No flask project found on this directory. Can't create app here. Navigate to a project directory or create an app."
        )

    os.chdir(project_dir)

    with make_dir("apps", back=True, empty=False) as _:
        with make_dir(app_name, back=True) as _:
            create_file("__init__.py", BLP_TEXT, {"{app_name}": app_name})
            create_file("views.py", VIEWS_TEXT, {"{app_name}": app_name})
            create_file("errors.py", ERRORS_TEXT, {"{app_name}": app_name})

    with open_dir(STATIC_DIR, back=True) as _:
        with make_dir(app_name, back=True) as _:
            create_file("style.css", BLP_STYLE)

    with open_dir(TEMPLATES_DIR, back=True) as _:
        with make_dir(app_name, back=True) as _:
            create_file("index.html", BLP_INDEX, {"{app_name}": app_name})

    print(f"App {name} created successfully. Will be accessible on '/{name}' route")
