from pathlib import Path

from ordeq import node, run
from ordeq_requests import ResponseJSON
from ordeq_yaml import YAML

user = ResponseJSON(url="https://jsonplaceholder.typicode.com/users/1")
yaml = YAML(path=Path("users.yml"))


@node(inputs=user, outputs=yaml)
def parse_users(user: dict) -> dict:
    """Parse user information.

    Args:
        user: A dictionary containing user information.

    Returns:
        A dictionary with user ID and formatted address.
    """

    return {
        "id": user["id"],
        "address": f"{user['address']['street']} {user['address']['zipcode']}",
    }


if __name__ == "__main__":
    run(parse_users)
