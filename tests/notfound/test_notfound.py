import requests
import os

port = int(os.getenv("PORT"))


class TestClass:

    ENDPOINT = f"http://localhost:{port}/notfound"

    def test_notfound_status_code(self):
        response = requests.get(self.ENDPOINT)
        assert response.status_code == 404

    def test_notfound_body(self):
        response = requests.get(self.ENDPOINT)
        body = {
            "success": False,
            "error": {
                "status": 404,
                "title": "Resource not found",
                "detail": "The requested resource does not exist",
            },
        }
        assert response.json() == body
