
# 🔎 Deep Research Agent (Agentic AI)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)  
An **AI-powered research assistant** that plans searches, gathers information, writes long-form reports, and optionally emails results — all orchestrated through autonomous agents.

---

## ✨ Features
- 📑 **Automated Research Workflow** – enter a topic, get a structured report.  
- 🧠 **Agentic Architecture** – planner, searcher, writer, and emailer agents.  
- 🌐 **Live Web Search** – pulls in up-to-date info via API.  
- 📝 **Multi-page Reports** – 1500+ word dossiers with summaries & follow-up Qs.  
- 📧 **Email Delivery** – send reports straight to your inbox with SendGrid.  
- 🎛 **Interactive UI** – clean Gradio app with streaming progress updates.  

---

## 🏗 Architecture
```
User → Gradio UI → Orchestrator
    → Planner Agent (decides search queries)
    → [Parallel] Search Agents (summarize web results)
    → Writer Agent (long-form markdown report)
    → Email Agent (send HTML email, optional)
    → UI streams status & final dossier
```

Agents are modular — swap models, tools, or add new outputs (Slack, Notion, etc.).

---

## 🚀 Quickstart

### 1. Clone & Install
```bash
git clone https://github.com/yourusername/deep-research-agent.git
cd deep-research-agent

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment
Copy `.env.example` → `.env` and fill in:
```
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_search_key   # or BING_SEARCH_V7_SUBSCRIPTION_KEY=...
SENDGRID_API_KEY=your_sendgrid_key
SENDER_EMAIL=verified@yourdomain.com
RECIPIENT_EMAIL=you@example.com
```

### 3. Run the App
```bash
python research_report_writer.py
```
Gradio will open at [http://localhost:7860](http://localhost:7860). Enter a topic and watch the agents work.

---

## 📂 Project Structure
```
.
├── planner_agent.py         # designs search plan
├── search_agent.py          # executes searches & summaries
├── writer_agent.py          # creates research dossier
├── email_agent.py           # sends results via SendGrid
├── research_manager.py      # orchestrates pipeline
├── research_report_writer.py# Gradio app UI
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🎯 Example
Input:
```
"How will AI agents impact small businesses in the next 2 years?"
```

Output:
- 5 targeted search queries with reasons.  
- Condensed notes from multiple sources.  
- A **~2000 word dossier** in Markdown with:
  - Short executive summary
  - Detailed analysis
  - Suggested follow-up questions  
- (Optional) Delivered to your inbox.

---

## 🛠 Customization
- **Swap Models**: Planner/Writer use `gpt-5`, Searcher uses `gpt-4o-mini`.  
- **Change Output**: Adjust word counts, style, or add HTML/PDF export.  
- **Add Integrations**: Push results to Slack, Notion, Discord, or databases.  
- **Improve Reliability**: Add retries, caching, or fact-checkers.  

---

## 🔒 Security Notes
- Store API keys in `.env`, never commit them.  
- Sanitize any HTML before sending via email.  
- Respect your search provider’s rate limits & ToS.  

---

## 📜 License
MIT License © 2025 – Your Name
