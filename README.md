# About project
This simple project includes automation tests of the online demo shop: [<img style="-webkit-user-select: none;margin: auto;cursor: zoom-in;background-color: hsl(0, 0%, 90%);transition: background-color 300ms;" src="https://images.ctfassets.net/czwjnyf8a9ri/1v5ZWsPr8uNv6sj3qnL4MW/aeb69cbdfade387fd9db95aec0b12891/vector-sauce-bot-python_s.png?fm=webp&amp;w=800" width="100" height="50">](https://www.saucedemo.com/)  

The structure of the project is based on **Page Object Model** and with using **Selenium** + **Python**.  

Tests are checking ordering process (e2e testing), and testing login credentials.  

All tests are running on travis CI: [![Travis (.com)](https://img.shields.io/travis/com/Bryg9/selenium_python_demo_shop?logo=travis&style=for-the-badge)](https://www.travis-ci.com/Bryg9/selenium_python_demo_shop)

# How to run this project on Ubuntu 20.04.1
## Prepare your environment:
* Create and activate virtual environment:
```
  # virtual environment creation:
  $ python3 -m venv .venv

  # activation:
  $ source .venv/bin/activate

  # deactivation if needed:
  $ deactivate
```
* Install required libraries on active .venv environment:
```
  # basic command:
  $ pip install -r requirements.txt
  $ pip install -r test_requirements.txt

  # or you can use:
  $ make deps
  $ make test
```
* Check your installation:
```
  $ pip freeze
```
* Install geckodriver:
```
  # Remember that the geckodriver needs to be in PATH.
  # Check out if installed geckodriver is in /usr/bin or /usr/local/bin directory.
  $ sudo apt install firefox-geckodriver
```
* Fork this repository and clone from your GitHub:
```
  $ git clone https://github.com/<YOUR_GITHUB_USER_NAME>/selenium_python_demo_shop.git
```
## Run tests and check code syntax:
* Use Makefile command to run all tests:
```
  # to run all tests
  $ make test

  # to check syntax
  $ make lint
```
