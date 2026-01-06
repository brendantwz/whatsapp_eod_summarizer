# Setup Guide - WhatsApp EOD Report Generator

## 🚀 Quick Start (5 minutes)

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `anthropic` - Claude API (recommended)
- `openai` - GPT-4 API (alternative)

### 2. Get Your API Key

#### Option A: Claude (Anthropic) - **Recommended**

1. Visit: https://console.anthropic.com/
2. Sign up / Log in
3. Navigate to **API Keys** section
4. Click **Create Key**
5. Copy your key (starts with `sk-ant-...`)

**Pricing**: ~$3 per million input tokens, $15 per million output tokens
**Model**: `claude-3-5-sonnet-20241022`

#### Option B: OpenAI (GPT-4)

1. Visit: https://platform.openai.com/
2. Sign up / Log in
3. Navigate to **API Keys**
4. Click **Create new secret key**
5. Copy your key (starts with `sk-...`)

**Pricing**: ~$2.50 per million input tokens, $10 per million output tokens
**Model**: `gpt-4o`

#### Option C: OpenRouter (NEW!) - **100+ Models**

1. Visit: https://openrouter.ai/
2. Sign up / Log in
3. Navigate to: https://openrouter.ai/keys
4. Click **Create Key**
5. Copy your key (starts with `sk-or-...`)

**Pricing**: Pay-per-use, varies by model ($0.03-0.15 per report typically)
**Models**: Access Claude, GPT-4, Gemini, Llama, and 100+ others with one key
**View all models**: https://openrouter.ai/models

### 3. Set Environment Variables

#### Windows (PowerShell):

**For Anthropic:**
```powershell
$env:AI_PROVIDER="anthropic"
$env:ANTHROPIC_API_KEY="your-key-here"
```

**For OpenAI:**
```powershell
$env:AI_PROVIDER="openai"
$env:OPENAI_API_KEY="your-key-here"
```

**For OpenRouter:**
```powershell
$env:AI_PROVIDER="openrouter"
$env:OPENROUTER_API_KEY="your-key-here"
```

#### Windows (Command Prompt):

**For Anthropic:**
```cmd
set AI_PROVIDER=anthropic
set ANTHROPIC_API_KEY=your-key-here
```

**For OpenAI:**
```cmd
set AI_PROVIDER=openai
set OPENAI_API_KEY=your-key-here
```

**For OpenRouter:**
```cmd
set AI_PROVIDER=openrouter
set OPENROUTER_API_KEY=your-key-here
```

#### Mac/Linux:

**For Anthropic:**
```bash
export AI_PROVIDER=anthropic
export ANTHROPIC_API_KEY=your-key-here
```

**For OpenAI:**
```bash
export AI_PROVIDER=openai
export OPENAI_API_KEY=your-key-here
```

**For OpenRouter:**
```bash
export AI_PROVIDER=openrouter
export OPENROUTER_API_KEY=your-key-here
```

#### Permanent Setup (Windows):
```powershell
# Add to your PowerShell profile
notepad $PROFILE

# Add these lines:
$env:AI_PROVIDER="anthropic"
$env:ANTHROPIC_API_KEY="your-actual-key"
```

#### Permanent Setup (Mac/Linux):
```bash
# Add to your .bashrc or .zshrc
echo 'export AI_PROVIDER=anthropic' >> ~/.bashrc
echo 'export ANTHROPIC_API_KEY=your-actual-key' >> ~/.bashrc
source ~/.bashrc
```

### 4. Test the Setup

```bash
# Test parsing only (no API needed)
python run.py "input/Netcore & Convx - QSR Team - test text.txt"

# Test complete pipeline (requires API key)
python generate_report.py "input/Netcore & Convx - QSR Team - test text.txt" "Test Site"
```

## 📁 Project Structure

```
whatsapp-eod/
├── input/                          # Put WhatsApp .txt exports here
│   └── team-chat.txt
├── output/                         # Generated files go here
│   ├── team-chat_parsed.json      # Parsed messages
│   └── team-chat_eod_report.md    # Final EOD report
├── parser.py                       # Message extraction
├── summarizer.py                   # AI report generation
├── run.py                          # Parse only
├── generate_report.py              # Complete pipeline
├── requirements.txt                # Dependencies
├── README.md                       # Main documentation
└── SETUP.md                        # This file
```

## 🎯 Usage Patterns

### Pattern 1: Quick Daily Report
```bash
# One command, full pipeline
python generate_report.py "input/today-chat.txt" "Site Alpha"
```

### Pattern 2: Parse First, Then Summarize
```bash
# Step 1: Parse (check quality first)
python run.py "input/today-chat.txt"

# Step 2: Generate report (after validation)
python summarizer.py "output/today-chat_parsed.json" "Site Alpha"
```

### Pattern 3: Batch Processing
```bash
# Parse multiple chats
for file in input/*.txt; do
    python run.py "$file"
done

# Generate reports
for file in output/*_parsed.json; do
    python summarizer.py "$file" "Site Alpha"
done
```

## ⚙️ Configuration Options

### Change AI Model

**For Claude:**
```python
# In summarizer.py, modify:
model="claude-3-5-sonnet-20241022"  # Default (best)
# or
model="claude-3-opus-20240229"      # Highest quality
# or
model="claude-3-haiku-20240307"     # Fastest/cheapest
```

**For OpenAI:**
```python
# In summarizer.py, modify:
model="gpt-4o"           # Default (best)
# or
model="gpt-4-turbo"      # Alternative
# or
model="gpt-3.5-turbo"    # Cheapest
```

## 🔧 Troubleshooting

### "ANTHROPIC_API_KEY environment variable not set"
- Check if you set the env var: `echo $env:ANTHROPIC_API_KEY` (Windows) or `echo $ANTHROPIC_API_KEY` (Mac/Linux)
- Make sure you used the correct syntax for your shell
- Try setting it again in the current terminal session

### "anthropic package not installed"
```bash
pip install anthropic
```

### "No module named 'parser'"
- Make sure you're running commands from the `whatsapp-eod/` directory
- Check: `cd "f:/Personal Documents/Web Project/whatsapp-eod"`

### Messages not parsing correctly
- Ensure the WhatsApp export is in the standard format: `DD/MM/YYYY, HH:MM - Sender: Message`
- Check the input file encoding is UTF-8
- Run with validation: `python run.py "input/file.txt"` and check the output

### Report quality issues
- Ensure messages contain enough context (at least 20-30 messages recommended)
- Check that messages discuss actual work/progress
- Try adjusting the temperature in summarizer.py (lower = more factual)

## 💰 Cost Estimates

**For typical daily chat (200 messages, ~5000 tokens):**

| Provider | Cost per Report | 100 Reports | Model |
|----------|----------------|-------------|-------|
| Claude (Anthropic) | ~$0.05 | ~$5 | claude-3-5-sonnet |
| GPT-4 (OpenAI) | ~$0.04 | ~$4 | gpt-4o |

**Note**: First-time users often get free credits!

## 📞 Support

If you encounter issues:
1. Check this setup guide
2. Verify API key is set correctly
3. Test with the provided sample file first
4. Check the error message carefully

---

**You're all set! 🎉 Ready to generate professional EOD reports.**

