import inspect

from flask import jsonify


def create_response(item, serializer=None, status_code=200):
    """
    Create a response object for API endpoints.

    Args:
        item: The data to be serialized and returned in the response.
        serializer: The serializer object used to serialize the data.
            If not provided, the data will be returned as is.
        status_code: The HTTP status code to be returned in the response.
            Default is 200.

    Returns:
        A tuple containing the serialized data and the HTTP status code.

    """
    if not serializer:
        return jsonify(item), status_code

    if inspect.isclass(serializer):
        serializer = serializer()

    if isinstance(item, list):
        return jsonify(serializer.dump(item, many=True)), status_code
    elif isinstance(item, dict):
        item_selection = item["items"]
        item["items"] = serializer.dump(item_selection, many=True)
        return item, status_code
    else:
        return jsonify(serializer.dump(item)), status_code


def create_message_response(message, status_code=200):
    """
    Create a response with a message.

    Args:
        message (str): The message to include in the response.
        status_code (int, optional): The HTTP status code of the response.
            Defaults to 200.

    Returns:
        dict: The response containing the message and status code.
    """
    return {"message": message}, status_code
