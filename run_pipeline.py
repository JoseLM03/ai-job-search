from src.pipeline import get_relevant_jobs
from src.models.user_preferences import UserPreferences
from src.config import get_default_preferences

preferences = get_default_preferences()

jobs = get_relevant_jobs(preferences)

print(f"Found {len(jobs)} relevant jobs:\n")

for job in jobs:
    print(f"{job.title} | {job.company} | {job.location}")