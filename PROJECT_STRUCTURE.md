# 📁 Project Structure - Clean & Organized

## Directory Layout

```
whatsapp-eod/
│
├── 📘 START_HERE.md          ⭐ BEGIN HERE - 5-minute setup guide
├── 📄 README.md              Overview & daily usage
├── 📖 SETUP.md               Detailed setup & troubleshooting
├── 📋 PROJECT_STRUCTURE.md   This file (directory reference)
│
├── ⚙️ CORE SCRIPTS (What you use)
│   ├── generate_report.py   ⭐ MAIN SCRIPT - Complete pipeline
│   ├── run.py                Parse only (for validation)
│   └── check_setup.py        Environment verification
│
├── 🔧 ENGINE (Don't touch unless customizing)
│   ├── parser.py             Message extraction logic
│   ├── summarizer.py         AI report generation (API config here)
│   └── requirements.txt      Python dependencies
│
├── 📥 input/                 Put WhatsApp .txt exports here
│   └── *.txt                 Your chat files
│
├── 📤 output/                Generated reports appear here
│   ├── *_parsed.json         Clean message data
│   └── *_eod_report.md       Final reports
│
└── 📚 docs/                  Additional documentation
    ├── QUICK_REFERENCE.md    Command cheat sheet
    ├── EXAMPLE_REPORT.md     Sample output
    ├── PROJECT_SUMMARY.md    Complete project overview
    └── WORKFLOW.md           Visual diagrams
```

---

## File Purposes

### 🎯 Start Here (Essential)

| File | Purpose | When to Read |
|------|---------|-------------|
| **START_HERE.md** | 5-minute complete setup | First time setup |
| **README.md** | Project overview & daily usage | After setup |
| **SETUP.md** | Detailed config & troubleshooting | When issues occur |

### ⚙️ Scripts (What You Run)

| Script | What It Does | When to Use |
|--------|-------------|-------------|
| **generate_report.py** ⭐ | Parse + Summarize (complete) | **99% of the time** |
| **run.py** | Parse only (no AI) | To check parsing quality |
| **check_setup.py** | Verify environment setup | When something breaks |

### 🔧 Engine (What Powers It)

| File | Purpose | When to Edit |
|------|---------|-------------|
| **parser.py** | Extracts messages from WhatsApp | Adding new message formats |
| **summarizer.py** | AI API integration | Changing AI provider/model |
| **requirements.txt** | Python packages needed | Adding new dependencies |

### 📚 Documentation (Reference)

| File | Content |
|------|---------|
| **docs/QUICK_REFERENCE.md** | Command cheat sheet |
| **docs/EXAMPLE_REPORT.md** | Sample generated report |
| **docs/PROJECT_SUMMARY.md** | Complete technical details |
| **docs/WORKFLOW.md** | Visual workflow diagrams |

---

## The 3 Scripts Explained

### 1. generate_report.py ⭐ (USE THIS ONE)

**What it does:**
```
WhatsApp .txt → Parse → Clean → AI Summarize → Save Report
```

**Command:**
```bash
python generate_report.py "input/chat.txt" "Site Name"
```

**Output:**
- `output/chat_parsed.json` (clean data)
- `output/chat_eod_report.md` (final report)

**When to use**: Daily report generation (99% of the time)

---

### 2. run.py (Parse Only)

**What it does:**
```
WhatsApp .txt → Parse → Clean → Save JSON
```

**Command:**
```bash
python run.py "input/chat.txt"
```

**Output:**
- `output/chat_parsed.json` (clean data only)
- Preview of first 10 messages

**When to use**: When you want to validate parsing quality before sending to AI

---

### 3. check_setup.py (Diagnostics)

**What it does:**
```
Check Python → Check Packages → Check API Key → Report Status
```

**Command:**
```bash
python check_setup.py
```

**Output:**
- ✅ or ❌ for each check
- Helpful error messages if something is wrong

**When to use**: When something isn't working or after initial setup

---

## API Configuration Locations

### All API-related code is in ONE file: `summarizer.py`

#### Lines 14-25: API Key Configuration
```python
# Choose provider
AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic")

# Load appropriate API key
if AI_PROVIDER == "anthropic":
    API_KEY = os.getenv("ANTHROPIC_API_KEY")  # ← Anthropic config
elif AI_PROVIDER == "openai":
    API_KEY = os.getenv("OPENAI_API_KEY")     # ← OpenAI config
elif AI_PROVIDER == "openrouter":
    API_KEY = os.getenv("OPENROUTER_API_KEY")  # ← OpenRouter config
```

#### Lines 106-197: AI Provider Functions

