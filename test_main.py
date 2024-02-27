from fastapi.testclient import TestClient
from main import app
from typing import Optional

client = TestClient(app)

def test_get_student_by_name_success():
    response = client.get("/get-by-name/1?name=John&test=1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "John",
        "age": 17,
        "year": "year 12"
    }

def test_get_student_by_name_not_found():
    response = client.get("/get-by-name/2?name=Jane&test=1")
    assert response.status_code == 200  # Adjust based on your error handling, might be 404 in some cases
    assert response.json() == {"Data": "Not Found"}

def test_get_student_without_name_param():
    response = client.get("/get-by-name/1?test=1")  # No name provided
    assert response.status_code == 200
    # This test might fail because your current implementation does not handle missing `name` correctly.
    # It's expected to return "Data: Not Found" or the details of the student with ID 1, depending on the intended behavior.
    assert response.json() == {"Data": "Not Found"}  # or the student data, depending on the implementation.