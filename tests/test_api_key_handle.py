from weather_api.utils import get_api_key, destroy_api_key
import os


def test_get_api_key_from_env_variable(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "test_api_key")
    assert get_api_key() == "test_api_key"


def test_get_api_key_from_user_input(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "")
    monkeypatch.setattr('getpass.getpass', (lambda prompt: 'user_input_api_key'))
    assert get_api_key() == "user_input_api_key"


def test_destroy_api_key(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "test_api_key")
    assert "OPENWEATHER_API_KEY" in os.environ

    destroy_api_key()

    assert "OPENWEATHER_API_KEY" not in os.environ