import os
import config
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# Construct core Flask application with embedded Dash app.
app = Flask(__name__, instance_relative_config=False)
Bootstrap(app)
CONFIG = config.ProdConfig if os.environ.get("APP_SETTING") else config.DevConfig
app.config.from_object(CONFIG)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


with app.app_context():
    # Import parts of our core Flask app
    from app import routes, errors, models, db  # noqa

    # Import Dash application
    from .plotly_dash.dashboard import init_dashboard

    app = init_dashboard(app)

    db.create_all()
