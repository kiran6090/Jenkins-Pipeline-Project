import requests

def test_get_single_object_status_code(base_url_patch):
    """Verify the API returns status code 200 for a single object request."""
    response = requests.get(base_url_patch)
    assert response.status_code == 200
    
    
def test_post_add_object_response_data(base_url_patch):
    """Validate the  data from the PATCH request."""
    response = requests.post(base_url_patch)
    json_data = response.json()
    print(json_data)
    