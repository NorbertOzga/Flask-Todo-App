from flask.cli import FlaskGroup

from run import app
from todo.extension import database

cli = FlaskGroup(app)


@cli.command('create_database')
def create_database():
    database.drop_all()
    print('Dropped all tables...')

    database.create_all()
    print('Created all tables...')

    database.session.commit()
    print('Database created.')


if __name__ == '__main__':
    cli()
