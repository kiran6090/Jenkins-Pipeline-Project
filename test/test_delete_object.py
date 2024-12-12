import requests

# Variable to store the ID for reuse
generated_object_id = None

def test_post_add_object_response_data(base_url_post, sample_payload):
    """Validate the returned data from the POST request."""
    global generated_object_id  # Declare global to modify it
    response = requests.post(base_url_post, json=sample_payload)
    json_data = response.json()
    print(f"Response Data: {json_data}")
    
    # Store the ID from the response for later use
    generated_object_id = json_data.get("id")

def test_delete_object_status_code(base_url_delete):
    """Verify the API returns status code 200 for a DELETE request."""
    full_url = f"{base_url_delete}/{generated_object_id}"
    response = requests.delete(full_url)
    assert response.status_code == 200

def test_delete_object_response_format(base_url_delete):
    """Verify the response is in the correct format (a dictionary)."""
    response = requests.delete(base_url_delete)
    json_data = response.json()
    print(json_data)
    assert isinstance(json_data, dict)


