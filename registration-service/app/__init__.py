import os

from flask import Flask


def create_app(test_config: dict = {}) -> Flask:
    """This function is responsible to create a Flask instance according
    a previous setting passed from environment. In that process, it also
    initialise the database source.

    Parameters:
        test_config (dict): settings coming from test environment

    Returns:
        flask.app.Flask: The application instance
    """

    app = Flask(__name__, instance_relative_config=True)

    load_config(app, test_config)

    init_logging(app)
    init_database(app)
    init_blueprints(app)
    init_dependency(app, dependency_container_packages=['app.blueprint.api'])

    return app


def load_config(app: Flask, test_config) -> None:
    """Load the application's config

    Parameters:
        app (flask.app.Flask): The application instance
            Flask that'll be running
        test_config (dict):
    """

    if os.environ.get('FLASK_ENV') == 'development' or \
            test_config.get("FLASK_ENV") == 'development':
        app.config.from_object('app.config.Development')

    elif test_config.get('TESTING'):
        app.config.from_mapping(test_config)

    else:
        app.config.from_object('app.config.Production')


def init_database(app) -> None:
    """Responsible for initializing and connecting to the database
    to be used by the application.

    Parameters:
        app (flask.app.Flask): The application instance
            Flask that'll be running
    """
    from .infrastructure.databases import init
    init(app)


def init_blueprints(app: Flask) -> None:
    """Registes the blueprint to the application.

    Parameters:
        app (flask.app.Flask): The application instance
            Flask that'll be running
    """

    # error handlers
    from .blueprint.api import people, webhook
    from .blueprint.handlers import register_error_handler
    register_error_handler(app)

    # error Handlers
    from .blueprint import index

    app.register_blueprint(index.bp)
    app.register_blueprint(people.bp)
    app.register_blueprint(webhook.bp)


def init_logging(app: Flask) -> None:
    """Initialize the application logging

    Parameters:
        app (flask.app.Flask): The application instance
            Flask that'll be running
    """
    from .logging import setup_logging
    setup_logging(app)


def init_dependency(
    app: Flask,
    dependency_container_packages=None,
    dependency_container_module=None
) -> None:
    """Initialize the application dependency

    Parameters:
        app (flask.app.Flask): The application instance
            Flask that'll be running
    """
    from .dependency_container import setup_dependency_container
    setup_dependency_container(
        app,
        modules=dependency_container_module,
        packages=dependency_container_packages)
