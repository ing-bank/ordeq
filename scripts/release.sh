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

if [[ -z "$TARGET_BRANCH" ]]; then
    echo "Error: --target-branch argument is required"
    exit 1
fi

echo "GIT_REFERENCE: $GIT_REFERENCE"
echo "TARGET_BRANCH: $TARGET_BRANCH"
if [[ $GIT_REFERENCE == refs/tags/* ]]; then
    # Build triggered by a release (tag)
    PACKAGE=${GIT_REFERENCE#refs/tags/}
    PACKAGE=${PACKAGE%%/*}
    echo "$PACKAGE"
else
    # Build triggered by a branch or other reason
    GLOBAL_CHANGES=$(git diff --name-only $TARGET_BRANCH HEAD | grep -v '^packages/')
    echo "GLOBAL_CHANGES: $GLOBAL_CHANGES"
    if [[ -n "$GLOBAL_CHANGES" ]]; then
        # If there are any non-package changes, e.g. `pyproject.toml`, then run the pipelines for all packages
        CHANGED_FOLDERS=$(ls -d packages/* | cut -d'/' -f2 | tr '\n' ',' | sed 's/,$//')
    else
        # Otherwise only the packages for which files have changed
        CHANGED_FOLDERS=$(
            git diff --name-only "$TARGET_BRANCH" HEAD |
                grep '^packages/' |
                cut -d'/' -f2 |
                sort |
                uniq |
                # Only consider the packages that are non-empty
                while read -r pkg; do
                    if [ -d "packages/$pkg" ]; then
                        echo "$pkg"
                    fi
                done |
                tr '\n' ',' |
                sed 's/,$//'
        )
    fi
    echo "$CHANGED_FOLDERS"
fi
