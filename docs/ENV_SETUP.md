# Environment Variables Setup Guide

## Security Best Practices

**IMPORTANT**: Never commit your `.env` file or API keys to Git! The `.gitignore` file protects you from this.

## Setup Instructions

### 1. Create Your `.env` File

Copy the template below and create a file named `.env` in the project root:

```bash
# Copy this template
cp env.sample .env
# Then edit .env with your actual keys
```

### 2. Environment Variables Template

Create a `.env` file with the following content:

```env
# AI Provider Configuration
# Choose: anthropic, openai, or openrouter
AI_PROVIDER=anthropic

# ============================================
# API Keys (only set the one you're using)
# ============================================

# Get Anthropic key at: https://console.anthropic.com/
ANTHROPIC_API_KEY=your-anthropic-key-here

# Get OpenAI key at: https://platform.openai.com/api-keys
OPENAI_API_KEY=your-openai-key-here

# Get OpenRouter key at: https://openrouter.ai/keys
OPENROUTER_API_KEY=your-openrouter-key-here

# ============================================
# Model Configuration (optional)
# ============================================
# These are optional. If not set, defaults are used.

# Anthropic models: claude-3-5-sonnet-20241022, claude-3-opus-20240229, claude-3-sonnet-20240229
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022

# OpenAI models: gpt-4o, gpt-4-turbo, gpt-4, gpt-3.5-turbo
OPENAI_MODEL=gpt-4o

# OpenRouter models: anthropic/claude-3.5-sonnet, openai/gpt-4o, etc.
OPENROUTER_MODEL=anthropic/claude-3.5-sonnet
```

### 3. Load Environment Variables

#### Option A: Using python-dotenv (Recommended)

Install python-dotenv:
```bash
pip install python-dotenv
```

Add to the top of your Python scripts:
```python
from dotenv import load_dotenv
load_dotenv()  # This loads variables from .env
```

#### Option B: Manual Export (Unix/Mac)

```bash
export AI_PROVIDER=anthropic
export ANTHROPIC_API_KEY=sk-ant-xxxxx
export ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

#### Option C: Manual Export (Windows PowerShell)

```powershell
$env:AI_PROVIDER="anthropic"
$env:ANTHROPIC_API_KEY="sk-ant-xxxxx"
$env:ANTHROPIC_MODEL="claude-3-5-sonnet-20241022"
```

#### Option D: Manual Export (Windows CMD)

```cmd
set AI_PROVIDER=anthropic
set ANTHROPIC_API_KEY=sk-ant-xxxxx
set ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

## Available Models

### Anthropic Claude
- `claude-3-5-sonnet-20241022` (Default, recommended)
- `claude-3-opus-20240229` (Most capable)
- `claude-3-sonnet-20240229` (Balanced)
- `claude-3-haiku-20240307` (Fast & cost-effective)

### OpenAI GPT
- `gpt-4o` (Default, latest)
- `gpt-4-turbo`
- `gpt-4`
- `gpt-3.5-turbo` (Cost-effective)

### OpenRouter
- `anthropic/claude-3.5-sonnet`
- `openai/gpt-4o`
- `google/gemini-pro-1.5`
- And many more at https://openrouter.ai/models

## Verification

To verify your setup, run:

```bash
python scripts/check_setup.py
```

This will check if your environment variables are correctly configured.

## Security Checklist

- ✅ `.env` file is in `.gitignore`
- ✅ Never share API keys in public repositories
- ✅ Rotate keys if accidentally exposed
- ✅ Use separate keys for development/production
- ✅ Monitor API usage for unexpected activity

## Troubleshooting

### Error: "API_KEY environment variable not set"
- Make sure your `.env` file exists in the project root
- Verify the variable name matches exactly (case-sensitive)
- If using python-dotenv, ensure `load_dotenv()` is called
- Try printing `os.getenv("ANTHROPIC_API_KEY")` to debug

### Error: "No module named 'dotenv'"
```bash
pip install python-dotenv
```

### Error: "Invalid API key"
- Check for extra spaces or quotes in your `.env` file
- Verify the key is active at the provider's dashboard
- Generate a new key if needed

