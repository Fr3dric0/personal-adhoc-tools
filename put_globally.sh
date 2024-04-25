#!/bin/bash

set -e
set -o pipefail

echo "Copying scripts to into /usr/local/bin/"

sudo cp utlegsdeltaggere/__main__.py /usr/local/bin/utleggsdeltagere