# 📊 Visual Quick Reference Guide

## 🎯 The ONE Command You Need

```bash
python generate_report.py "input/your-chat.txt" "Site Name"
```

**That's it!** This does everything automatically.

---

## 📁 Clean Directory Structure

```
whatsapp-eod/
│
├── 📘 START_HERE.md          ⭐ BEGIN HERE (5-min setup)
├── 📄 README.md              Daily reference
├── 📖 SETUP.md               Troubleshooting guide
├── 📋 PROJECT_STRUCTURE.md   File reference
├── 📋 CLEANUP_SUMMARY.md     What changed
│
├── ⚙️ SCRIPTS (What you run)
│   ├── generate_report.py   ⭐ USE THIS (complete pipeline)
│   ├── run.py                Parse only
│   └── check_setup.py        Verify environment
│
├── 🔧 ENGINE (Don't touch unless customizing)
│   ├── parser.py             Message extraction
│   ├── summarizer.py         AI integration ← API config here!
│   └── requirements.txt      Dependencies
│
├── 📥 input/                 Put WhatsApp .txt here
├── 📤 output/                Reports appear here
│
└── 📚 docs/                  Extra documentation
    ├── QUICK_REFERENCE.md
    ├── EXAMPLE_REPORT.md
    ├── PROJECT_SUMMARY.md
    └── WORKFLOW.md
```

---

## 🔄 Complete Workflow

```
┌─────────────────────┐
│  WhatsApp Chat .txt │
│  (messy, raw data)  │
└──────────┬──────────┘
           │
           ▼
   ┌───────────────┐
   │ generate_     │  ← The ONE script you need
   │ report.py     │
   └───────┬───────┘
           │
           ├──► parser.py
           │    (extracts & cleans)
           │
           ├──► summarizer.py
           │    (AI analysis)
           │    └──► Anthropic Claude
           │         OpenAI GPT-4
           │         OpenRouter (100+ models)
           │
           ▼
┌─────────────────────────┐
│  Professional EOD       │
│  Report (1 page, 6      │
│  structured sections)   │
└─────────────────────────┘
```

---

## 🤖 Three AI Provider Options

### Option A: Anthropic Claude (Recommended)
```powershell
# Windows
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='sk-ant-...'
```

- **Cost**: $0.05/report
- **Best for**: Quality & reliability
- **Get key**: https://console.anthropic.com/

### Option B: OpenAI GPT-4
```powershell
# Windows
$env:AI_PROVIDER='openai'
$env:OPENAI_API_KEY='sk-...'
```

- **Cost**: $0.04/report
- **Best for**: Familiarity
- **Get key**: https://platform.openai.com/

### Option C: OpenRouter (NEW! 100+ models)
```powershell
# Windows
$env:AI_PROVIDER='openrouter'
$env:OPENROUTER_API_KEY='sk-or-...'
```

- **Cost**: $0.03-0.08/report
- **Best for**: Flexibility (Claude, GPT-4, Gemini, Llama, etc.)
- **Get key**: https://openrouter.ai/keys

---

## 📄 API Configuration Locations

### All in ONE file: `summarizer.py`

```python
# Lines 14-25: Choose Provider
AI_PROVIDER = os.getenv("AI_PROVIDER")  # anthropic/openai/openrouter

if AI_PROVIDER == "anthropic":
    API_KEY = os.getenv("ANTHROPIC_API_KEY")     # ← Line 18
elif AI_PROVIDER == "openai":
    API_KEY = os.getenv("OPENAI_API_KEY")        # ← Line 20
elif AI_PROVIDER == "openrouter":
    API_KEY = os.getenv("OPENROUTER_API_KEY")    # ← Line 22

# Lines 106-133: Anthropic function
def summarize_with_anthropic():
    model="claude-3-5-sonnet-20241022"           # ← Line 106 (change model)

# Lines 136-165: OpenAI function
def summarize_with_openai():
    model="gpt-4o"                                # ← Line 136 (change model)

# Lines 168-197: OpenRouter function (NEW!)
def summarize_with_openrouter():
    model="anthropic/claude-3.5-sonnet"          # ← Line 168 (change model)
```

**To change AI model:**
1. Open `summarizer.py`
2. Go to the appropriate line (106, 136, or 168)
3. Change the `model=` parameter

---

## 🎯 Three Scripts Explained

### 1. generate_report.py ⭐ (USE THIS 99% OF TIME)

**What it does:**
```
Parse → Clean → AI → Save → Done
```

**Command:**
```bash
python generate_report.py "input/chat.txt" "Site Name"
```

**Output:**
- `output/chat_parsed.json`
- `output/chat_eod_report.md` ← Share this!

---

### 2. run.py (Validation Mode)

**What it does:**
```
Parse → Clean → Preview → Save JSON (no AI)
```

**Command:**
```bash
python run.py "input/chat.txt"
```

**When to use:** Check parsing quality before AI

---

### 3. check_setup.py (Diagnostics)

**What it does:**
```
Check Python → Check Packages → Check API → Report
```

**Command:**
```bash
python check_setup.py
```

**When to use:** Troubleshooting

---

## 📊 Report Structure (Always the Same)

```markdown
## Site: Your Site Name
## Date: DD/MM/YYYY

### 1. Overall Site Status
[Executive summary paragraph]

### 2. Work Completed Today
- Achievement 1
- Achievement 2

### 3. Issues / Delays
- Problem 1
- Blocker 2

### 4. Risks / Attention Required
- **Critical risk** (bold)
- Concern needing attention

### 5. Tomorrow's Planned Work
- Scheduled activity 1
- Meeting 2

### 6. Decisions Needed
- Approval needed
- Management input required
```

