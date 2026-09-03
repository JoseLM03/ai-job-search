from src.models.job import Job


def normalize_job(raw_job):
    return Job(
        id=raw_job["id"],
        title=raw_job["title"],
        company=raw_job["company"]["display_name"],
        location=raw_job["location"]["display_name"],
        description=raw_job["description"],
        salary_min=raw_job.get("salary_min"),
        salary_max=raw_job.get("salary_max"),
        url=raw_job["redirect_url"],
        created=raw_job["created"],
        source="adzuna",
    )