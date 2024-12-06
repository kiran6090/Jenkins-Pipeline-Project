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

def test_put_update_object_response_data(base_url_update, update_payload):
    """Validate the returned data from the PUT request."""
    response = requests.put(base_url_update, json=update_payload)

    # Validate specific fields within the `data` object
    data = json_data["data"]
    assert data["year"] == update_payload["data"]["year"], f"Expected year {update_payload['data']['year']}, got {data.get('year')}"
    assert data["price"] == update_payload["data"]["price"], f"Expected price {update_payload['data']['price']}, got {data.get('price')}"
    assert data["CPU model"] == update_payload["data"]["CPU model"], f"Expected CPU model {update_payload['data']['CPU model']}, got {data.get('CPU model')}"
    assert data["Hard disk size"] == update_payload["data"]["Hard disk size"], f"Expected Hard disk size {update_payload['data']['Hard disk size']}, got {data.get('Hard disk size')}"
    assert data["color"] == update_payload["data"]["color"], f"Expected color {update_payload['data']['color']}, got {data.get('color')}"

    # Check if updatedAt exists
    assert "updatedAt" in json_data, "The 'updatedAt' field is missing in the response."

