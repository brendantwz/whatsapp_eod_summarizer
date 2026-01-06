# WhatsApp EOD Report Generator

**Transform WhatsApp group chats into professional end-of-day construction reports using AI.**

---

## 🚀 Quick Start (5 Minutes)

### 1. Install Dependencies
```bash
pip install -r engine/requirements.txt
```

### 2. Choose AI Provider & Set API Key

**Pick ONE option:**

#### Option A: Anthropic Claude (Recommended)
```powershell
# Windows PowerShell
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='sk-ant-your-key-here'

# Mac/Linux
export AI_PROVIDER=anthropic
export ANTHROPIC_API_KEY='sk-ant-your-key-here'
```
- **Cost**: $0.05/report
- **Get key**: https://console.anthropic.com/

#### Option B: OpenAI GPT-4
```powershell
# Windows PowerShell
$env:AI_PROVIDER='openai'
$env:OPENAI_API_KEY='sk-your-key-here'

# Mac/Linux
export AI_PROVIDER=openai
export OPENAI_API_KEY='sk-your-key-here'
```
- **Cost**: $0.04/report
- **Get key**: https://platform.openai.com/

#### Option C: OpenRouter (100+ Models)
```powershell
# Windows PowerShell
$env:AI_PROVIDER='openrouter'
$env:OPENROUTER_API_KEY='sk-or-your-key-here'

# Mac/Linux
export AI_PROVIDER=openrouter
export OPENROUTER_API_KEY='sk-or-your-key-here'
```
- **Cost**: $0.03-0.08/report
- **Models**: Claude, GPT-4, Gemini, Llama, and more
- **Get key**: https://openrouter.ai/keys

### 3. Verify Setup
```bash
python scripts/check_setup.py
```

### 4. Generate Your First Report
```bash
python scripts/generate_report.py "input/Netcore & Convx - QSR Team - test text.txt" "Test Site"
```

---

## 📦 Daily Usage

### The ONE Command You Need
```bash
python scripts/generate_report.py "input/your-chat.txt" "Your Site Name"
```

**Output:**
- `output/your-chat_parsed.json` (clean data)
- `output/your-chat_eod_report.md` (professional report)

---

## 📁 Project Structure

```
whatsapp-eod/
├── README.md              ← You are here (complete guide)
├── SETUP.md               ← Troubleshooting only
│
├── scripts/               ⚙️ Scripts you run
│   ├── generate_report.py ← Main script (use this!)
│   ├── run.py             ← Parse only (validation)
│   └── check_setup.py     ← Verify environment
│
├── engine/                🔧 Core functionality
│   ├── parser.py          ← Message extraction
│   ├── summarizer.py      ← AI integration (API config here)
│   └── requirements.txt   ← Dependencies
│
├── input/                 ← Put WhatsApp .txt files here
├── output/                ← Generated reports appear here
└── docs/                  ← Reference documentation
```

---

## 🔧 Which Script to Use

| Script | Purpose | When to Use |
|--------|---------|-------------|
| **generate_report.py** | Complete pipeline | **99% of the time** |
| run.py | Parse only (no AI) | Check parsing quality first |
| check_setup.py | Verify environment | Troubleshooting |

### Main Script: generate_report.py
```bash
python scripts/generate_report.py "input/chat.txt" "Site Name"
```
- Parses WhatsApp messages
- Cleans and validates
- AI summarization
- Saves JSON + Markdown report

### Parse Only: run.py
```bash
python scripts/run.py "input/chat.txt"
# Review: output/chat_parsed.json
# Then if good:
python engine/summarizer.py "output/chat_parsed.json" "Site Name"
```

### Diagnostics: check_setup.py
```bash
python scripts/check_setup.py
```
Shows what's configured correctly and what needs fixing.

---

## 🤖 AI Configuration

**All API settings are in ONE file: `engine/summarizer.py`**

