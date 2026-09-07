from src.pipeline import get_relevant_jobs
from src.config import get_default_preferences

preferences = get_default_preferences()

jobs = get_relevant_jobs(preferences)

print(f"Found {len(jobs)} relevant jobs:\n")

for job in jobs:
    print(f"{job.title} | {job.company} | {job.location} | {job.work_arrangement} | {job.salary_min} - {job.salary_max} | {job.employment_types} | {job.url}")