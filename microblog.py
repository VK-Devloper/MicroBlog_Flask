from app import app, db, login
from app.models import User, Post
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_script import Shell, Manager

db.init_app(app)
manager = Manager(app)
bootstrap = Bootstrap()
moment = Moment()


def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command('shell', Shell(make_context=make_shell_context))


if __name__ == '__main__':
    login.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    # manager.run()
    app.run(port=5000, debug=True)

