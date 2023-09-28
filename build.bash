#!/bin/bash

# Ensure we are in the directory containing pyproject.toml
if [ ! -f "pyproject.toml" ]; then
    echo "pyproject.toml not found in the current directory."
    exit 1
fi

# Extract version from pyproject.toml
version=$(grep -E '^version =' pyproject.toml | cut -d\" -f2)

# Split the version into major, minor, and patch
major=$(echo $version | cut -d. -f1)
minor=$(echo $version | cut -d. -f2)
patch=$(echo $version | cut -d. -f3)

# Increment the version
if [ "$patch" -eq 9 ]; then
    patch=0
    minor=$((minor + 1))
else
    patch=$((patch + 1))
fi

# Construct the new version
new_version="$major.$minor.$patch"

# Replace the old version with the new version in pyproject.toml
sed -i.bak "s/version = \"$version\"/version = \"$new_version\"/g" pyproject.toml

# Update the version in docs/index.md
sed -i.bak "s/version = \"$version\"/version = \"$new_version\"/g" docs/index.md

# Publish to PYPI with poetry
poetry publish --build

# Commit the changes
git add .
git commit -m "Version $new_version"
git push 

# Remove the backup files created by sed
rm pyproject.toml.bak
rm docs/index.md.bak