from src.normalizers.adzuna import normalize_job


def test_normalize_job():
    raw_job = {
        "id": "123",
        "title": "Python Developer",
        "company": {
            "display_name": "Tech Company"
        },
        "location": {
            "display_name": "Atlanta, GA"
        },
        "description": "Python developer needed.",
        "redirect_url": "https://example.com/job/123",
        "created": "2026-09-02T12:00:00Z",
    }

    job = normalize_job(raw_job)

    assert job.id == "123"
    assert job.title == "Python Developer"
    assert job.company == "Tech Company"
    assert job.location == "Atlanta, GA"
    assert job.salary_min is None
    assert job.salary_max is None
    assert job.source == "adzuna"