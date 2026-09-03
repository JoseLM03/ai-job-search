from dotenv import load_dotenv
import httpx
import os

load_dotenv()
app_id = os.getenv("ADZUNA_APP_ID")
app_key = os.getenv("ADZUNA_APP_KEY")

response = httpx.get(
    "https://api.adzuna.com/v1/api/jobs/us/search/1",
    params={
        "app_id": app_id,
        "app_key": app_key,
        "what": "software engineer",
        "where": "Atlanta",
        "results_per_page": 10
    }
)

data = response.json()
print(data["count"])

for job in data["results"]:
    print(job["title"])