from src.filters.role_aliases import ROLE_ALIASES

def matches_role(job, preferences):
    title = job.title.lower()
    all_roles = []
    
    for desired_role in preferences.desired_roles:
        all_roles.extend(ROLE_ALIASES.get(desired_role, [desired_role]))
        
    return any(
        role.lower() in title
        for role in all_roles
    )

def matches_location(job, preferences):
    if not preferences.location:
        return True
    return preferences.location.lower() in job.location.lower()

def is_relevant(job, preferences):
    location_matches = matches_location(job, preferences)

    role_matches = matches_role(job, preferences)

    arrangement_matches = (
        job.work_arrangement in preferences.work_arrangements
    )

    employment_matches = (
    not preferences.employment_types
    or any(
        emp_type in preferences.employment_types
        for emp_type in job.employment_types
    )
)

    return role_matches and arrangement_matches and employment_matches and location_matches

def filter_jobs(jobs, preferences):
    return [job for job in jobs if is_relevant(job, preferences)]