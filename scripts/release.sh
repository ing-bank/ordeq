#!/bin/bash

# Parse command-line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
    --git-ref)
        GIT_REFERENCE="$2"
        shift
        ;;
    --target-branch)
        TARGET_BRANCH="$2"
        shift
        ;;
    *)
        echo "Unknown parameter passed: $1"
        exit 1
        ;;
    esac
    shift
done

if [[ -z "$GIT_REFERENCE" ]]; then
    echo "Error: --git-ref argument is required"
    exit 1
fi

echo "GIT_REFERENCE: $GIT_REFERENCE"

PACKAGE=${GIT_REFERENCE#refs/tags/}
PACKAGE=${PACKAGE%%/*}
echo "$PACKAGE"
