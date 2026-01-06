# 🚀 START HERE - Quick Setup Guide

**Complete setup in 5 minutes. Follow these steps in order.**

---

## Step 1: Install Python Dependencies (1 minute)

Open your terminal and run:

```bash
cd "f:/Personal Documents/Web Project/whatsapp-eod"
pip install -r requirements.txt
```

This installs the AI provider packages you'll need.

---

## Step 2: Choose Your AI Provider (1 minute)

You need to pick **ONE** of these three options:

### Option A: Anthropic Claude (Recommended)
- **Best for**: Quality and reliability
- **Cost**: ~$0.05 per report
- **Sign up**: https://console.anthropic.com/
- **Get API key**: Console → API Keys → Create Key

### Option B: OpenAI GPT-4
- **Best for**: Familiarity with OpenAI
- **Cost**: ~$0.04 per report
- **Sign up**: https://platform.openai.com/
- **Get API key**: API Keys → Create new secret key

### Option C: OpenRouter (NEW!)
- **Best for**: Access to multiple models with one API key
- **Cost**: Pay-per-use, varies by model
- **Sign up**: https://openrouter.ai/
- **Get API key**: https://openrouter.ai/keys
- **Available models**: Claude, GPT-4, Gemini, Llama, and 100+ more

---

## Step 3: Set Your API Key (2 minutes)

### For Windows (PowerShell):

**If you chose Anthropic:**
```powershell
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='sk-ant-your-key-here'
```

**If you chose OpenAI:**
```powershell
$env:AI_PROVIDER='openai'
$env:OPENAI_API_KEY='sk-your-key-here'
```

**If you chose OpenRouter:**
```powershell
$env:AI_PROVIDER='openrouter'
$env:OPENROUTER_API_KEY='sk-or-your-key-here'
```

### For Mac/Linux:

**If you chose Anthropic:**
```bash
export AI_PROVIDER=anthropic
export ANTHROPIC_API_KEY='sk-ant-your-key-here'
```

**If you chose OpenAI:**
```bash
export AI_PROVIDER=openai
export OPENAI_API_KEY='sk-your-key-here'
```

**If you chose OpenRouter:**
```bash
export AI_PROVIDER=openrouter
export OPENROUTER_API_KEY='sk-or-your-key-here'
```

---

## Step 4: Verify Setup (30 seconds)

Run this command to check everything is configured:

```bash
python check_setup.py
```

You should see:
- ✅ Python version compatible
- ✅ AI package(s) installed
- ✅ API key configured

If you see any ❌, fix those issues first!

---

## Step 5: Test with Sample Data (30 seconds)

Run your first report generation:

```bash
python generate_report.py "input/Netcore & Convx - QSR Team - test text.txt" "Test Site"
```

If successful, you'll see:
- Parsed messages preview
- AI generating report
- Final report displayed
- Files saved to `output/` folder

---

## 🎯 You're Ready! Daily Usage

### The ONE Command You Need

```bash
python generate_report.py "input/your-chat-file.txt" "Your Site Name"
```

That's it! This command does EVERYTHING:
1. ✅ Parses WhatsApp chat
2. ✅ Cleans and validates messages
3. ✅ Sends to AI for summarization
4. ✅ Generates structured EOD report
5. ✅ Saves both JSON and Markdown files

---

## 📁 Where Files Go

```
input/               ← Put your WhatsApp .txt exports here
output/              ← Generated reports appear here
  ├── yourfile_parsed.json        (clean data)
  └── yourfile_eod_report.md      (final report)
```

---

## 🔧 The 3 Scripts Explained

| Script | What It Does | When to Use |
|--------|-------------|-------------|
| **`generate_report.py`** | Complete pipeline | **USE THIS 99% OF THE TIME** |
| `run.py` | Parse only (no AI) | When you want to check parsing quality first |
| `check_setup.py` | Verify environment | When something isn't working |

**💡 Pro Tip**: Just use `generate_report.py` for daily reports!

---

## 📋 How to Export WhatsApp Chat

1. Open WhatsApp on your phone
2. Go to the group chat
3. Tap the 3 dots (⋮) → **More** → **Export chat**
4. Choose **Without media**
5. Save the .txt file
6. Transfer to your computer's `input/` folder
7. Run `generate_report.py`!

---

## 🆘 Troubleshooting

### "API key not set"
- Re-run Step 3 commands in your current terminal
- Verify with: `echo $env:ANTHROPIC_API_KEY` (Windows) or `echo $ANTHROPIC_API_KEY` (Mac/Linux)

### "Package not installed"
- Run: `pip install -r requirements.txt`

### "No messages parsed"
- Make sure the WhatsApp export is in standard format
- Check the file has actual messages, not just system notifications

### Need more help?
- Run: `python check_setup.py` to diagnose
- See `SETUP.md` for detailed troubleshooting

---

## 🎓 Advanced: API Key Locations (Where to Update)

All API-related configuration is in **ONE FILE**:

### 📄 `summarizer.py` (Lines 14-25)

```python
# Line 14-25: API Provider Configuration
AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic")

if AI_PROVIDER == "anthropic":
    API_KEY = os.getenv("ANTHROPIC_API_KEY")  # ← Anthropic key location
elif AI_PROVIDER == "openai":
    API_KEY = os.getenv("OPENAI_API_KEY")     # ← OpenAI key location
elif AI_PROVIDER == "openrouter":
    API_KEY = os.getenv("OPENROUTER_API_KEY")  # ← OpenRouter key location
```

**Functions that use the API:**
- **Line 106-133**: `summarize_with_anthropic()` - Claude API calls
- **Line 136-165**: `summarize_with_openai()` - GPT-4 API calls
- **Line 168-197**: `summarize_with_openrouter()` - OpenRouter API calls

**To change the AI model**, edit the `model` parameter:
- Line 106: `model="claude-3-5-sonnet-20241022"` (Anthropic)
- Line 136: `model="gpt-4o"` (OpenAI)
- Line 168: `model="anthropic/claude-3.5-sonnet"` (OpenRouter)

---

## 🎨 Customization

### Change AI Model (in summarizer.py)

**For OpenRouter, you can use any model:**
```python
model="anthropic/claude-3.5-sonnet"    # Claude via OpenRouter
model="openai/gpt-4"                    # GPT-4 via OpenRouter
model="google/gemini-pro"               # Gemini via OpenRouter
model="meta-llama/llama-3-70b"         # Llama 3 via OpenRouter
```

See all models: https://openrouter.ai/models

---

## 💰 Cost Comparison

| Provider | Cost per Report | 100 Reports | Where to Get Key |
|----------|----------------|-------------|------------------|
| Anthropic Claude | $0.05 | $5 | console.anthropic.com |
| OpenAI GPT-4 | $0.04 | $4 | platform.openai.com |
| OpenRouter | $0.03-0.08 | $3-8 | openrouter.ai/keys |

*Based on ~200 messages per report*

---

## ✅ Quick Checklist

- [ ] Installed Python dependencies
- [ ] Chose AI provider
- [ ] Got API key from provider website
- [ ] Set environment variables
- [ ] Ran `check_setup.py` successfully
- [ ] Tested with sample file
- [ ] Generated first report

**All done? You're ready to generate professional EOD reports! 🎉**

---

## 📞 Next Steps

- **Daily use**: Just run `generate_report.py` with your chat files
- **Need more details?**: See `README.md`
- **Advanced setup**: See `SETUP.md`
- **More documentation**: Check the `docs/` folder

---

**🎯 Remember**: `python generate_report.py "input/chat.txt" "Site Name"`

That's the only command you need to memorize!

