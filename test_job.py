from src.models.job import Job

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