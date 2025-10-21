import catalog
from ordeq import node


@node(inputs=catalog.user, outputs=catalog.yaml)
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
