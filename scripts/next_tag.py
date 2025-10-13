import argparse
import re
import subprocess
import sys


def get_tags(package: str) -> list[str]:
    """Get all git tags for a given package.

    Args:
        package: The package name, e.g. 'ordeq'.

    Returns:
        A list of tags for the package.
    """
    result = subprocess.run(
        ["git", "tag", "-l", f"{package}/v*"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip().splitlines()


def parse_version(tag: str) -> tuple[int, int, int]:
    """Parse a version tag into a tuple of integers.

    Args:
        tag: The git tag, e.g. 'ordeq/v1.2.3'.

    Returns:
        A tuple of integers representing the version, e.g. (1, 2, 3).

    Raises:
        ValueError: If the tag does not match the expected version pattern.
    """
    match = re.search(r"v(\d+)\.(\d+)\.(\d+)", tag)
    if not match:
        raise ValueError(f"Tag {tag} does not match version pattern.")
    return tuple(map(int, match.groups()))


def bump_version(
    version: tuple[int, int, int], bump: str
) -> tuple[int, int, int]:
    """Bump the version based on the specified type.

    Args:
        version: A tuple of integers representing the current version, e.g.
            (1, 2, 3).
        bump: The type of bump to apply, one of 'major', 'minor', or 'patch'.

    Returns:
        A tuple of integers representing the new version after the bump.

    Raises:
        ValueError: If the bump type is unknown.
    """
    major, minor, patch = version
    if bump == "major":
        return major + 1, 0, 0
    if bump == "minor":
        return major, minor + 1, 0
    if bump == "patch":
        return major, minor, patch + 1
    raise ValueError(f"Unknown bump type: {bump}")


def get_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for the script.

    Returns:
        The argument parser.
    """

    parser = argparse.ArgumentParser(
        description="Bump package git tag version."
    )
    parser.add_argument(
        "--package", "-p", required=True, help="Package package, e.g. ordeq"
    )
    parser.add_argument(
        "--bump", choices=["major", "minor", "patch", "auto"], required=True
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the new tag but do not create it.",
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the new tag to the origin remote.",
    )
    parser.add_argument("--message", "-m", required=False, help="Tag message.")
    return parser


def get_last_commit_message(package: str, last_tag: str) -> str:
    """Get the last commit message in the package directory between the last
    tag and HEAD.

    Args:
        package: The package name, e.g. 'ordeq'.
        last_tag: The last tag for the package, e.g. 'ordeq/v1.2.3'.

    Returns:
        The message of the most recent commit in the package directory after
        the last tag.
    """

    package_path = f"packages/{package}/"
    result = subprocess.run(
        ["git", "log", "-1", f"{last_tag}..HEAD", "--pretty=%s", package_path],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def infer_bump_type_from_commit(commit_msg: str) -> str | None:
    """Infer the change type from the last commit message.

    Args:
        commit_msg: The commit message to analyze.

    Returns:
        The inferred bump type: 'major', 'minor', or 'patch'.
    """

    if commit_msg.startswith("feat!:"):
        return "major"
    if commit_msg.startswith("feat:"):
        return "minor"
    if commit_msg.startswith("fix:"):
        return "patch"
    return None


def main():
    parser = get_parser()
    args = parser.parse_args()

    tags = get_tags(args.package)
    if not tags:
        print(f"No tags found for package {args.package}.")
        sys.exit(1)

    versions = [parse_version(tag) for tag in tags]
    max_version = max(versions)
    max_tag = (
        f"{args.package}/v{max_version[0]}.{max_version[1]}.{max_version[2]}"
    )

    last_commit_msg = get_last_commit_message(args.package, max_tag)

    bump_type = args.bump
    if bump_type == "auto":
        bump_type = infer_bump_type_from_commit(last_commit_msg)
        if not bump_type:
            print(
                "Could not infer change type from commit message. "
                "Please specify --bump explicitly. "
            )
            sys.exit(0)

    new_version = bump_version(max_version, bump_type)
    new_tag = (
        f"{args.package}/v{new_version[0]}.{new_version[1]}.{new_version[2]}"
    )

    if not args.message:
        print(
            "No tag message provided, using last commit message as tag "
            "message."
        )
        message = last_commit_msg
    else:
        message = args.message

    print(
        f"Latest tag: "
        f"{args.package}/v{max_version[0]}.{max_version[1]}.{max_version[2]}"
    )
    print(f"Bumping to: {new_tag}")

    if not args.dry_run:
        subprocess.run(
            ["git", "tag", "-a", new_tag, "-m", message], check=True
        )
        print(f"Created new tag: {new_tag} with message: {message}")
        if args.push:
            subprocess.run(["git", "push", "origin", new_tag], check=True)
            print(f"Pushed tag {new_tag} to origin.")
    else:
        print(
            f"Dry run: tag {new_tag} would be created with message: {message}"
        )


if __name__ == "__main__":
    main()
