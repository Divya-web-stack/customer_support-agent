# Bloom Aesthetics Clinic AI Support Agent

A modular Python CLI application that simulates an intelligent customer support assistant for Bloom Aesthetics Clinic. The agent answers questions strictly from the Service Operating Procedures (SOP), qualifies leads, detects escalation scenarios, and generates structured conversation summaries.

## 🎯 Features

- **SOP-Compliant Responses** — Answers strictly from SOP data (no hallucinations)
- **Intelligent Escalation Detection** — Automatically escalates unsupported, medical, or out-of-scope requests
- **Lead Qualification** — Collects customer information after 3 successful interactions
- **Conversation Logging** — Maintains detailed logs of all interactions with timestamps
- **Structured Summaries** — Generates professional conversation summaries
- **Modular Multi-Agent Architecture** — Clean separation of concerns with specialized agents
- **CLI Interface** — User-friendly command-line interaction
- **OpenRouter Integration** — Flexible AI model switching via OpenRouter API

## 📋 Prerequisites

- Python 3.8+
- OpenRouter API key ([Get one here](https://openrouter.ai/))

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd ai_support_agent
```

### 2. Create a Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_api_key_here
```

## 🚀 Running the Application

```bash
python app.py
```

The application will start an interactive CLI session. Type your questions and the AI agent will respond based on the SOP data.

To exit, type `exit` or `quit`.

## 📁 Project Structure

```
ai_support_agent/
├── app.py                      # Main CLI application
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── .gitignore                 # Git ignore rules
├── README.md                  # This file
├── sop_data.json             # SOP knowledge base
├── agents/
│   ├── faq_agent.py          # FAQ answering logic
│   ├── qualification_agent.py # Lead qualification
│   ├── escalation_agent.py    # Escalation detection
│   └── summary_agent.py       # Summary generation
├── utils/
│   ├── logger.py             # Conversation logging
│   ├── memory.py             # Session memory management
│   └── prompts.py            # System prompts & questions
├── logs/
│   └── conversation_log.txt  # Conversation history
└── test_transcripts/
    ├── qualification.md
    ├── escalation.md
    ├── faq.md
    ├── out_of_scope.md
    └── summary.md
```

## 🤖 How It Works

### Conversation Flow
1. **Customer Input** → User enters a question
2. **FAQ Agent** → Searches SOP for matching answer
3. **Escalation Check** → Detects if escalation is needed
4. **Response** → Answers customer or escalates
5. **Count Tracking** → After 3 successful interactions, triggers qualification
6. **Lead Qualification** → Collects customer information
7. **Summary** → Generates and logs conversation summary

### Agent Architecture

- **FAQAgent** — Matches questions against SOP; uses OpenRouter API for semantic matching
- **QualificationAgent** — Asks qualifying questions and stores lead information
- **EscalationAgent** — Detects out-of-scope, medical, or angry requests
- **SummaryAgent** — Generates structured conversation summaries

## 📝 SOP Data Format

The `sop_data.json` file should follow this structure:

```json
{
  "faqs": [
    {
      "q": "What are your clinic hours?",
      "a": "Our clinic is open from 9am to 6pm, Monday to Saturday."
    },
    {
      "q": "How can I book an appointment?",
      "a": "Please call us at 555-1234 or visit our website."
    }
  ]
}
```

## 📊 Conversation Logs

All conversations are logged to `logs/conversation_log.txt` with timestamps. Each interaction is recorded for quality assurance and analytics.

Example log entry:
```
[2026-05-24 10:30:45] Customer: What are your clinic hours?
[2026-05-24 10:30:45] AI: Our clinic is open from 9am to 6pm, Monday to Saturday.
```

## 🔒 Security Notes

- **API Key Security** — Store your OpenRouter API key in `.env`, never commit it
- **SOP Compliance** — The agent only uses information from `sop_data.json`
- **Data Privacy** — Logs are stored locally; ensure proper data handling per GDPR/regulations

## ⚠️ Limitations

- Responses are only as accurate as the SOP data
- No persistent database (uses in-memory session memory)
- No web or GUI interface
- Requires active internet connection for OpenRouter API calls
- Single-threaded (one conversation at a time)

## 🐛 Troubleshooting

### API Key Not Found
- Ensure `.env` file exists in the project root
- Check that `OPENROUTER_API_KEY` is set correctly
- Verify the API key is valid on OpenRouter

### Conversations Not Logging
- Ensure `logs/` directory exists
- Check file permissions for `logs/conversation_log.txt`
- Verify logger is initialized in `app.py`

### SOP Not Matching
- Verify `sop_data.json` contains the expected Q&A pairs
- Check for typos or case-sensitivity issues
- Ensure JSON is valid (use `jsonlint` if needed)

## 🚀 Future Improvements

- [ ] Multi-turn conversation history
- [ ] Sentiment analysis
- [ ] Custom escalation rules
- [ ] Web interface (Flask/FastAPI)
- [ ] Database integration
- [ ] Multi-language support
- [ ] Performance analytics dashboard

## 📄 License

This project is proprietary software for Bloom Aesthetics Clinic.

## 👤 Author

AI Internship Project

## 📧 Support

For issues or questions, please contact the development team.

---

**Last Updated:** May 2026

- Vector database for large SOP retrieval
- Multi-channel integrations (WhatsApp/email)
- RAG pipeline
- Human-in-the-loop review dashboard
- Persistent customer memory
