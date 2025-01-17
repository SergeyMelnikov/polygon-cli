#!/usr/bin/env python3
from setuptools import setup

setup(
        name='polygon-cli',
        version='1.1.10',
        packages=['polygon_cli', 'polygon_cli.actions'],
        url='https://github.com/kunyavskiy/polygon-cli',
        license='MIT',
        author='Pavel Kunyavskiy',
        author_email='kunyavskiy@gmail.com',
        description='Commandline tool for polygon',
        install_requires=['colorama', 'requests', 'prettytable', 'pyyaml'],
        entry_points={
            'console_scripts': [
                'polygon-cli=polygon_cli:main'
            ],
        }
)
