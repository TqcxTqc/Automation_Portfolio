#!/bin/bash

docker-compose up
allure serve ./reports/allure-results
docker container rm run_test