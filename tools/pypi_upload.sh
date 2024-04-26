#!/bin/bash

# Exit in case of error
set -e

# Define the package name and new version
PACKAGE_NAME="input_devices"
NEW_VERSION="0.1.1" # Increment this each time

# Navigate to the project root
cd /home/mark/Desktop/Projects/input_devices

# Update version in setup.py
sed -i "s/version='.*'/version='$NEW_VERSION'/" setup.py

# Remove old build artifacts
rm -rf dist/ build/ src/*.egg-info

# Build new distribution
python setup.py sdist bdist_wheel

# Upload to PyPI
twine upload dist/*
