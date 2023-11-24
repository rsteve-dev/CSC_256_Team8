from flask import Flask, request, jsonify
from functools import wraps

key = "XvbjR6NKcSkFVGtMqBzGUxKInKKH6k8K"


def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        headers = request.headers
        api_key = headers["Key"]
        print(request.headers)
        if api_key != key:
            response = jsonify({"error": "Unauthorized access"})
            response.status_code = 401
            return response

        return f(*args, **kwargs)

    return decorated_function
