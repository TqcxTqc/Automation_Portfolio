# Use an official Playwright image as the base image
FROM mcr.microsoft.com/playwright:v1.39.0-jammy

# Set the working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y curl unzip openjdk-11-jre-headless python3-pip

# Install Allure
RUN curl -o allure.zip -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.14.0/allure-commandline-2.14.0.zip && \
    unzip allure.zip -d /opt/ && \
    rm allure.zip

# Set Allure in the PATH
ENV PATH="/opt/allure-2.14.0/bin:${PATH}"

# Copy the application code
COPY . .

# Install Python dependencies
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

CMD ["pytest"]
