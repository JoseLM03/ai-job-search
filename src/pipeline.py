from src.collectors.adzuna import get_jobs
from src.normalizers.adzuna import normalize_job
from src.filters.job_filter import filter_jobs


def get_relevant_jobs():
    raw_jobs = get_jobs()

    jobs = [normalize_job(raw_job) for raw_job in raw_jobs]

    relevant_jobs = filter_jobs(jobs)

    return relevant_jobs