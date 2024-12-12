import requests

def test_get_objects_by_ids_status_code(base_url_by_ids):
    """Verify the API returns status code 200."""
    response = requests.get(base_url_by_ids)
    assert response.status_code == 200

def test_get_objects_by_ids_response_format(base_url_by_ids):
    """Verify the response is in the correct format (a list)."""
    response = requests.get(base_url_by_ids)
    json_data = response.json()
    assert isinstance(json_data, list)

def test_get_objects_by_ids_contains_expected_fields(base_url_by_ids):
    """Verify the objects in the response contain expected fields."""
    response = requests.get(base_url_by_ids)
    json_data = response.json()
    for obj in json_data:
        assert "id" in obj
        assert "name" in obj
        assert "data" in obj

def test_object_data_validation(base_url_by_ids):
    """Validate the data for specific objects returned by the API."""
    response = requests.get(base_url_by_ids)
    json_data = response.json()
    for obj in json_data:
        if obj["id"] == "3":
            assert obj["name"] == "Apple iPhone 12 Pro Max"
            assert obj["data"]["color"] == "Cloudy White"
            assert obj["data"]["capacity GB"] == 512
        elif obj["id"] == "5":
            assert obj["name"] == "Samsung Galaxy Z Fold2"
            assert obj["data"]["price"] == 689.99
            assert obj["data"]["color"] == "Brown"
        elif obj["id"] == "10":
            assert obj["name"] == "Apple iPad Mini 5th Gen"
            assert obj["data"]["Capacity"] == "64 GB"
            assert obj["data"]["Screen size"] == 7.9

def test_objects_with_null_data(base_url_by_ids):
    """Ensure there are no objects with null 'data' fields."""
    response = requests.get(base_url_by_ids)
    json_data = response.json()
    null_data_objects = [obj for obj in json_data if obj["data"] is None]
    assert len(null_data_objects) == 0
    print(json_data)
