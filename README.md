# Caprae LeadGen Tool

A lightweight CLI tool to extract professional leads using Google Search and SerpAPI. Built in under 5 hours for Caprae Capital's intern selection task, this tool enables batch lead scraping from LinkedIn search results and predicts professional email addresses using common formats.

---

## Project Summary

This project replicates and enhances aspects of [saasquatchleads.com](https://www.saasquatchleads.com) by focusing on one core feature: **role + company-based lead extraction**. It uses Google dorks to query public LinkedIn profiles and returns a list of high-intent prospects, with guessed emails for outreach.

---

## Features

-  Google Search-based LinkedIn profile extraction (via SerpAPI)
-  Batch mode: Load multiple roles + company names from CSV
-  Heuristic email guesser using patterns like `{first}.{last}@domain.com`
-  Outputs clean `.csv` with: Name, Title, Company, LinkedIn, Email
-  Uses `.env` to manage SerpAPI keys securely

---

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/caprae-leadgen.git
cd caprae-leadgen
```

### 2. Install Dependencies

Make sure you have Python 3.10+ installed. Then install required libraries:

```bash
pip install -r requirements.txt
```

### 3. Add Your SerpAPI Key

Create a `.env` file in the project root:

```
SERPAPI_KEY=your_serpapi_key_here
```

>  Get your free API key from [serpapi.com](https://serpapi.com/).

---

### 4. Prepare Your Input CSV

Create a file named `leads_input.csv` with the following format:

```csv
company,role
Google,Software Engineer
McKinsey,Data Analyst
Bain,Private Equity Analyst
...
```

---

### 5. Run the Tool

Use this command to start batch lead scraping:

```bash
python batch_run.py
```

The script will:
- Perform Google searches for each (company, role) pair
- Extract name, title, LinkedIn URL
- Guess likely email using basic patterns
- Save everything into `leads_output.csv`

---

### 6. Output Example

```csv
company,role,name,title,linkedin,email
Google,Software Engineer,John Lam,Software Engineer,https://www.linkedin.com/in/johnhlam,john.lam@google.com
McKinsey,Data Analyst,Jane Smith,Data Analyst,https://www.linkedin.com/in/janesmith,jane.smith@mckinsey.com
```

---

### Notes & Tips

- You can adjust the number of leads per query in `lead_scraper.py` (`num_results`).
- Avoid rapid repeated calls — SerpAPI has rate limits.
- If a lead’s name is incomplete or unusual, the email guess may be off.

---

## Report

The design rationale, decisions, limitations, and evaluation are included in [`report.pdf`](./report.pdf).

---

## Optional Demo

A short walkthrough video explaining usage and design intent is included (`video.mp4` or shared via Drive).

---

## Built With

- Python 3.10+
- SerpAPI (Google Search API)
- `dotenv`, `requests`, `csv`

---

## Author

Armaan Pratik Pasayat  
[LinkedIn](https://www.linkedin.com/in/armaan-pratik-pasayat-59a214358)

---

## License

MIT License 
