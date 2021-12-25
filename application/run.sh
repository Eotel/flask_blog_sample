#!/bin/sh

export FLASK_APP=server
export FLASK_RUN_PORT=5000

flask init-db
flask run