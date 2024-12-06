import requests

def test_put_update_object_status_code(base_url_update, update_payload):
    """Verify the API returns status code 405 for a PUT request."""
    response = requests.put(base_url_update, json=update_payload)
    assert response.status_code == 405

def test_put_update_object_response_format(base_url_update, update_payload):
    """Verify the response is in the correct format (a dictionary)."""
    response = requests.put(base_url_update, json=update_payload)
    json_data = response.json()
    assert isinstance(json_data, dict)


