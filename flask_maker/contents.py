APP_TEXT = """
import click
from {app_name} import app

@click.group()
def cli():
    \"\"\"{app_name}'s cli\"\"\"

@cli.command(name="start")
@click.option("--debug", is_flag=True, help="Run app in debug mode.")
@click.option("--port", default=5000, help="Port to start the webserver.")
def _start(debug, port):
    print("[+] Routes")
    for rule in app.url_map.iter_rules():
        if 'static/<path:filename>' not in str(rule):
            print(f'    http://localhost:{port}{rule}')
    print('\\n')

    app.run(debug=debug, port=port)

if __name__ == "__main__":
    cli()
"""

URLS_TEXT = """
from .views import index

url_patterns = [
    ['/', index],
]
"""

INIT_TEXT = """
import os
import importlib
from flask import Flask
from .config import config
from .urls import url_patterns

app = Flask(__name__)
app.config.from_object(config['development']) # Change it to production for production use

_apps = {}
apps_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'apps')

if os.path.exists(apps_folder):
    for path in os.listdir(apps_folder):
        module_path = os.path.join(apps_folder, path)
        if os.path.isdir(module_path) and not path.startswith('__'):
            module = importlib.import_module(f'.{path}', package=f"{app.name}.apps")
            try:
                _apps[path] = getattr(module, path)
            except:
                print(f"[-] Filed to import blueprint from 'apps/{path}' directory.")
                

for _key, _module in _apps.items():
    try:
        app.register_blueprint(_module)
    except Exception as e:
        print(f'[-] Failed to register blueprint {_key}. Reason :', e)

for pattern in url_patterns:
    app.add_url_rule(rule=pattern[0], view_func=pattern[1])
"""

CONFIG_TEXT = """
class Config:
    SECRET_KEY = "{secret}"

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
"""

INDEX_TEXT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="https://flask.palletsprojects.com/en/2.0.x/_static/flask-icon.png" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>Flask</title>
</head>
<body>
    <div class="header container">
        <div class="title">
            Flask
        </div>

        <a href="https://flask.palletsprojects.com/en/2.0.x/" target="_blank">Documentation</a>
    </div>


    <div class="content container">
        <img src="https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png" alt="Flask">
        <p>Web development, One drop at a time.</p>
    </div>
</body>
</html>
"""

STYLE_TEXT = """
.container {
    max-width: 960px;
    margin: 0 auto;
    padding-left: 20px;
    padding-right: 20px;
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 60px;
}

.header .title {
    font-size: 30px;
    color: black;
}

.header a {
    color: #008dff;
    text-decoration: none;
    font-size: 20px;
}

.content {
    text-align: center;
    width: 100%;
    height: 100vh;
    font-size: 20px;
}

.content img {
    width: 300px;
    max-width: 100%;
    margin-top: 50px;
}
"""

BLP_TEXT = """
from flask import Blueprint
from .urls import url_patterns

{app_name} = Blueprint("{app_name}", __name__, url_prefix="/{app_name}")

for pattern in url_patterns:
    {app_name}.add_url_rule(rule=pattern[0], view_func=pattern[1])

from .errors import *
"""

VIEWS_TEXT = """
from flask import render_template, make_response

def index():
    template = render_template("index.html")
    response = make_response(template)

    return response
"""

BLP_VIEWS_TEXT = """
from flask import render_template, make_response

def index():
    template = render_template('{app_name}/index.html')
    response = make_response(template)

    return response
"""

ERRORS_TEXT = """
from . import {app_name}

@{app_name}.app_errorhandler(404)
def not_found(e):
    return "This route doesn't exist", 404
"""

BLP_STYLE = """
.qspan {
    color: #ec5a3b;
}
"""

BLP_INDEX = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='{app_name}/style.css') }}">
    <title>{app_name}</title>
</head>
<body>
    <p><span class="qspan">{app_name}</span> app's index view</p>
</body>
</html>
"""