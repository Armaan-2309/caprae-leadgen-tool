# lead_scraper.py

import requests

import os
from dotenv import load_dotenv

load_dotenv() 
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_linkedin_profiles(company, role, num_results=3):
    query = f'site:linkedin.com/in "{role}" "{company}"'
    url = "https://serpapi.com/search"

    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }

    
    response = requests.get(url, params=params)
    data = response.json()

    leads = []
    for result in data.get("organic_results", []):
        link = result.get("link")
        snippet = result.get("snippet", "")
        title = result.get("title", "")

        name = title.split(" - ")[0] if " - " in title else title
        role_found = title.split(" - ")[1] if " - " in title else ""

        leads.append({
            "company": company,
            "name": name,
            "title": role_found,
            "linkedin": link
        })

    return leads


if __name__ == "__main__":
    test_results = search_linkedin_profiles("Google", "Software Engineer")
    
    import json
    print(json.dumps(test_results, indent=2))

