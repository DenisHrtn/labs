FROM python:3.11-slim

WORKDIR /app

COPY entrypoint.sh /app/entrypoint.sh

COPY . /app

# даем права на выполнение
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
