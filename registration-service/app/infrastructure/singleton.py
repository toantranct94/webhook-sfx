def singleton(class_):
    """
    Decorator that converts a class into a singleton.

    Args:
        class_: The class to be converted into a singleton.

    Returns:
        The singleton instance of the class.

    """
    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return wrapper
