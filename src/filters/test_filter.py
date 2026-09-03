from src.filters.job_filter import is_relevant, filter_jobs
from src.models.job import Job


def make_job(title):
    return Job(
        id="1",
        title=title,
        company="Tech Company",
        location="Atlanta, GA",
        description="Test job",
        salary_min=None,
        salary_max=None,
        url="https://example.com",
        created="2026-09-02T12:00:00Z",
        source="test",
    )


def test_relevant_title():
    assert is_relevant(make_job("Senior Software Engineer")) is True


def test_case_insensitive():
    assert is_relevant(make_job("SOFTWARE DEVELOPER")) is True


def test_irrelevant_title():
    assert is_relevant(make_job("Marketing Manager")) is False


def test_filter_jobs():
    jobs = [
        make_job("Software Engineer"),
        make_job("Marketing Manager"),
        make_job("Python Developer"),
    ]

    relevant_jobs = filter_jobs(jobs)

    assert len(relevant_jobs) == 2
    assert relevant_jobs[0].title == "Software Engineer"
    assert relevant_jobs[1].title == "Python Developer"