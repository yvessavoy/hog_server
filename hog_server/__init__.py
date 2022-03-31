import os
import click
from flask import Flask, request
from flask.cli import with_appcontext
from hog_server.database import get_device_id, get_type_id, add_measurement, init_db, close_db

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite3'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/measurements", methods=['POST'])
    def new_measurement():
        data = request.form
        data_type = data['type']
        data_value = data['value']
        tech_device_name = data['tech_device_name']

        device_id = get_device_id(tech_device_name)
        type_id = get_type_id(data_type)
        if not type_id or not device_id:
            return '', 400

        add_measurement(type_id, device_id, data_value)

        print(f"Type: {data['type']} - Value: {data['value']}")
        return '', 200

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

    return app

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')