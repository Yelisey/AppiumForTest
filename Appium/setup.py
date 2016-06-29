#!/usr/bin/env python

import sys
from distutils.core import setup
from setuptools import setup


if sys.version_info < (3, 4):
    install_requires.append("enum34")

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def main():
    setup(
        name='AppiumAutoTestFramework',
        version='0.0.1',
        description='Autotests on Python with Appium',
        packages=['appium','allure',],
        install_requires=['selenium>=2.47.0',"lxml>=3.2.0","pytest>=2.7.3,<=2.9.0","namedlist","six>=1.9.0"],
        pytest_plugins=['allure.pytest_plugin']
)

if __name__ == '__main__':
    main()