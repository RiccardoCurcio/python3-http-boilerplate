import requests
import os

port = int(os.getenv("PORT", "3050"))


class TestClass:

    ENDPOINT = f"http://localhost:{port}/healthcheck"

    def test_healthcheck_status_code(self):
        response = requests.get(self.ENDPOINT)
        assert response.status_code == 200

    def test_healthcheck_body(self):
        response = requests.get(self.ENDPOINT)
        body = {"success": True, "data": {}}
        assert response.json() == body