---

## 🚀 Quick Start Steps

```
┌──────────────────────────────────┐
│ Step 1: Install Dependencies    │
│ pip install -r requirements.txt │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│ Step 2: Choose AI Provider      │
│ (Anthropic/OpenAI/OpenRouter)   │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│ Step 3: Set Environment Vars    │
│ $env:AI_PROVIDER='...'          │
│ $env:ANTHROPIC_API_KEY='...'    │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│ Step 4: Verify Setup             │
│ python check_setup.py            │
└──────────────────────────────────┘
              ↓
┌──────────────────────────────────┐
│ Step 5: Generate Report          │
│ python generate_report.py        │
│   "input/test.txt" "Test Site"   │
└──────────────────────────────────┘
              ↓
           ✅ DONE!
```

---

## 💡 OpenRouter Model Examples

Edit `summarizer.py` line 168:

```python
# Claude models
model="anthropic/claude-3.5-sonnet"      # Best quality
model="anthropic/claude-3-opus"          # Highest quality
model="anthropic/claude-3-haiku"         # Fastest/cheapest

# OpenAI models
model="openai/gpt-4"                     # Standard
model="openai/gpt-4-turbo"               # Faster
model="openai/gpt-3.5-turbo"             # Cheapest

# Google models
model="google/gemini-pro"                # Gemini Pro
model="google/gemini-pro-1.5"            # Latest

# Meta models
model="meta-llama/llama-3-70b"          # Llama 3
model="meta-llama/llama-3-8b"           # Smaller/faster
```

**See all 100+ models**: https://openrouter.ai/models

---

## 📥 How to Get WhatsApp Export

```
┌─────────────────────┐
│ Open WhatsApp       │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Go to Group Chat    │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Tap ⋮ (Menu)        │
│ → More              │
│ → Export chat       │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Choose WITHOUT      │
│ MEDIA               │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Save .txt file      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Transfer to input/  │
│ folder on PC        │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│ Run generate_       │
│ report.py           │
└─────────────────────┘
```

---

## 🎓 Decision Tree: Which Script to Use?

```
                START
                  │
    ┌─────────────┴─────────────┐
    │                           │
Need to generate          Need to check
  a report?                   setup?
    │                           │
    ▼                           ▼
Want to check          Run check_setup.py
parsing first?
    │
    ├── YES ──► run.py ──► Review ──► summarizer.py
    │
    └── NO ───► generate_report.py ◄──── USE THIS 99% OF TIME
```

---

## 💰 Cost Comparison

| Provider | Per Report | 20 Reports | 100 Reports |
|----------|-----------|-----------|-------------|
| Claude 3.5 Sonnet | $0.05 | $1 | $5 |
| GPT-4o | $0.04 | $0.80 | $4 |
| OpenRouter (varies) | $0.03-0.08 | $0.60-1.60 | $3-8 |

*Based on ~200 messages per report*

---

## ✅ Daily Workflow

### Simple (Recommended)
```bash
# 1. Export WhatsApp chat to input/
# 2. Run one command:
python generate_report.py "input/today.txt" "Site Alpha"
# 3. Share: output/today_eod_report.md
```

### Careful (Two-Step)
```bash
# 1. Export WhatsApp chat to input/
# 2. Parse first:
python run.py "input/today.txt"
# 3. Review: output/today_parsed.json
# 4. If good, summarize:
python summarizer.py "output/today_parsed.json" "Site Alpha"
# 5. Share: output/today_eod_report.md
```

---

## 🆘 Troubleshooting Flow

```
Something not working?
        │
        ▼
Run: python check_setup.py
        │
        ├─► ❌ Python version → Install Python 3.8+
        │
        ├─► ❌ Packages → pip install -r requirements.txt
        │
        ├─► ❌ API key → Set environment variable (see START_HERE.md)
        │
        └─► ✅ All good → Check SETUP.md for advanced help
```

---

## 📚 Documentation Hierarchy

```
NEW USER? → START_HERE.md (5 minutes)
    │
    ├─► Need overview? → README.md
    │
    ├─► Setup issues? → SETUP.md
    │
    ├─► File locations? → PROJECT_STRUCTURE.md
    │
    ├─► Commands? → docs/QUICK_REFERENCE.md
    │
    ├─► Example? → docs/EXAMPLE_REPORT.md
    │
    └─► Deep dive? → docs/PROJECT_SUMMARY.md
```

---

## 🎯 Key Points to Remember

1. **One command for daily use**: `generate_report.py`
2. **API config in ONE file**: `summarizer.py` (lines 14-197)
3. **Three AI providers**: Anthropic, OpenAI, OpenRouter
4. **Start with**: `START_HERE.md`
5. **Docs organized**: Root = essential, `docs/` = reference

---

## 🎨 File Color Code

- 📘 **Blue** = Setup guides (START_HERE, README, SETUP)
- ⚙️ **Gear** = Scripts you run
- 🔧 **Wrench** = Engine files (don't touch unless customizing)
- 📥 **Inbox** = Input folder (your WhatsApp files)
- 📤 **Outbox** = Output folder (generated reports)
- 📚 **Books** = Documentation reference

---

**🎯 Remember: For 99% of your work:**

```bash
python generate_report.py "input/chat.txt" "Site Name"
```

**API config location:**
```
summarizer.py
  → Lines 14-25: API keys
  → Lines 106-197: AI functions (change models here)
```

**Start here:**
```
START_HERE.md (5-minute setup)
```

