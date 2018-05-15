from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import db
from app.application import create_app

instance = create_app('development')

migrate = Migrate(instance, db)

manager = Manager(instance)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
