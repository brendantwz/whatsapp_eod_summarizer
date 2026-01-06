# WhatsApp EOD Report Generator

**Transform messy WhatsApp group chats into professional end-of-day construction reports using AI.**

---

## 🎯 What This Does

**Input**: Raw WhatsApp chat export (.txt file)
```
07/10/2025, 15:13 - John: Foundation pour delayed by rain
07/10/2025, 16:30 - Sarah: Steel delivery confirmed for tomorrow
...
```

**Output**: Structured markdown report (1 page, 6 sections)
```markdown
## Site: Construction Site Alpha
## Date: 07/10/2025

### 1. Overall Site Status
Work progressed despite weather delays...

### 2. Work Completed Today
- Steel reinforcement installation completed
- Site preparation for foundation pour

### 3. Issues / Delays
- Foundation pour delayed due to heavy rain

### 4. Risks / Attention Required
- **Weather forecast shows continued rain** (critical)

### 5. Tomorrow's Planned Work
- Steel delivery at 9:00 AM
- Resume foundation work if weather permits

### 6. Decisions Needed
- Approve alternative waterproofing method
```

---

## ⚡ Quick Start (5 Minutes)

### **👉 [START_HERE.md](START_HERE.md) - Complete Setup Guide**

Follow these simple steps:
1. Install dependencies (`pip install`)
2. Choose AI provider (Anthropic, OpenAI, or OpenRouter)
3. Set API key (copy-paste command)
4. Verify setup (`check_setup.py`)
5. Generate your first report!

---

## 📦 What's Included

### Core Scripts
- **`generate_report.py`** ⭐ - **USE THIS ONE** - Complete pipeline (parse + summarize)
- `parser.py` - Message extraction engine
- `summarizer.py` - AI-powered report generation
- `run.py` - Parse-only mode (for validation)
- `check_setup.py` - Environment verification tool

### Documentation
- **`START_HERE.md`** ⭐ - Quick setup guide (start here!)
- `README.md` - This file (project overview)
- `SETUP.md` - Detailed setup & troubleshooting
- `docs/` - Additional guides and examples

---

## 🚀 Daily Usage

### The ONE Command You Need

```bash
python generate_report.py "input/your-chat.txt" "Your Site Name"
```

That's it! This does everything:
- ✅ Parses WhatsApp messages
- ✅ Filters system messages
- ✅ Cleans Unicode artifacts
- ✅ Sends to AI for analysis
- ✅ Generates structured report
- ✅ Saves both JSON and Markdown

**Output files:**
- `output/your-chat_parsed.json` - Clean data
- `output/your-chat_eod_report.md` - Final report

---

## 🤖 AI Provider Options

