# Detailed Setup & Troubleshooting Guide

**For quick start, see README.md. This guide covers advanced setup and problem-solving.**

📖 **Related Documentation:**
- [ENV_SETUP.md](docs/ENV_SETUP.md) - Environment variables and API key configuration
- [SECURITY.md](docs/SECURITY.md) - Security best practices and API key protection

---

## 🔧 Advanced Setup

### Permanent Environment Variables

#### Windows (Permanent)
```powershell
# Edit PowerShell profile
notepad $PROFILE

# Add these lines:
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='your-key'

# Reload
. $PROFILE
```

#### Mac/Linux (Permanent)
```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export AI_PROVIDER=anthropic' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY="your-key"' >> ~/.bashrc
source ~/.bashrc
```

---

## 🆘 Common Issues & Solutions

### Issue 1: "API key not set"

**Symptom:**
```
❌ ERROR: ANTHROPIC_API_KEY environment variable not set.
```

**Solution:**
```bash
# Check if variable is set
# Windows:
echo $env:ANTHROPIC_API_KEY

# Mac/Linux:
echo $ANTHROPIC_API_KEY

# If empty, set it (see README.md Quick Start Step 2)
```

**Root cause:** Environment variable only set for previous terminal session. Re-run the export/set command in your current terminal.

---

### Issue 2: "Package not installed"

**Symptom:**
```
❌ ERROR: anthropic package not installed.
```

**Solution:**
```bash
pip install -r engine/requirements.txt

# If that fails, try:
pip install anthropic openai

# Verify installation:
pip list | grep -E "anthropic|openai"
```

**Root cause:** Dependencies not installed or wrong Python environment.

---

### Issue 3: "No messages parsed" or Empty Output

**Symptom:**
```
Total messages parsed: 0
```

**Solution:**

1. **Check file format:**
   - Must be: `DD/MM/YYYY, HH:MM - Sender: Message`
   - Open file in text editor and verify format

2. **Check file encoding:**
   ```bash
   # Should be UTF-8
   file -bi "input/chat.txt"  # Mac/Linux
   ```

3. **Verify it's not all system messages:**
   - System messages are filtered out
   - Need actual user messages in chat

4. **Test with sample file:**
   ```bash
   python scripts/run.py "input/Netcore & Convx - QSR Team - test text.txt"
   ```

---

### Issue 4: Unicode/Encoding Errors

**Symptom:**
```
UnicodeEncodeError: 'charmap' codec can't encode character
```

**Solution:**

This is handled automatically in the code, but if you still see it:

```bash
# Windows: Set console to UTF-8
chcp 65001

# Then run your command
python scripts/generate_report.py "input/chat.txt" "Site"
```

**Root cause:** Windows console encoding issue (already fixed in scripts).

---

### Issue 5: AI Request Fails

**Symptom:**
```
API request failed
Connection error
Rate limit exceeded
```

**Solutions:**

1. **Check API key is valid:**
   - Log into provider dashboard
   - Verify key hasn't expired
   - Check billing/credits available

2. **Rate limit:**
   - Wait 60 seconds
   - Try again
   - Consider upgrading API plan

3. **Network issues:**
   - Check internet connection
   - Try different network
   - Check firewall/proxy settings

4. **API service down:**
   - Check provider status page:
     - Anthropic: https://status.anthropic.com/
     - OpenAI: https://status.openai.com/
     - OpenRouter: https://status.openrouter.ai/

---

### Issue 6: Wrong Python Version

**Symptom:**
```
SyntaxError or module not found errors
```

**Solution:**
```bash
# Check Python version
python --version

# Need Python 3.8+
# If wrong version, use:
python3 generate_report.py "input/chat.txt" "Site"

# Or install correct Python version
```

---

### Issue 7: Multiple Python Installations

**Symptom:**
```
Packages installed but import fails
```

**Solution:**
```bash
# Check which Python
which python    # Mac/Linux
where python    # Windows

# Install packages with same Python you're using:
python -m pip install -r engine/requirements.txt

# Run scripts with same Python:
python scripts/generate_report.py "input/chat.txt" "Site"
```

---

### Issue 8: Report Quality Issues

**Symptom:**
- Report is too vague
- Missing important details
- Hallucinated information

**Solutions:**

1. **Ensure enough context:**
   - Need at least 20-30 messages with actual work discussion
   - Not just "hi", "ok", "thanks" messages

2. **Check parsed data quality:**
   ```bash
   python scripts/run.py "input/chat.txt"
   # Review output/chat_parsed.json
   ```

3. **Try different AI model:**
   - Edit `engine/summarizer.py` line 106, 136, or 168
   - Try higher-quality model (e.g., Claude Opus, GPT-4 Turbo)

4. **Adjust temperature:**
   - In `engine/summarizer.py`, find `temperature=0.3`
   - Lower = more factual (0.1-0.2)
   - Higher = more creative (0.5-0.7)

---

### Issue 9: File Path Issues

**Symptom:**
```
FileNotFoundError: No such file or directory
```

**Solution:**
```bash
# Use quotes for paths with spaces
python scripts/generate_report.py "input/my chat.txt" "Site"

# Or use absolute paths
python scripts/generate_report.py "F:/Documents/input/chat.txt" "Site"

# Check current directory
pwd    # Mac/Linux
cd     # Windows

# Navigate to project folder
cd "f:/Personal Documents/Web Project/whatsapp-eod"
```

---

### Issue 10: Permission Errors

**Symptom:**
```
Permission denied
```

**Solution:**

