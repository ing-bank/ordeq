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
readme_target="$pkg/README.md"
license_target="$pkg/LICENSE"

if [ -d "$pkg" ]; then
  if [ -f "$readme_target" ]; then
    echo "README.md already exists in '$pkg'. Skipping copy."
  else
    cp README.md "$readme_target"
  fi

  if [ -f "$license_target" ]; then
    echo "LICENSE already exists in '$pkg'. Skipping copy."
  else
    cp LICENSE "$license_target"
  fi
else
  echo "Package directory '$pkg' does not exist."
  exit 2
fi
