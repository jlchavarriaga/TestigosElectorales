import json
from fastapi.responses import JSONResponse


class ApiResponser:

    @staticmethod
    def response(**kwargs):
        return JSONResponse(**kwargs)

    @staticmethod
    def error_response(exception, code: int = 500):
        content = {
            "internal_error": "An error has ocurred, "
            "contact system administrator",
            "description": str(exception)
        }

        return ApiResponser.response(status_code=code, content=content)

    @staticmethod
    def success_response(data, code: int = 200):
        if type(data) is str:
            data = json.loads(data)

        return ApiResponser.response(status_code=code, content=data)

    @staticmethod
    def client_error_response(msg, code: int = 400):
        content = {
            'message': msg
        }

        return ApiResponser.response(status_code=code, content=content)

    @staticmethod
    def bad_request_response(msg):
        return ApiResponser.client_error_response(msg, 400)

    @staticmethod
    def unauthorized_response(msg: str):
        return ApiResponser.client_error_response(msg, 403)
