#!/bin/bash

docker build -t my_tests .
docker run --name run_test my_tests
docker cp run_test:/app/reports .
allure serve ./reports/allure-results
docker container rm run_test