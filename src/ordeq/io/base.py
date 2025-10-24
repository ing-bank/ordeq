# ...existing code...

def _get_resources_of(io: object) -> list:
    """Get all resources from the given io object and its base classes.

    Args:
        io: The io object to retrieve resources from.

    Returns:
        A list of resources from the io object and all its base classes.
    """
    resources = []
    for cls in io.__class__.__mro__:
        if hasattr(cls, "resources"):
            resources += getattr(cls, "resources")
    return resources

# ...existing code...

