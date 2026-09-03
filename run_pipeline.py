from src.pipeline import get_relevant_jobs

jobs = get_relevant_jobs()

print(f"Found {len(jobs)} relevant jobs:\n")

for job in jobs:
    print(f"{job.title} | {job.company} | {job.location}")