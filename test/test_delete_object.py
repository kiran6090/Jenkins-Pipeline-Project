import requests

def test_delete_object_status_code(base_url_delete):
    """Verify the API returns status code 405 for a DELETE request."""
    response = requests.delete(base_url_delete)
    assert response.status_code == 405

def test_delete_object_response_format(base_url_delete):
    """Verify the response is in the correct format (a dictionary)."""
    response = requests.delete(base_url_delete)
    json_data = response.json()
    assert isinstance(json_data, dict)


