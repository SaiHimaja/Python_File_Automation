import pytest
from unittest.mock import patch
from service_checker import check_service

@patch('service_checker.check_service.requests.post')
def test_create_incident_success(mock_post):
    # Mocking ServiceNow API response
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {
        "result": {
            "number": "INC0012345"
        }
    }

    check_service.create_incident(
        short_description="Test incident",
        description="This is a test incident created by Pytest."
    )

    mock_post.assert_called_once()
    payload = mock_post.call_args.kwargs['json']
    assert payload['short_description'] == "Test incident"
    assert payload['urgency'] == "2"
