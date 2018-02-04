import os
import sqlalchemy as sa


user = os.environ['db_username']
password = os.environ['password']
hostname = os.environ['hostname']
db_name = os.environ['db_name']
dev_mode = os.environ['dev_mode']


engine = sa.create_engine(
    'postgresql://{user}:{password}@{hostname}/{db_name}'.format(
        user=user,
        password=password,
        hostname=hostname,
        db_name=db_name
    ),
    echo=True if dev_mode == 'DEV' else False
)
