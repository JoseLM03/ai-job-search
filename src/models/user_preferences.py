from dataclasses import dataclass


@dataclass
class UserPreferences:
    desired_roles: list[str]
    work_arrangements: list[str]
    location: str | None
    max_commute_minutes: int | None
    employment_types: list[str]