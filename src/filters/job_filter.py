def is_relevant(job, preferences):
    title = job.title.lower()

    return any(role.lower() in title for role in preferences.desired_roles)

def filter_jobs(jobs, preferences):
    return [job for job in jobs if is_relevant(job, preferences)]