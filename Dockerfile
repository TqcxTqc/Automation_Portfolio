FROM mcr.microsoft.com/playwright/python:v1.39.0-jammy

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["pytest"]
CMD ["tests/"]