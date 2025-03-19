from setuptools import setup, find_packages

setup(
    name='sql_utils',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'sqlalchemy',
        'trino'
    ],
    description='A collection of utilities for working with SQL databases',
    author='Levi Leach',
    author_email='levi.leach@rokt.com',
    url='https://github.com/levileachrokt/sql-utils'
    
)