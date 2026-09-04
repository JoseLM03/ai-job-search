from src.normalizers.adzuna import normalize_job
from src.normalizers.adzuna import extract_work_arrangement
from src.normalizers.adzuna import extract_employment_type

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
        "description": "Python developer needed. This is a hybrid position.",
        "redirect_url": "https://example.com/job/123",
        "created": "2026-09-02T12:00:00Z",
        "contract_time": "full_time",
    }

    job = normalize_job(raw_job)
    assert job.employment_type == "full-time"
    assert job.work_arrangement == "hybrid"
    assert job.id == "123"
    assert job.title == "Python Developer"
    assert job.company == "Tech Company"
    assert job.location == "Atlanta, GA"
    assert job.salary_min is None
    assert job.salary_max is None
    assert job.source == "adzuna"
    assert extract_work_arrangement("This is a hybrid position.") == "hybrid"
    assert extract_work_arrangement("This is a fully remote position.") == "remote"
    assert extract_work_arrangement("Employees must work onsite") == "onsite"
    assert extract_work_arrangement("Great opportunity with competitive benefits.") is None
    assert extract_work_arrangement("This is a hybrid position with remote flexibility.") == "hybrid"
    assert extract_employment_type({"contract_time": "full_time"}) == "full-time"
    assert extract_employment_type({"contract_time": "part_time"}) == "part-time"
    assert extract_employment_type({"contract_type": "contract"}) == "contract"
    assert extract_employment_type({"contract_type": "temporary"}) == "temporary"
    assert extract_employment_type({"contract_time": "internship"}) is None
