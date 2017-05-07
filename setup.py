import sys
import os
from setuptools import setup, find_packages

__version__ = None
with open('simplyhosting/version.py') as f:
    exec(f.read())

long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

test_requirements = []

def getRequires():
    deps = ['python_http_client>=2.1.1']
    if sys.version_info < (2, 7):
        deps.append('unittest2')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('unittest2py3k')
    return deps

setup(
    name='simplyhosting',
    version=str(__version__),
    author='Bernardo Vieira da Silva',
    author_email='benny.stuff@gmail.com',
    url='https://github.com/bernardosilva/simplyhosting-api-client-python/',
    packages=find_packages(exclude=["temp*.py", "register.py", "test"]),
    include_package_data=True,
    license='MIT',
    description='Simply Hosting library for Python',
    long_description=long_description,
    install_requires=getRequires(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2'
    ],
    test_suite='test',
    tests_require=test_requirements
)