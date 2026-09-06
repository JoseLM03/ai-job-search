from src.models.user_preferences import UserPreferences

def get_default_preferences():
    return UserPreferences(
        desired_roles=["software engineer"],
        work_arrangements=["remote"],
        location=None,
        max_commute_minutes=None,
        employment_types=["full-time"],
    )