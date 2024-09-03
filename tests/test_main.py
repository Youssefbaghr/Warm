from src.config import Config
import pytest
from unittest.mock import patch, MagicMock
from main import load_urls_from_env, main

def test_load_urls_from_env():
    with patch.dict('os.environ', {
        'API_URL_1': 'https://api1.com',
        'API_URL_2': 'https://api2.com',
        'API_URL_3': 'https://conversai-back.onrender.com',
        'OTHER_VAR': 'not_an_api_url'
    }):
        urls = load_urls_from_env()
        assert set(urls) == {'https://api1.com', 'https://api2.com', 'https://conversai-back.onrender.com'}

    
@patch('main.load_dotenv')
@patch('main.setup_logging')
@patch('main.load_urls_from_env')
@patch('main.start_scheduler')
def test_main_success(mock_start_scheduler, mock_load_urls, mock_setup_logging, mock_load_dotenv):
    mock_logger = MagicMock()
    mock_setup_logging.return_value = mock_logger
    mock_load_urls.return_value = ['https://api1.com', 'https://api2.com']

    main()

    mock_load_dotenv.assert_called_once()
    mock_setup_logging.assert_called_once()
    mock_load_urls.assert_called_once()
    mock_start_scheduler.assert_called_once()
    mock_logger.info.assert_any_call("Starting Warm - API Warming Service")
    mock_logger.info.assert_any_call("Loaded 2 URLs. Ping interval set to 12 minutes.")

@patch('main.load_dotenv')
@patch('main.setup_logging')
@patch('main.load_urls_from_env')
@patch('main.start_scheduler')
def test_main_no_urls(mock_start_scheduler, mock_load_urls, mock_setup_logging, mock_load_dotenv):
    mock_logger = MagicMock()
    mock_setup_logging.return_value = mock_logger
    mock_load_urls.return_value = []

    main()

    mock_load_dotenv.assert_called_once()
    mock_setup_logging.assert_called_once()
    mock_load_urls.assert_called_once()
    mock_start_scheduler.assert_not_called()
    mock_logger.warning.assert_called_with("No API URLs found in environment variables.")

@patch('main.load_dotenv')
@patch('main.setup_logging')
@patch('main.load_urls_from_env')
def test_main_exception(mock_load_urls, mock_setup_logging, mock_load_dotenv):
    mock_logger = MagicMock()
    mock_setup_logging.return_value = mock_logger
    mock_load_urls.side_effect = Exception("Test exception")

    main()

    mock_load_dotenv.assert_called_once()
    mock_setup_logging.assert_called_once()
    mock_load_urls.assert_called_once()
    mock_logger.error.assert_called_with("An error occurred: Test exception")