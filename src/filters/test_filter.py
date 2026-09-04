from src.filters.job_filter import is_relevant, filter_jobs
from src.models.job import Job
from src.models.user_preferences import UserPreferences


def make_job(title, work_arrangement=None):
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
        work_arrangement=work_arrangement,
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

    assert is_relevant(make_job("Senior Software Engineer", "remote"), preferences) is True


def test_case_insensitive():
    preferences = make_preferences(["software developer"])

    assert is_relevant(make_job("SOFTWARE DEVELOPER", "remote"), preferences) is True


def test_irrelevant_title():
    preferences = make_preferences(["software engineer"])

    assert is_relevant(make_job("Marketing Manager", "remote"), preferences) is False


def test_filter_jobs():
    jobs = [
        make_job("Software Engineer", "remote"),
        make_job("Marketing Manager", "remote"),
        make_job("Python Developer", "remote"),
    ]

    preferences = make_preferences(["software engineer", "python developer"])
    relevant_jobs = filter_jobs(jobs, preferences)

    assert len(relevant_jobs) == 2
    assert relevant_jobs[0].title == "Software Engineer"
    assert relevant_jobs[1].title == "Python Developer"

def test_remote_arrangement():
    preferences = make_preferences(["software engineer"])
    job = make_job("Software Engineer", "remote")

    assert is_relevant(job, preferences) is True


def test_hybrid_arrangement():
    preferences = UserPreferences(
        desired_roles=["software engineer"],
        work_arrangements=["remote", "hybrid"],
        location=None,
        max_commute_minutes=None,
        employment_types=["full-time"],
    )

    job = make_job("Software Engineer", "hybrid")

    assert is_relevant(job, preferences) is True


def test_onsite_arrangement():
    preferences = make_preferences(["software engineer"])
    job = make_job("Software Engineer", "onsite")

    assert is_relevant(job, preferences) is False


def test_unknown_arrangement():
    preferences = make_preferences(["software engineer"])
    job = make_job("Software Engineer")

    assert is_relevant(job, preferences) is False