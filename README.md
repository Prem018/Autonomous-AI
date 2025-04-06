# Autonomous-AI
Autonomous AI Description

Autonomous AI Agent
A Python-based project that interprets natural language instructions and performs tasks such as fetching AI news headlines, summarizing smartphone reviews, and analyzing renewable energy trends — completely autonomously.

 Features
 AI News Extraction
Retrieves top 5 Artificial Intelligence news headlines from Google News RSS feed.

 Smartphone Review Summarizer
Scrapes top smartphone reviews from TechRadar and summarizes pros and cons.

 Renewable Energy Trend Analysis
Generates and saves trend charts for solar and wind energy using sample data.

 How It Works
User gives a natural language instruction (e.g., "Find top 5 AI headlines and save to file").

The system identifies the relevant task based on keywords.

It calls the appropriate utility module to:

Fetch content (via web scraping or APIs)

Summarize or analyze data

Generate .txt, .pdf, or .png outputs

 Technologies Used
Python

Selenium – Web scraping

Feedparser – RSS feed parsing

Matplotlib – Data visualization

Pandas – Data processing

FPDF – PDF generation

 Folder Structure
bash
Copy
Edit
AI/
│
├── autonomous_agent.py               # Main script
└── utils/
    ├── ai_headlines.py              # AI headlines fetching logic
    ├── smartphone_reviews.py        # Smartphone scraping/summarizing
    └── renewable_trends.py          # Energy trend plotting
 How to Run
Step 1: Install Dependencies
bash
Copy
Edit
pip install selenium feedparser pandas matplotlib fpdf
Step 2: Download ChromeDriver
Make sure you have ChromeDriver installed and added to PATH.
Download ChromeDriver

Step 3: Run the Script
bash
Copy
Edit
python autonomous_agent.py
Step 4: Enter Any of These Instructions
Find top 5 AI headlines and save to file

Search smartphone reviews, extract pros/cons, create summary

Research renewable energy, analyze trends, create PDF with charts

 Output Files
Task	Output
AI Headlines	ai_headlines.txt
Smartphone Reviews	smartphone_summary.txt
Renewable Energy Trends	renewable_trends_chart.png
 Demo Flow
Input instruction.

Task is identified (AI/Smartphone/Energy).

Output is generated and saved.

Logs and messages are printed to confirm success.