| Lines | Function | Provider | What to Edit |
|-------|----------|----------|--------------|
| 106-133 | `summarize_with_anthropic()` | Anthropic Claude | Change model on line 106 |
| 136-165 | `summarize_with_openai()` | OpenAI GPT-4 | Change model on line 136 |
| 168-197 | `summarize_with_openrouter()` | OpenRouter (NEW!) | Change model on line 168 |

**Example model changes:**
```python
# Line 106 (Anthropic)
model="claude-3-5-sonnet-20241022"  # Default
model="claude-3-opus-20240229"      # Higher quality
model="claude-3-haiku-20240307"     # Faster/cheaper

# Line 136 (OpenAI)
model="gpt-4o"           # Default
model="gpt-4-turbo"      # Alternative
model="gpt-3.5-turbo"    # Cheaper

# Line 168 (OpenRouter - 100+ models!)
model="anthropic/claude-3.5-sonnet"     # Claude
model="openai/gpt-4"                    # GPT-4
model="google/gemini-pro"               # Gemini
model="meta-llama/llama-3-70b"         # Llama
```

---

## Input/Output Flow

### Input Directory (`input/`)

**What goes here:**
- WhatsApp exported .txt files
- One file per chat/day
- Standard WhatsApp format: `DD/MM/YYYY, HH:MM - Sender: Message`

**How to get files:**
1. Open WhatsApp → Group Chat
2. Menu (⋮) → More → Export chat
3. Choose "Without media"
4. Save .txt file
5. Move to `input/` folder

### Output Directory (`output/`)

**What appears here:**
- `filename_parsed.json` - Clean message data (for debugging)
- `filename_eod_report.md` - Final professional report (what you share)

**Auto-created**: The script creates these files automatically

---

## Documentation Hierarchy

```
START HERE (First time)
    ↓
START_HERE.md (5 min setup)
    ↓
README.md (Overview & daily usage)
    ↓
    ├─→ Need help?  → SETUP.md (Troubleshooting)
    ├─→ Commands?   → docs/QUICK_REFERENCE.md
    ├─→ Examples?   → docs/EXAMPLE_REPORT.md
    └─→ Technical?  → docs/PROJECT_SUMMARY.md
```

**Most people only need:**
1. START_HERE.md (once)
2. README.md (reference)
3. The generate_report.py command (daily)

---

## What NOT to Touch

### Leave These Alone (Unless Customizing)

- `parser.py` - Core parsing logic works perfectly
- `__pycache__/` - Python cache (auto-generated)
- `.git/` - Version control (if using Git)
- `output/*.json` - Generated data files (auto-created)

### Safe to Delete

- `output/*.json` - Regenerate anytime
- `output/*.md` - Old reports you don't need
- `docs/` - Can delete if you don't need reference docs

### Never Delete

- Core scripts: `generate_report.py`, `parser.py`, `summarizer.py`
- Setup files: `requirements.txt`, `check_setup.py`
- Main docs: `START_HERE.md`, `README.md`, `SETUP.md`

---

## Workflow Summary

### Daily Report Generation (Simple)

```
1. Export WhatsApp chat
2. Save to input/
3. Run: python generate_report.py "input/file.txt" "Site Name"
4. Share: output/file_eod_report.md
```

### Two-Step Validation (Careful)

```
1. Export WhatsApp chat
2. Save to input/
3. Run: python run.py "input/file.txt"
4. Review: output/file_parsed.json
5. If good → Run: python summarizer.py "output/file_parsed.json" "Site"
6. Share: output/file_eod_report.md
```

---

## Quick Reference

| I want to... | Use this command |
|--------------|------------------|
| Generate a report | `python generate_report.py "input/chat.txt" "Site"` |
| Just parse (no AI) | `python run.py "input/chat.txt"` |
| Check my setup | `python check_setup.py` |
| Change AI model | Edit `summarizer.py` lines 106/136/168 |
| Change API provider | Set environment variable `AI_PROVIDER` |
| Add new dependency | Add to `requirements.txt`, run `pip install -r requirements.txt` |

---

## File Size Reference

| File | Lines | Purpose |
|------|-------|---------|
| generate_report.py | 105 | Main script |
| parser.py | 135 | Parsing engine |
| summarizer.py | 259 | AI integration ← API config here |
| run.py | 72 | Parse-only CLI |
| check_setup.py | 188 | Setup verification |
| START_HERE.md | ~300 | Quick setup |
| README.md | ~230 | Overview |
| SETUP.md | ~250 | Detailed setup |

---

**🎯 Remember**: For 99% of your work, you only need one command:

```bash
python generate_report.py "input/your-chat.txt" "Your Site Name"
```

Everything else is for setup, troubleshooting, or customization!

