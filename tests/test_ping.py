import pytest
import aiohttp
from unittest.mock import patch, MagicMock
from src.ping import ping_api, ping_all_apis

@pytest.mark.asyncio
async def test_ping_api_success():
    mock_session = MagicMock(spec=aiohttp.ClientSession)
    mock_response = MagicMock()
    mock_response.status = 200
    mock_session.get.return_value.__aenter__.return_value = mock_response

    result = await ping_api(mock_session, "https://example.com")
    assert result["success"] == True
    assert result["status_code"] == 200

@pytest.mark.asyncio
async def test_ping_api_failure():
    mock_session = MagicMock(spec=aiohttp.ClientSession)
    mock_session.get.side_effect = aiohttp.ClientError("Connection error")

    result = await ping_api(mock_session, "https://example.com")
    assert result["success"] == False
    assert "Connection error" in result["error"]

@pytest.mark.asyncio
@patch('src.ping.Config.API_URLS', ['https://example1.com', 'https://example2.com'])
@patch('src.ping.ping_api')
async def test_ping_all_apis(mock_ping_api):
    mock_ping_api.return_value = {"success": True, "url": "https://example.com", "response_time": 0.1}
    
    await ping_all_apis()
    
    assert mock_ping_api.call_count == 2