**Windows:**
- Run terminal as administrator
- Check file isn't open in another program
- Verify folder permissions

**Mac/Linux:**
```bash
# Make scripts executable
chmod +x generate_report.py run.py check_setup.py

# Or run with python
python scripts/generate_report.py "input/chat.txt" "Site"
```

---

## 🔍 Diagnostic Commands

### Check Everything
```bash
python scripts/check_setup.py
```

### Check Python Environment
```bash
python --version
pip list
which python  # Mac/Linux
where python  # Windows
```

### Check Environment Variables
```bash
# Windows
echo $env:AI_PROVIDER
echo $env:ANTHROPIC_API_KEY

# Mac/Linux
echo $AI_PROVIDER
echo $ANTHROPIC_API_KEY
printenv | grep -E "ANTHROPIC|OPENAI|OPENROUTER"
```

### Test Parsing Only
```bash
python scripts/run.py "input/test-file.txt"
# Check output looks correct
```

### Test with Sample Data
```bash
python scripts/generate_report.py "input/Netcore & Convx - QSR Team - test text.txt" "Test"
```

---

## ⚙️ Advanced Customization

### Change AI Model

**Edit `engine/summarizer.py`:**

**For Anthropic (line 106):**
```python
model="claude-3-5-sonnet-20241022"  # Default (best balance)
model="claude-3-opus-20240229"      # Highest quality (slower/pricier)
model="claude-3-haiku-20240307"     # Fastest (cheaper)
```

**For OpenAI (line 136):**
```python
model="gpt-4o"           # Default (best)
model="gpt-4-turbo"      # Alternative
model="gpt-3.5-turbo"    # Cheaper/faster
```

**For OpenRouter (line 168):**
```python
model="anthropic/claude-3.5-sonnet"     # Claude
model="openai/gpt-4"                    # GPT-4
model="google/gemini-pro"               # Gemini
model="meta-llama/llama-3-70b"         # Llama 3
# See all: https://openrouter.ai/models
```

### Adjust AI Temperature

**Edit `summarizer.py`, find `temperature=0.3`:**

```python
temperature=0.1  # Very factual, less creative
temperature=0.3  # Balanced (default)
temperature=0.7  # More creative, less strict
```

### Change Output Length

**Edit `summarizer.py`, find `max_tokens=2000`:**

```python
max_tokens=1000  # Shorter reports
max_tokens=2000  # Default (1 page)
max_tokens=4000  # Longer detailed reports
```

### Modify Report Prompt

**Edit `summarizer.py`, function `create_eod_prompt()`:**

- Adjust instructions for AI
- Change report sections
- Modify tone/style requirements

---

## 🔐 Security Best Practices

### Never Commit API Keys
```bash
# If using Git, add to .gitignore:
echo "*.env" >> .gitignore
echo ".env" >> .gitignore

# Never commit files with actual keys
```

### Use .env File (Optional)
```bash
# Install python-dotenv
pip install python-dotenv

# Create .env file
AI_PROVIDER=anthropic
ANTHROPIC_API_KEY=your-key-here

# Load in your scripts (modify at top of script)
from dotenv import load_dotenv
load_dotenv()
```

### Rotate Keys Regularly
- Change API keys every 3-6 months
- Revoke old keys after updating

---

## 📞 Getting Help

### Before Asking for Help

1. Run `python scripts/check_setup.py`
2. Check error message carefully
3. Review this troubleshooting guide
4. Try with sample data first

### Error Information to Provide

When reporting issues, include:
- Full error message (copy-paste)
- Python version (`python --version`)
- Operating system (Windows/Mac/Linux)
- Output of `python scripts/check_setup.py`
- Steps to reproduce

---

## 🔄 Reinstalling/Resetting

### Clean Reinstall
```bash
# Remove old packages
pip uninstall anthropic openai -y

# Reinstall
pip install -r engine/requirements.txt

# Verify
python scripts/check_setup.py
```

### Reset Environment Variables
```bash
# Windows
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='new-key'

# Mac/Linux
unset ANTHROPIC_API_KEY
export ANTHROPIC_API_KEY='new-key'
```

### Clear Cache
```bash
# Remove Python cache
rm -rf __pycache__  # Mac/Linux
rmdir /s __pycache__  # Windows

# Remove old outputs (optional)
rm output/*.json output/*.md  # Mac/Linux
```

---

## 📊 Performance Optimization

### Speed Up Processing

1. **Use faster model:**
   - Claude Haiku (Anthropic)
   - GPT-3.5 Turbo (OpenAI)

2. **Reduce max_tokens:**
   ```python
   max_tokens=1000  # Faster response
   ```

3. **Local processing for parsing:**
   - Run `python scripts/run.py` locally (instant)
   - Only send to AI when ready

### Reduce Costs

1. **Use cheaper models:**
   - Claude Haiku: ~$0.01/report
   - GPT-3.5 Turbo: ~$0.005/report

2. **Filter messages first:**
   - Parse and review JSON
   - Remove unnecessary messages manually
   - Then send to AI

3. **Batch processing:**
   - Process multiple chats in one session
   - Reuse same environment/API connection

---

## ✅ System Requirements

- **Python**: 3.8 or higher
- **RAM**: 512MB minimum (AI processing is done via API)
- **Disk**: 50MB for installation
- **Internet**: Required (for AI API calls)
- **OS**: Windows 10+, macOS 10.14+, Linux (any modern distro)

---

**For quick daily usage, see README.md**

**This guide covers edge cases and advanced scenarios only.**
