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

