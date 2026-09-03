RELEVANT_TITLE_PHRASES = [
    "software engineer",
    "software developer",
    "backend engineer",
    "backend developer",
    "frontend engineer",
    "frontend developer",
    "full stack engineer",
    "full stack developer",
    "python developer",
    "java developer",
    "ai engineer",
    "ai developer",
]


def is_relevant(job):
    title = job.title.lower()

    return any(phrase in title for phrase in RELEVANT_TITLE_PHRASES)

def filter_jobs(jobs):
    return [job for job in jobs if is_relevant(job)]