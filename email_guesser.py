# email_guesser.py

import re

# Sample mapping of company names to domains
DOMAIN_MAP = {
    "Google": "google.com",
    "Notion": "notion.so",
    "Stripe": "stripe.com",
    "Netflix": "netflix.com",
    "Apple": "apple.com",
    "Microsoft": "microsoft.com",
    "Amazon": "amazon.com"
}

def normalize_name(name):
    parts = name.strip().split()
    if len(parts) == 0:
        return "", ""
    if len(parts) == 1:
        return parts[0].lower(), ""
    return parts[0].lower(), parts[-1].lower()


def guess_email_formats(name, company):
    first, last = normalize_name(name)
    domain = DOMAIN_MAP.get(company, f"{company.lower()}.com")

    guesses = []

    if first and last:
        guesses = [
            f"{first}.{last}@{domain}",
            f"{first}{last}@{domain}",
            f"{first}@{domain}",
            f"{first[0]}{last}@{domain}",
            f"{first[0]}.{last}@{domain}",
        ]
    elif first:
        guesses = [f"{first}@{domain}"]

    return guesses


if __name__ == "__main__":
    # Test
    results = guess_email_formats("Joemer R.", "Google")
    for email in results:
        print(email)
 
