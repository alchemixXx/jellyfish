from flask import Flask

from chat.routes import main
from db import db

app = Flask(__name__)


def run_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
    app.register_blueprint(main)
    db.init_app(app)
    return app


if __name__ == '__main__':
    run_app().run(debug=True, host='0.0.0.0')
