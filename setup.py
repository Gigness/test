from setuptools import setup, find_packages

setup(
    name='web-auth',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy',
        'alembic',
        'psycopg2'
    ]
)