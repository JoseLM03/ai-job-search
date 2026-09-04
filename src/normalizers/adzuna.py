from src.models.job import Job

def extract_work_arrangement(description):
    description_lower = description.lower()
    
    if "hybrid" in description_lower:
        return "hybrid"
    elif "remote" in description_lower:
        return "remote"
    elif "on-site" in description_lower or "onsite" in description_lower:
        return "onsite"
    return None

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
        work_arrangement=extract_work_arrangement(raw_job["description"]),
    )