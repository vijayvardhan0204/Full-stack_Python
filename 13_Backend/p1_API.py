import requests

location = input("Enter location: ").strip()
industry = input("Enter industry: ").strip()

url = "https://jobicy.com/api/v2/remote-jobs"
params = {
    "count": 20,
    "geo": location,
    "industry": industry
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()   # raises error for 4xx / 5xx

    data = response.json()
    jobs = data.get("jobs", [])

    if not jobs:
        print("No jobs found.")
    else:
        for i, job in enumerate(jobs, start=1):
            print(f"{i}. {job.get('jobTitle')} - {job.get('jobGeo')}")

except requests.exceptions.RequestException as e:
    print("Error fetching jobs:", e)
