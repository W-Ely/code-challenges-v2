#!/bin/sh

set -ex

echo "unittest coverage:"
coverage run -m unittest "$@" && coverage report
