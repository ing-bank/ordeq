import catalog
from ordeq import node


@node(inputs=catalog.user, outputs=catalog.yaml)
def parse_users(user: dict) -> dict:
    return {
        "id": user["id"],
        "address": f"{user['address']['street']} {user['address']['zipcode']}",
    }
