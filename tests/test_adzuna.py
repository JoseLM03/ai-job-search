from src.collectors.adzuna import get_jobs
import httpx

def fake_get(url, params):
    raise httpx.RequestError("Adzuna API not working")

def test_adzuna_request_error(monkeypatch):
    monkeypatch.setattr("httpx.get", fake_get)
    jobs = get_jobs("software engineer", "Atlanta")
    assert jobs == []