#!/bin/sh

HOST="localhost"
PORT=5432
USER=${POSTGRES_USERNAME}
DATABASE=$1

createdb ${DATABASE} -E UTF8 -h ${HOST} -p ${PORT} -U ${USER} -W
