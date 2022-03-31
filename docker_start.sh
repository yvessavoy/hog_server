#!/bin/sh

# Run webserver in background
export FLASK_APP=hog_server
export FLASK_ENV=development
flask init-db
flask run -h 0.0.0.0 -p 3001 &

# Run grafana
/run.sh