from ordeq import node

from starter_package import catalog


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
