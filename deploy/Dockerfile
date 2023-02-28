FROM python:3.9.6-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*


WORKDIR /app/src

RUN pip install poetry==1.2.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying actuall application
COPY . .

# Installing requirements
RUN poetry install

# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*
RUN chmod +x config/entrypoint.sh
EXPOSE 8000

#CMD ["/usr/local/bin/python", "-m", "arbitrage"]
ENTRYPOINT ["./config/entrypoint.sh"]
