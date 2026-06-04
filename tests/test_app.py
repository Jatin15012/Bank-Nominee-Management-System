import sys
import os

# add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import app

def test_home():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200