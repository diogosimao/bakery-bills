# bakery-bills

[![Build Status](https://travis-ci.org/diogosimao/bakery-bills.svg?branch=master)](https://travis-ci.org/diogosimao/bakery-bills)
[![Coverage Status](https://coveralls.io/repos/github/diogosimao/bakery-bills/badge.svg?branch=master)](https://coveralls.io/github/diogosimao/bakery-bills?branch=master)
[![Code Health](https://landscape.io/github/diogosimao/bakery-bills/master/landscape.svg?style=flat)](https://landscape.io/github/diogosimao/bakery-bills/master)
[![Requirements Status](https://requires.io/github/diogosimao/bakery-bills/requirements.svg?branch=master)](https://requires.io/github/diogosimao/bakery-bills/requirements/?branch=master)

## Hosted at Heroku

- Available on [https://bakery-bills.herokuapp.com/](https://bakery-bills.herokuapp.com/)

## API Documentation

- Available on [http://localhost:8000/docs/](http://127.0.0.1:8000/docs/)

## Stack

- Python >= 3.5
- PIP
- Pipenv

## Run the app locally

1. Make sure you have [Python >= 3.5](https://www.python.org/downloads/source/) and [PIP](https://pip.pypa.io/en/stable/installing/) installed.

    1.1. In order to install it on Ubuntu-like systems run:

        $ sudo apt-get install python3 \
            sudo apt-get install python3-pip

2. Install `Pipenv`.

        $ sudo pip3 install pipenv

3. Git clone this [repo](https://github.com/diogosimao/bakery-bills.git). Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed

        $ git clone https://github.com/diogosimao/bakery-bills.git && cd bakery-bills

4. Use `Pipenv` to create a virtualenv, install its dependencies and activate the virtualenv.

        $ pipenv --three && pipenv install && pipenv shell

5. Run `. ./bin/start_development.sh`

Development server should be up at [http://localhost:8000/](http://127.0.0.1:8000/).

## Run tests

1. Run `. ./bin/run_tests.sh` 

After that your browser should open with coverage report. 
