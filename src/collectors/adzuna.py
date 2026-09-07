from dotenv import load_dotenv
import os  
import httpx

load_dotenv()
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")

def get_jobs(title, location):
    try:
        response = httpx.get(
            "https://api.adzuna.com/v1/api/jobs/us/search/1",
        params={
            "app_id": ADZUNA_APP_ID,
            "app_key": ADZUNA_APP_KEY,
            "results_per_page": 50,
            "what": title,
            "where": location,
            },
        )
        data = response.json()
        return data.get("results", [])
    except httpx.RequestError as e:
        print(f"An error occurred while requesting Adzuna API: {e}")
        return []
    
if __name__ == "__main__":
    jobs = get_jobs("software engineer", "Atlanta")
    print(len(jobs))
    print(jobs[0])