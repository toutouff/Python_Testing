import pytest
import server


def client_getter():
    app = server.app
    return app.test_client()
