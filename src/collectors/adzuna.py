from dotenv import load_dotenv
import os  
import httpx

load_dotenv()
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

def get_jobs():
    response = httpx.get(
        "https://api.adzuna.com/v1/api/jobs/us/search/1",
        params={
            "app_id": ADZUNA_APP_ID,
            "app_key": ADZUNA_APP_KEY,
            "results_per_page": 50,
            "what": "python developer",
            "where": "Atlanta",
        },
    )
    data = response.json()
    return data.get("results", [])
    
if __name__ == "__main__":
    jobs = get_jobs()
    print(len(jobs))
    print(jobs[0])