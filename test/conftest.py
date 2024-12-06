import pytest

@pytest.fixture(scope="session")
def base_url_all_objects():
    """Fixture for the base URL to get all objects."""
    return "https://api.restful-api.dev/objects"

@pytest.fixture(scope="session")
def base_url_by_ids():
    """Fixture for the base URL to get objects by IDs."""
    return "https://api.restful-api.dev/objects?id=3&id=5&id=10"

@pytest.fixture(scope="session")
def base_url_single_object():
    """Fixture for the base URL for single object testing."""
    return "https://api.restful-api.dev/objects/7"
@pytest.fixture(scope="session")
def base_url_post():
    """Fixture for the base URL for POST requests."""
    return "https://api.restful-api.dev/objects"

@pytest.fixture
def sample_payload():
    """Fixture for the sample payload for adding an object."""
    return {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    
@pytest.fixture(scope="session")
def base_url_update():
    """Fixture for the base URL for updating an object."""
    return "https://api.restful-api.dev/objects/7"

@pytest.fixture
def update_payload():
    """Fixture for the payload for updating an object."""
    return {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    
@pytest.fixture(scope="session")
def base_url_delete():
    """Fixture for the base URL for deleting an object."""
    return "https://api.restful-api.dev/objects/6"        

