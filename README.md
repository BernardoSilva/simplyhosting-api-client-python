# Simply Hosting API Client for Python

[![Build Status](https://travis-ci.org/BernardoSilva/simplyhosting-api-client-python.svg?branch=master)](https://travis-ci.org/BernardoSilva/simplyhosting-api-client-python) 
[![Coverage Status](https://coveralls.io/repos/github/BernardoSilva/simplyhosting-api-client-python/badge.svg)](https://coveralls.io/github/BernardoSilva/simplyhosting-api-client-python)

## How to install

```bash
pip install ...
```

## How to use

```python
import simplyhosting


simplyClient = simplyhosting.Client(api_key='xxx', api_secret='your-api-secret')
response = simplyClient.user().ping().call()
```

## How to setup

```bash
git clone git@github.com:BernardoSilva/simplyhosting-api-client-python.git
python setup.py install
```

## How to contribute


```bash
git clone git@github.com:BernardoSilva/simplyhosting-api-client-python.git
python setup.py develop
```

### How to run tests

```bash
python setup.py test
```

If you want to run this project on multiple environments you need ot install tox package.

```bash
python -m pip install tox
```

and then just run tox command from the root of the project

```bash
tox
```

## How to contribute

Just [check the issues list](https://github.com/BernardoSilva/simplyhosting-api-client-python/issues) and open a Pull Request to help us improve this library.

If you find any problem or have a suggestion open a [new issue](https://github.com/BernardoSilva/simplyhosting-api-client-python/issues/new)

