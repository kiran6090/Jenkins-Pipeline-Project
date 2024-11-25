import requests

def test_get_all_objects_status_code(base_url_all_objects):
    """Verify the API for getting all objects returns status code 200."""
    response = requests.get(base_url_all_objects)
    assert response.status_code == 200

def test_get_all_objects_response_format(base_url_all_objects):
    """Verify the response is in the correct format (a list)."""
    response = requests.get(base_url_all_objects)
    json_data = response.json()
    assert isinstance(json_data, list)

def test_all_objects_contain_expected_fields(base_url_all_objects):
    """Verify all objects in the response contain expected fields."""
    response = requests.get(base_url_all_objects)
    json_data = response.json()
    for obj in json_data:
        assert "id" in obj
        assert "name" in obj
        assert "data" in obj

def test_object_sample_validation(base_url_all_objects):
    """Validate specific object properties based on sample data."""
    response = requests.get(base_url_all_objects)
    json_data = response.json()
    for obj in json_data:
        if obj["id"] == "1":
            assert obj["name"] == "Google Pixel 6 Pro"
            assert obj["data"]["color"] == "Cloudy White"
            assert obj["data"]["capacity"] == "128 GB"

def test_objects_with_null_data(base_url_all_objects):
    response = requests.get(base_url_all_objects)
    json_data = response.json()
    null_data_objects = [obj for obj in json_data if obj["data"] is None]
    assert len(null_data_objects) > 0


