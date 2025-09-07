#!/bin/bash

# Check if shell is bash
if [ -z "$BASH_VERSION" ]; then
    echo "Error: This script must be run with bash" >&2
    exit 1
fi

# Check if .venv exists, if not create it
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
    source ./.venv/bin/activate
    pip install -r requirements.txt
fi

# Activate the virtual environment
source ./.venv/bin/activate

# Add z3 to PATH
export PATH=./z3/build:$PATH

echo "Virtual environment activated and PATH updated"
