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

def extract_employment_types(raw_job):
    employment_types = []
    contract_time = raw_job.get("contract_time")
    contract_type = raw_job.get("contract_type")
    if contract_time == "full_time":
        employment_types.append("full-time")
    elif contract_time == "part_time":
        employment_types.append("part-time")
    if contract_type == "contract":
        employment_types.append("contract")
    elif contract_type == "temporary":
        employment_types.append("temporary")
    return employment_types

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
        employment_types=extract_employment_types(raw_job),
    )