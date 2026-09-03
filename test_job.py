from src.normalizers.adzuna import normalize_job
from src.models.job import Job
from src.collectors.adzuna import get_jobs

job = Job(
    id="123",
    title="Python Developer",
    company="Tech Company",
    location="Atlanta, GA",
    description="We are looking for a skilled Python Developer to join our team.",
    salary_min=80000.0,
    salary_max=120000.0,
    url="https://www.example.com/job/123",
    created="2023-10-01T12:00:00Z",
    source="Adzuna"
)

print(job)

raw_jobs = get_jobs()
raw_job = raw_jobs[0]  # Get the first job from the list of raw jobs
normalized_job = normalize_job(raw_job)
print(normalized_job)