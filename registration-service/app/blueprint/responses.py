import inspect

from flask import jsonify


def create_response(item, serializer=None, status_code=200):

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
    return {"message": message}, status_code
