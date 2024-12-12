import requests

def test_post_add_object_status_code(base_url_post, sample_payload):
    """Verify the API returns status code 200 for a POST request."""
    response = requests.post(base_url_post, json=sample_payload)
    assert response.status_code == 200

def test_post_add_object_response_format(base_url_post, sample_payload):
    """Verify the response is in the correct format (a dictionary)."""
    response = requests.post(base_url_post, json=sample_payload)
    json_data = response.json()
    assert isinstance(json_data, dict)


    # Verify that the response contains expected data
    assert json_data["name"] == sample_payload["name"]
    assert json_data["data"] == sample_payload["data"]
    assert "id" in json_data
    assert "createdAt" in json_data
    
def test_post_add_object_response_data(base_url_post, sample_payload):
    """Validate the returned data from the POST request."""
    response = requests.post(base_url_post, json=sample_payload)
    json_data = response.json()
    print(json_data)
