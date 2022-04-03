FROM grafana/grafana:latest

# Switch to root temporarily
USER root

# Install python
RUN apk add curl python3 py3-pip sqlite

# Setup folder structure
RUN mkdir -p /app/instance
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

# Copy relevant files over
COPY docker_start.sh /app/docker_start.sh
RUN chmod +x /app/docker_start.sh

COPY hog_server /app/hog_server

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/app/docker_start.sh"]
