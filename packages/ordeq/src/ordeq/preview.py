import logging

logger = logging.getLogger("ordeq.preview")


def preview(message: str, *args, **kwargs) -> None:
    """Warning to user that a feature is in preview"""
    logger.warning(message, *args, **kwargs)
