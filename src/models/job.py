from dataclasses import dataclass, field
@dataclass

class Job:
    id: str
    title: str
    company: str
    location: str
    description: str
    salary_min: float | None
    salary_max: float | None
    url: str
    created: str
    source: str
    work_arrangement: str | None = None
    employment_types: list[str] = field(default_factory=list)
