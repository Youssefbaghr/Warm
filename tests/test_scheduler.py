import pytest
from unittest.mock import patch, MagicMock
from src.scheduler import start_scheduler, run_scheduler

@patch('src.scheduler.Config.RUN_INTERVAL', 60)
@patch('src.scheduler.schedule.every')
@patch('src.scheduler.run_ping_all_apis')
@patch('src.scheduler.run_scheduler')
def test_start_scheduler(mock_run_scheduler, mock_run_ping, mock_schedule):
    start_scheduler(test_mode=True)

    mock_schedule.assert_called_once_with(60)
    mock_schedule.return_value.minutes.do.assert_called_once_with(mock_run_ping)
    mock_run_ping.assert_called_once()
    assert mock_run_scheduler.call_count == 3

@patch('src.scheduler.schedule.run_pending')
@patch('src.scheduler.time.sleep')
def test_run_scheduler(mock_sleep, mock_run_pending):
    run_scheduler()
    mock_run_pending.assert_called_once()
    mock_sleep.assert_called_once_with(1)