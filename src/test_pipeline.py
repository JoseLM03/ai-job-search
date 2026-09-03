from src.pipeline import get_relevant_jobs


def test_get_relevant_jobs(monkeypatch):
    fake_raw_jobs = [
        {
            "id": "1",
            "title": "Software Engineer",
            "company": {"display_name": "Tech Company"},
            "location": {"display_name": "Atlanta, GA"},
            "description": "Software engineer needed.",
            "redirect_url": "https://example.com/1",
            "created": "2026-09-02T12:00:00Z",
        },
        {
            "id": "2",
            "title": "Marketing Manager",
            "company": {"display_name": "Marketing Company"},
            "location": {"display_name": "Atlanta, GA"},
            "description": "Marketing manager needed.",
            "redirect_url": "https://example.com/2",
            "created": "2026-09-02T12:00:00Z",
        },
    ]

    monkeypatch.setattr(
        "src.pipeline.get_jobs",
        lambda: fake_raw_jobs
    )

    relevant_jobs = get_relevant_jobs()

    assert len(relevant_jobs) == 1
    assert relevant_jobs[0].title == "Software Engineer"
    assert relevant_jobs[0].company == "Tech Company"