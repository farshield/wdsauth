import os
from wdsauth import create_app, db
from wdsauth.epicenter.models import Static, Wormhole
from flask_script import Manager, Shell


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    return dict(
        app=app,
        db=db,
        Static=Static, Wormhole=Wormhole,
    )

manager.add_command("shell", Shell(make_context=make_shell_context))


if __name__ == '__main__':
    manager.run()