| Provider | Cost/Report | Best For | Get API Key |
|----------|------------|----------|-------------|
| **Anthropic Claude** | $0.05 | Quality & reliability | [console.anthropic.com](https://console.anthropic.com/) |
| **OpenAI GPT-4** | $0.04 | Familiarity with ChatGPT | [platform.openai.com](https://platform.openai.com/) |
| **OpenRouter** 🆕 | $0.03-0.08 | 100+ models in one API | [openrouter.ai/keys](https://openrouter.ai/keys) |

---

## 📊 Report Structure (Always Consistent)

Every report follows this exact structure:

```markdown
## Site: {site_name}
## Date: {date}

### 1. Overall Site Status
[Executive summary paragraph]

### 2. Work Completed Today
- Concrete deliverables

### 3. Issues / Delays
- Problems identified

### 4. Risks / Attention Required
- **Critical items in bold**
- Management attention needed

### 5. Tomorrow's Planned Work
- Scheduled activities

### 6. Decisions Needed
- Awaiting approvals
```

**Features:**
- ✅ Professional executive tone
- ✅ Maximum 1 page length
- ✅ Facts extracted from messages (no hallucinations)
- ✅ Similar updates grouped logically
- ✅ Risks and delays highlighted clearly

---

## 📁 Project Structure

```
whatsapp-eod/
├── START_HERE.md           ⭐ Begin here for setup
├── README.md               📄 This file (overview)
├── SETUP.md                📖 Detailed setup guide
│
├── generate_report.py      ⭐ Main script (use this!)
├── parser.py               🔧 Message extraction
├── summarizer.py           🤖 AI report generation
├── run.py                  🔍 Parse-only mode
├── check_setup.py          ✓  Setup verification
├── requirements.txt        📦 Python dependencies
│
├── input/                  📥 Put WhatsApp .txt files here
├── output/                 📤 Generated reports go here
└── docs/                   📚 Additional documentation
    ├── QUICK_REFERENCE.md
    ├── EXAMPLE_REPORT.md
    ├── PROJECT_SUMMARY.md
    └── WORKFLOW.md
```

---

## 🎓 When to Use Each Script

### 99% of the time: `generate_report.py`
```bash
python generate_report.py "input/chat.txt" "Site Name"
```
**Does everything:** Parse → Validate → AI Summarize → Save

### When you want to check parsing quality first: `run.py`
```bash
python run.py "input/chat.txt"
# Review the parsed JSON
# Then run summarizer if it looks good
python summarizer.py "output/chat_parsed.json" "Site Name"
```

### When something isn't working: `check_setup.py`
```bash
python check_setup.py
# Shows what's configured correctly and what needs fixing
```

---

## 🔧 API Configuration (Where to Update)

All API-related code is in **`summarizer.py`**:

### Lines 14-25: API Key Configuration
```python
AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic")

if AI_PROVIDER == "anthropic":
    API_KEY = os.getenv("ANTHROPIC_API_KEY")  # ← Update here
elif AI_PROVIDER == "openai":
    API_KEY = os.getenv("OPENAI_API_KEY")     # ← Or here
elif AI_PROVIDER == "openrouter":
    API_KEY = os.getenv("OPENROUTER_API_KEY")  # ← Or here
```

### Lines 106-197: AI Functions
- **Line 106**: `summarize_with_anthropic()` - Claude API
- **Line 136**: `summarize_with_openai()` - GPT-4 API
- **Line 168**: `summarize_with_openrouter()` - OpenRouter API (NEW!)

**To change model**, edit the `model` parameter in these functions.

---

## ✅ Features & Validation

### Parser Features
- ✅ Extracts timestamp, sender, message
- ✅ Filters system messages (group changes, encryption notices)
- ✅ Cleans Unicode artifacts (WhatsApp formatting)
- ✅ Handles multi-line messages correctly
- ✅ Windows/Mac/Linux compatible

### Summarizer Features
- ✅ Three AI providers (Anthropic, OpenAI, OpenRouter)
- ✅ Fact-grounded (no hallucinations)
- ✅ Structured 6-section format
- ✅ Executive professional tone
- ✅ Risk highlighting (bold critical items)
- ✅ Length control (1 page max)

### Quality Gates
- ✅ Preview first 10 messages
- ✅ No crashes (robust error handling)
- ✅ Clean output (no garbage)
- ✅ Validation with real data (149 messages from 235 lines)

---

## 💰 Cost Estimates

**For typical daily chat (200 messages ≈ 5000 tokens):**

| Provider | Per Report | 100 Reports | Annual (Daily) |
|----------|-----------|-------------|----------------|
| Claude 3.5 Sonnet | $0.05 | $5/month | $60/year |
| GPT-4o | $0.04 | $4/month | $48/year |
| OpenRouter | $0.03-0.08 | $3-8/month | $36-96/year |

**Note:** All providers offer free trial credits for new users!

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **START_HERE.md** | 5-minute setup guide (begin here!) |
| **README.md** | Project overview (this file) |
| **SETUP.md** | Detailed setup & troubleshooting |
| **docs/QUICK_REFERENCE.md** | Command cheat sheet |
| **docs/EXAMPLE_REPORT.md** | Sample output |
| **docs/PROJECT_SUMMARY.md** | Complete project details |
| **docs/WORKFLOW.md** | Visual workflow diagrams |

---

## 🆘 Troubleshooting

### Quick Fixes

**"API key not set"**
```bash
# Re-run the appropriate command from START_HERE.md Step 3
$env:ANTHROPIC_API_KEY='your-key'  # Windows
export ANTHROPIC_API_KEY='your-key'  # Mac/Linux
```

**"Package not installed"**
```bash
pip install -r requirements.txt
```

**"No messages parsed"**
- Verify WhatsApp export is in standard format
- Check file contains actual messages, not just system notifications

**Still stuck?**
```bash
python check_setup.py  # Diagnoses common issues
```

See `SETUP.md` for detailed troubleshooting.

---

## 🎯 Remember

**The only command you need:**
```bash
python generate_report.py "input/chat.txt" "Site Name"
```

**The only file you need to edit (for API config):**
```
summarizer.py (lines 14-25 for API keys, lines 106-197 for models)
```

**The guide to start with:**
```
START_HERE.md
```

---

## 📞 Support

- **Setup issues**: See `START_HERE.md`
- **Detailed config**: See `SETUP.md`
- **Command syntax**: See `docs/QUICK_REFERENCE.md`
- **Sample output**: See `docs/EXAMPLE_REPORT.md`

---

**Status**: ✅ Production Ready | 🚀 Updated with OpenRouter Support

**Last Updated**: 2026-01-06 | **Version**: 2.0
