# batch_run.py

from lead_scraper import search_linkedin_profiles
from email_guesser import guess_email_formats
import csv

# Sample companies and roles (you can later replace this with CSV reading)
targets = [
    {"company": "Notion", "role": "Product Manager"},
    {"company": "Stripe", "role": "Head of Growth"},
    {"company": "Google", "role": "AI Researcher"},
]

output_data = []

for target in targets:
    company = target["company"]
    role = target["role"]

    print(f"\n--> Searching leads for: {company} | {role}")
    leads = search_linkedin_profiles(company, role)

    for lead in leads:
        email_guesses = guess_email_formats(lead["name"], lead["company"])

        output_data.append({
            "Company": lead["company"],
            "Name": lead["name"],
            "Title": lead["title"],
            "LinkedIn": lead["linkedin"],
            "Email Guesses": ", ".join(email_guesses)
        })

# Save to CSV
with open("leads_output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=output_data[0].keys())
    writer.writeheader()
    writer.writerows(output_data)

print(f"\n--> Done! Leads saved to leads_output.csv")
