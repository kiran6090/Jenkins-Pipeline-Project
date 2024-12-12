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

def test_put_update_object_status_code(base_url_put, update_payload):
    """Verify the API returns status code 200 for a PUT request."""
    
    # Use the generated ID dynamically
    full_url = f"{base_url_put}/{generated_object_id}"
    response = requests.put(full_url, json=update_payload)
    print(f"the status code of put object is: { response.status_code}")
    print(f"Response Headers: {response.headers}")
    print(f"response text:{response.text}")
    
    assert response.status_code == 200

def test_put_update_object_response_format(base_url_put, update_payload):
    """Verify the response is in the correct format (a dictionary)."""
    response = requests.put(base_url_put, json=update_payload)
    json_data = response.json()
    assert isinstance(json_data, dict)



