# Automated Testing Framework with Python, Docker, Playwright, and Allure Reporting

This repository contains an automation framework built using Python, Playwright, and pytest to test web applications. It utilizes Docker to simplify the test environment setup and execution.

WEBSITE: https://magento.softwaretestingboard.com

## Features
- **Cross-browser testing:** The framework supports testing across Chromium, Firefox, and WebKit browsers using Playwright's unified API.
- **Headless execution:** Tests can be run in headless mode, reducing the browser's UI overhead and improving test execution speed.
- **Organized test structure:** Tests are structured using Page Objects to maintain separation of concerns and improve test maintainability.
- **pytest integration:** The framework utilizes pytest as the test runner for executing tests and generating comprehensive test reports.
- **Allure reporting:** The framework generates comprehensive and detailed test reports using Allure, providing valuable insights into test execution.
- **GitHub Actions integration:** Automated testing and report generation are integrated with GitHub Actions, ensuring that reports are generated seamlessly after each test execution.
- **GitHub Pages report publishing:** Generated reports are published to the GitHub Pages repository, making them easily accessible and shareable
- **Dockerized environment:** The framework is packaged using Docker to ensure consistent test execution across different environments.

### Getting Started
<br>

1. #### Clone the repository

````
git clone https://github.com/TqcxTqc/Automation_Portfolio
````
#### Install dependencies

````
cd Automation_Portfolio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

### Run tests:

````
pytest tests
````

### Generate report

````
allure serve ./reports/allure-results
````

### Simple launch

This bash script will launch creation of docker container with run tests, generate report after the test is finished and remove the container

````
./run_tests.sh
````

## Modify/Add Tests
To add or modify tests, navigate to the ```tests``` directory. Each test case is represented by a ```.py``` file with a descriptive name. Page Objects are located in the ```pages``` directory.

