#!/bin/sh

set -eux

echo "black:"
if [ "$CONTEXT" = "ci" ]
then
    black --safe -v --check "$@"
else
    black --safe -v "$@"
fi
echo "pylint:"
pylint "$@"
echo "pycodestyle:"
pycodestyle "$@" --ignore=E203,E402,E711,E712,W503,W405,E231,E501 --max-line-length=88
