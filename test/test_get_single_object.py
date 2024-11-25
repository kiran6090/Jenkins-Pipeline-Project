import requests

def test_get_single_object_status_code(base_url_single_object):
    """Verify the API returns status code 200 for a single object request."""
    response = requests.get(base_url_single_object)
    assert response.status_code == 200

def test_get_single_object_response_format(base_url_single_object):
    """Verify the response is in the correct format (a dictionary)."""
    response = requests.get(base_url_single_object)
    json_data = response.json()
    assert isinstance(json_data, dict)

def test_single_object_contains_expected_fields(base_url_single_object):
    """Verify the object contains the required fields."""
    response = requests.get(base_url_single_object)
    json_data = response.json()
    assert "id" in json_data
    assert "name" in json_data
    assert "data" in json_data

def test_single_object_data_validation(base_url_single_object):
    """Validate the data for the object with ID 7."""
    response = requests.get(base_url_single_object)
    json_data = response.json()
    assert json_data["id"] == "7"
    assert json_data["name"] == "Apple MacBook Pro 16"
    assert json_data["data"]["year"] == 2019
    assert json_data["data"]["price"] == 1849.99
    assert json_data["data"]["CPU model"] == "Intel Core i9"
    assert json_data["data"]["Hard disk size"] == "1 TB"
