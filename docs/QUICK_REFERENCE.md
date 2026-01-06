# Quick Reference Guide

## 🚀 One-Command Cheat Sheet

```bash
# Check if everything is set up correctly
python check_setup.py

# Complete pipeline: Parse + Summarize
python generate_report.py "input/chat.txt" "Site Name"

# Parse only (no AI needed)
python run.py "input/chat.txt"

# Summarize pre-parsed JSON
python summarizer.py "output/chat_parsed.json" "Site Name"
```

## 📋 Common Workflows

### Daily EOD Report Generation

```bash
# 1. Export WhatsApp chat and save to input/ folder
# 2. Run complete pipeline
python generate_report.py "input/daily-chat.txt" "Construction Site Alpha"
# 3. Find report at: output/daily-chat_eod_report.md
```

### Validate Before Summarizing

```bash
# Parse and check message quality
python run.py "input/chat.txt"

# Review the parsed JSON
# If good, then summarize:
python summarizer.py "output/chat_parsed.json" "Site Name"
```

### Batch Processing Multiple Chats

**Windows PowerShell:**
```powershell
Get-ChildItem input/*.txt | ForEach-Object {
    python generate_report.py $_.FullName "Site Alpha"
}
```

**Mac/Linux:**
```bash
for file in input/*.txt; do
    python generate_report.py "$file" "Site Alpha"
done
```

## ⚙️ Environment Setup

### Windows PowerShell (Temporary)
```powershell
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='sk-ant-api03-...'
```

### Windows PowerShell (Permanent)
```powershell
# Edit your PowerShell profile
notepad $PROFILE

# Add these lines:
$env:AI_PROVIDER='anthropic'
$env:ANTHROPIC_API_KEY='sk-ant-api03-...'

# Restart PowerShell or reload:
. $PROFILE
```

### Mac/Linux (Temporary)
```bash
export AI_PROVIDER=anthropic
export ANTHROPIC_API_KEY='sk-ant-api03-...'
```

### Mac/Linux (Permanent)
```bash
# Add to ~/.bashrc or ~/.zshrc
echo 'export AI_PROVIDER=anthropic' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc
source ~/.bashrc
```

## 📂 File Structure Quick View

```
input/          → WhatsApp .txt files go here
output/         → Generated JSON and .md reports
parser.py       → Extract messages from WhatsApp exports
summarizer.py   → AI-powered report generation
run.py          → Parse only (CLI)
generate_report.py  → Complete pipeline (CLI)
check_setup.py  → Verify environment setup
```

## 🎯 Command Parameters

### `generate_report.py` (Recommended)
```bash
python generate_report.py <input_file> [site_name]
```
- `input_file`: WhatsApp .txt export (required)
- `site_name`: Construction site name (optional, AI will extract if omitted)

### `run.py` (Parse Only)
```bash
python run.py <input_file> [output_file]
```
- `input_file`: WhatsApp .txt export (required)
- `output_file`: Output JSON path (optional, auto-generated)

### `summarizer.py` (Summarize Only)
```bash
python summarizer.py <parsed_json> [site_name] [output_file]
```
- `parsed_json`: Parsed messages JSON (required)
- `site_name`: Site name (optional)
- `output_file`: Report output path (optional)

## 📊 Report Structure Reference

Every generated report follows this structure:

```markdown
## Site: [Name]
## Date: [DD/MM/YYYY]

### 1. Overall Site Status
[Executive summary paragraph]

### 2. Work Completed Today
- Bullet points of achievements

### 3. Issues / Delays
- Problems and blockers

### 4. Risks / Attention Required
- **Critical items in bold**
- Management attention needed

### 5. Tomorrow's Planned Work
- Scheduled activities

### 6. Decisions Needed
- Awaiting approvals
```

## 🔧 Troubleshooting One-Liners

```bash
# Check if API key is set (Windows)
echo $env:ANTHROPIC_API_KEY

# Check if API key is set (Mac/Linux)
echo $ANTHROPIC_API_KEY

# Install dependencies
pip install -r requirements.txt

# Test with sample file
python generate_report.py "input/Netcore & Convx - QSR Team - test text.txt" "Test Site"

# Verify setup
python check_setup.py
```

## 💡 Pro Tips

1. **Always validate first**: Run `check_setup.py` before your first report
2. **Use descriptive site names**: Makes reports easier to organize
3. **Batch process at end of day**: Process all daily chats at once
4. **Check parsed output**: Review JSON if report seems off
5. **Keep messages focused**: AI works best with 20+ contextual messages

## 🎨 Customization

### Change AI Model (in `summarizer.py`)

**For higher quality:**
```python
model="claude-3-opus-20240229"  # Anthropic
# or
model="gpt-4-turbo"  # OpenAI
```

**For lower cost:**
```python
model="claude-3-haiku-20240307"  # Anthropic (fast & cheap)
# or
model="gpt-3.5-turbo"  # OpenAI (cheapest)
```

### Adjust Report Length

Edit the prompt in `summarizer.py` → `create_eod_prompt()`:
```python
# For shorter reports:
"Keep extremely concise, maximum 0.5 page"

# For more detail:
"Provide detailed analysis, maximum 2 pages"
```

## 📞 Quick Help

- **Parser issues**: Check `parser.py` → System message filters
- **AI not working**: Run `check_setup.py` → Verify API key
- **Report quality**: Ensure messages have enough context
- **Cost concerns**: Use Claude Haiku or GPT-3.5-turbo

---

**For detailed setup**: See `SETUP.md`
**For full documentation**: See `README.md`
**For examples**: See `EXAMPLE_REPORT.md`

