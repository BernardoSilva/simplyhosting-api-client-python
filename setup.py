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
    deps = ['requests==2.13.0']
    if sys.version_info < (2, 7):
        deps.append('unittest2')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('unittest2py3k')
    return deps

setup(
    name='simplyhosting-api-client',
    version=str(__version__),
    author='Bernardo Vieira da Silva',
    author_email='benny.stuff@gmail.com',
    url='https://github.com/bernardosilva/simplyhosting-api-client-python/',
    packages=find_packages(exclude=["temp*.py", "register.py", "test"]),
    include_package_data=True,
    license='MIT',
    description='Simply Hosting API client library for Python',
    keywords= ['Simply Hosting', 'API', 'Client'],
    long_description=long_description,
    install_requires=getRequires(),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    test_suite='test',
    tests_require=test_requirements
)