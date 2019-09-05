#!/bin/sh
set -e

export UWSGI_HTTP=:$PORT

exec "$@"