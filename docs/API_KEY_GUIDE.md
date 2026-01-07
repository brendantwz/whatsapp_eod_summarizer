# API Key Storage - Quick Reference

## 🎯 Where to Store Your API Keys

### ✅ CORRECT: Use `.env` File (Recommended)

1. **Create a `.env` file in the project root:**

```env
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

2. **The `.env` file is automatically protected by `.gitignore`** ✅

3. **The code automatically loads it** (using `python-dotenv`)

### ✅ CORRECT: Use System Environment Variables

**Windows PowerShell:**
```powershell
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='sk-ant-your-key-here'
```

**Mac/Linux:**
```bash
export AI_PROVIDER=anthropic
export ANTHROPIC_API_KEY='sk-ant-your-key-here'
```

### ❌ WRONG: Hardcoding in Source Files

**NEVER do this:**
```python
# ❌ BAD - This will be committed to Git!
API_KEY = "sk-ant-1234567890"
```

## 📁 File Structure

```
whatsapp-eod/
├── .env                    # ✅ Your actual keys (NOT committed)
├── .gitignore              # ✅ Protects .env from Git
├── ENV_SETUP.md            # 📖 Setup instructions
├── SECURITY.md             # 🔒 Security guidelines
├── engine/
│   └── summarizer.py       # ✅ Reads from environment
└── README.md
```

## 🔒 Security Features Implemented

1. **`.gitignore` Protection**
   - `.env` file is ignored by Git
   - Won't be committed accidentally

2. **Environment Variable Loading**
   - Automatic `.env` file loading (if `python-dotenv` installed)
   - Falls back to system environment variables

3. **Configurable Models**
   - No hardcoded model versions
   - Can be changed via environment variables

## 🚀 Quick Setup

### Step 1: Install Dependencies
```bash
pip install -r engine/requirements.txt
```

### Step 2: Create `.env` File
```bash
# Create .env file with your keys
cat > .env << EOF
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
EOF
```

### Step 3: Verify Setup
```bash
# Check that .env is ignored by Git
git status
# You should NOT see .env in the list

# Run the application
python scripts/run.py
```

## 🔄 Switching Models

### Change Anthropic Model
```env
# In your .env file
ANTHROPIC_MODEL=claude-3-opus-20240229
```

### Change to OpenAI
```env
# In your .env file
AI_PROVIDER=openai
OPENAI_API_KEY=sk-your-openai-key
OPENAI_MODEL=gpt-4-turbo
```

### Change to OpenRouter
```env
# In your .env file
AI_PROVIDER=openrouter
OPENROUTER_API_KEY=sk-or-your-key
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
```

## ⚠️ Model Version Concern - RESOLVED

**Your Question:** 
> "I noticed line 108 uses `claude-3-5-sonnet-20241022` - would this be a concern if we use other models?"

**Answer:** ✅ **FIXED!** 

**Before (Hardcoded):**
```python
def summarize_with_anthropic(messages, site_name=None, model="claude-3-5-sonnet-20241022"):
```

**After (Configurable):**
```python
def summarize_with_anthropic(messages, site_name=None, model=None):
    model = model or ANTHROPIC_MODEL  # Reads from environment
```

**Now you can:**
- Change models via `.env` file
- Override per function call
- Use different models without code changes

## 📚 Related Documentation

- **[ENV_SETUP.md](ENV_SETUP.md)** - Detailed environment setup
- **[SECURITY.md](SECURITY.md)** - Security best practices
- **[SETUP.md](SETUP.md)** - Troubleshooting guide
- **[README.md](README.md)** - Quick start guide

## ✅ Security Checklist

Before committing:
- [ ] `.env` file exists locally
- [ ] `.env` is in `.gitignore`
- [ ] No API keys in source code
- [ ] `git status` doesn't show `.env`
- [ ] Tested with your API key

## 🆘 Help

If you see this error:
```
❌ ERROR: ANTHROPIC_API_KEY environment variable not set.
```

**Solution:**
1. Check if `.env` file exists: `ls -la .env`
2. Check if key is in `.env`: `cat .env`
3. Install python-dotenv: `pip install python-dotenv`
4. Restart your terminal/IDE

---

**Quick Test:**
```bash
# Test that environment variables are loaded
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('AI_PROVIDER'))"
```

Should output: `anthropic` (or your chosen provider)

