from src.filters.job_filter import is_relevant, filter_jobs
from src.models.job import Job
from src.models.user_preferences import UserPreferences


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

def make_preferences(roles):
    return UserPreferences(
        desired_roles=roles,
        work_arrangements=["remote"],
        location=None,
        max_commute_minutes=None,
        employment_types=["full-time"],
    )


def test_relevant_title():
    preferences = make_preferences(["software engineer"])

    assert is_relevant(make_job("Senior Software Engineer"), preferences) is True


def test_case_insensitive():
    preferences = make_preferences(["software developer"])

    assert is_relevant(make_job("SOFTWARE DEVELOPER"), preferences) is True


def test_irrelevant_title():
    preferences = make_preferences(["software engineer"])

    assert is_relevant(make_job("Marketing Manager"), preferences) is False


def test_filter_jobs():
    jobs = [
        make_job("Software Engineer"),
        make_job("Marketing Manager"),
        make_job("Python Developer"),
    ]

    preferences = make_preferences(["software engineer", "python developer"])
    relevant_jobs = filter_jobs(jobs, preferences)

    assert len(relevant_jobs) == 2
    assert relevant_jobs[0].title == "Software Engineer"
    assert relevant_jobs[1].title == "Python Developer"