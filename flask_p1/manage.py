from myapp import create_app
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from myapp.exts import db
from myapp.models import Movie
app=create_app()
migrate=Migrate(app,db)
manager=Manager(app)
manager.add_command("db",MigrateCommand)
if __name__ == '__main__':
    manager.run()