### Lines 14-25: API Key Configuration
```python
AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic")

if AI_PROVIDER == "anthropic":
    API_KEY = os.getenv("ANTHROPIC_API_KEY")     # ← Line 18
elif AI_PROVIDER == "openai":
    API_KEY = os.getenv("OPENAI_API_KEY")        # ← Line 20
elif AI_PROVIDER == "openrouter":
    API_KEY = os.getenv("OPENROUTER_API_KEY")    # ← Line 22
```

### Lines 106-197: AI Provider Functions

| Lines | Function | Provider | Change Model |
|-------|----------|----------|--------------|
| 106-133 | `summarize_with_anthropic()` | Claude | Edit line 106 |
| 136-165 | `summarize_with_openai()` | GPT-4 | Edit line 136 |
| 168-197 | `summarize_with_openrouter()` | OpenRouter | Edit line 168 |

**To change AI model:**
1. Open `engine/summarizer.py`
2. Go to the appropriate line (106, 136, or 168)
3. Edit the `model=` parameter

**OpenRouter model examples (line 168):**
```python
model="anthropic/claude-3.5-sonnet"  # Claude
model="openai/gpt-4"                  # GPT-4
model="google/gemini-pro"             # Gemini
model="meta-llama/llama-3-70b"       # Llama 3
```

---

## 📊 Report Structure (Always Consistent)

Every report follows this exact format:

```markdown
## Site: {site_name}
## Date: {date}

### 1. Overall Site Status
[Executive summary paragraph]

### 2. Work Completed Today
- Bullet points of achievements

### 3. Issues / Delays
- Problems and blockers

### 4. Risks / Attention Required
- **Critical items in bold**

### 5. Tomorrow's Planned Work
- Scheduled activities

### 6. Decisions Needed
- Awaiting approvals
```

---

## 📱 How to Export WhatsApp Chat

1. Open WhatsApp → Go to group chat
2. Tap ⋮ (Menu) → **More** → **Export chat**
3. Choose **Without media**
4. Save the .txt file
5. Move to `input/` folder
6. Run: `python scripts/generate_report.py "input/file.txt" "Site Name"`

---

## ⚙️ Features

### Parser
- ✅ Extracts timestamp, sender, message
- ✅ Filters system messages
- ✅ Cleans Unicode artifacts
- ✅ Handles multi-line messages
- ✅ Cross-platform (Windows/Mac/Linux)

### Summarizer
- ✅ 3 AI providers (Anthropic, OpenAI, OpenRouter)
- ✅ No hallucinations (fact-grounded)
- ✅ Professional executive tone
- ✅ Risk highlighting (bold critical items)
- ✅ 1-page length control

---

## 💰 Cost Estimates

**Per typical report (~200 messages):**

| Provider | Per Report | 100 Reports/Month |
|----------|-----------|-------------------|
| Claude 3.5 Sonnet | $0.05 | $5 |
| GPT-4o | $0.04 | $4 |
| OpenRouter | $0.03-0.08 | $3-8 |

All providers offer free trial credits!

---

## 🆘 Troubleshooting

### Quick Fixes

**"API key not set"**
```bash
# Re-run the appropriate command from Quick Start Step 2
```

**"Package not installed"**
```bash
pip install -r engine/requirements.txt
```

**"No messages parsed"**
- Verify WhatsApp export is in standard format
- Check file contains actual messages

**Still stuck?**
```bash
python scripts/check_setup.py  # Diagnoses issues
```

**For detailed troubleshooting**: See `SETUP.md`

---

## 📚 Additional Documentation

- **SETUP.md** - Detailed troubleshooting guide
- **docs/** - Reference materials (examples, technical details)

---

## ✅ Validation

Tested with real WhatsApp data:
- **Input**: 235 lines (raw export)
- **Parsed**: 149 clean messages
- **Success rate**: 100%
- **No crashes**: Robust error handling

---

## 🎯 Remember

**The one command you need:**
```bash
python scripts/generate_report.py "input/chat.txt" "Site Name"
```

**API config location:**
```
engine/summarizer.py (lines 14-197)
```

**Need help?**
```
SETUP.md (detailed troubleshooting)
```

---

**Version**: 2.0 | **Status**: Production Ready | **Last Updated**: 2026-01-06
