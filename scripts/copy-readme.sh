#!/bin/bash
set -e

if [ ! -f "README.md" ] || [ ! -d "packages" ]; then
  echo "Please run this script from the root of the repository."
  exit 3
fi

if [ $# -ne 1 ]; then
  echo "Usage: $0 <package-name>"
  exit 1
fi

pkg="packages/$1"
target="$pkg/README.md"
if [ -d "$pkg" ]; then
  if [ -f "$target" ]; then
    echo "README.md already exists in '$pkg'. Skipping copy."
  else
    cp README.md "$target"
  fi
else
  echo "Package directory '$pkg' does not exist."
  exit 2
fi
