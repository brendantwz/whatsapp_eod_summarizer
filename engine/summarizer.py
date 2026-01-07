"""
WhatsApp Chat Summarizer - AI-Powered EOD Report Generator

Converts parsed WhatsApp messages into structured end-of-day construction site reports.
"""

import json
import os
import sys
from datetime import datetime
from .parser import parse_whatsapp_chat

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load .env file from project root
except ImportError:
    # python-dotenv not installed, will use system environment variables
    pass


# AI Provider Configuration
AI_PROVIDER = os.getenv("AI_PROVIDER", "anthropic")  # "anthropic", "openai", or "openrouter"

# Model Configuration (with sensible defaults)
DEFAULT_ANTHROPIC_MODEL = "claude-3-5-sonnet-20241022"
DEFAULT_OPENAI_MODEL = "gpt-4o"
DEFAULT_OPENROUTER_MODEL = "anthropic/claude-3.5-sonnet"

ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", DEFAULT_ANTHROPIC_MODEL)
OPENAI_MODEL = os.getenv("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", DEFAULT_OPENROUTER_MODEL)

# API Key mapping based on provider
if AI_PROVIDER == "anthropic":
    API_KEY = os.getenv("ANTHROPIC_API_KEY")
elif AI_PROVIDER == "openai":
    API_KEY = os.getenv("OPENAI_API_KEY")
elif AI_PROVIDER == "openrouter":
    API_KEY = os.getenv("OPENROUTER_API_KEY")
else:
    API_KEY = None


def format_messages_for_ai(messages):
    """Convert parsed messages into readable text for AI processing"""
    formatted = []
    for msg in messages:
        formatted.append(f"[{msg['timestamp']}] {msg['sender']}: {msg['message']}")
    return "\n".join(formatted)


def extract_date_from_messages(messages):
    """Extract the primary date from messages (most common date)"""
    if not messages:
        return datetime.now().strftime("%d/%m/%Y")
    
    # Get the first message date as primary
    first_timestamp = messages[0]['timestamp']
    date_part = first_timestamp.split(',')[0]
    return date_part


def create_eod_prompt(messages, site_name=None):
    """Create the AI prompt for EOD report generation"""
    
    formatted_messages = format_messages_for_ai(messages)
    date = extract_date_from_messages(messages)
    
    site_instruction = f'Site name: "{site_name}"' if site_name else "Extract site name from context (if mentioned)"
    
    prompt = f"""You are analyzing WhatsApp messages from a construction site team. Your task is to generate a professional end-of-day (EOD) report.

CRITICAL RULES:
- Do NOT invent facts or information not present in the messages
- If a section has no relevant information, write "No updates" or "None identified"
- Group similar updates together logically
- Highlight delays and risks with clear, direct language
- Use professional, executive tone
- Keep the report to maximum 1 page when formatted
- Extract concrete deliverables, timelines, and action items
- Only include messages in the last 24 hours
- Provide context on previous days work and progress if needed

{site_instruction}
Report date: {date}

WHATSAPP MESSAGES:
{formatted_messages}

Generate a report using EXACTLY this structure:

## Site: [Extract or use provided site name]
## Date: {date}

### 1. Overall Site Status
[One concise paragraph summarizing the day's overall progress, mood, and key themes]

### 2. Work Completed Today
[List specific completed tasks and deliverables as bullet points]
- [If none mentioned, write "No completed work explicitly mentioned"]

### 3. Issues / Delays
[List any problems, blockers, or delays mentioned]
- [If none, write "None reported"]

### 4. Risks / Attention Required
[List potential risks, concerns, or items needing management attention]
- **[Use bold for CRITICAL items]**
- [If none, write "None identified"]

### 5. Tomorrow's Planned Work
[List scheduled work, meetings, or planned activities]
- [If none mentioned, write "No explicit plans mentioned"]

### 6. Decisions Needed
[List any decisions awaiting management input or approval]
- [If none, write "None identified"]

Generate the report now:"""
    
    return prompt


def summarize_with_anthropic(messages, site_name=None, model=None):
    """Generate EOD report using Anthropic Claude API"""
    model = model or ANTHROPIC_MODEL
    try:
        import anthropic
    except ImportError:
        print("❌ ERROR: anthropic package not installed.")
        print("Install with: pip install anthropic")
        sys.exit(1)
    
    if not API_KEY:
        print("❌ ERROR: ANTHROPIC_API_KEY environment variable not set.")
        print("Set it with: export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)
    
    client = anthropic.Anthropic(api_key=API_KEY)
    prompt = create_eod_prompt(messages, site_name)
    
    print("🤖 Generating EOD report with Claude...")
    
    message = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text


def summarize_with_openai(messages, site_name=None, model=None):
    """Generate EOD report using OpenAI API"""
    model = model or OPENAI_MODEL
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ ERROR: openai package not installed.")
        print("Install with: pip install openai")
        sys.exit(1)
    
    if not API_KEY:
        print("❌ ERROR: OPENAI_API_KEY environment variable not set.")
        print("Set it with: export OPENAI_API_KEY='your-key-here'")
        sys.exit(1)
    
    client = OpenAI(api_key=API_KEY)
    prompt = create_eod_prompt(messages, site_name)
    
    print("🤖 Generating EOD report with GPT-4...")
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a professional construction project manager creating end-of-day reports."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.3
    )
    
    return response.choices[0].message.content


def summarize_with_openrouter(messages, site_name=None, model=None):
    """Generate EOD report using OpenRouter API"""
    model = model or OPENROUTER_MODEL
    try:
        from openai import OpenAI
    except ImportError:
        print("❌ ERROR: openai package not installed.")
        print("Install with: pip install openai")
        sys.exit(1)
    
    if not API_KEY:
        print("❌ ERROR: OPENROUTER_API_KEY environment variable not set.")
        print("Set it with: export OPENROUTER_API_KEY='your-key-here'")
        print("Get your key at: https://openrouter.ai/keys")
        sys.exit(1)
    
    # OpenRouter uses OpenAI-compatible API
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY
    )
    prompt = create_eod_prompt(messages, site_name)
    
    print(f"🤖 Generating EOD report with OpenRouter ({model})...")
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a professional construction project manager creating end-of-day reports."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000,
        temperature=0.3
    )
    
    return response.choices[0].message.content


def generate_eod_report(messages, site_name=None, provider=None):
    """
    Generate EOD report from parsed messages
    
    Args:
        messages: List of parsed message dictionaries
        site_name: Optional site name override
        provider: "anthropic", "openai", or "openrouter" (defaults to AI_PROVIDER env var)
    
    Returns:
        Formatted EOD report as markdown string
    """
    if not messages:
        return "❌ ERROR: No messages to summarize"
    
    provider = provider or AI_PROVIDER
    
    if provider == "anthropic":
        return summarize_with_anthropic(messages, site_name)
    elif provider == "openai":
        return summarize_with_openai(messages, site_name)
    elif provider == "openrouter":
        return summarize_with_openrouter(messages, site_name)
    else:
        return f"❌ ERROR: Unknown AI provider '{provider}'. Use 'anthropic', 'openai', or 'openrouter'"


def save_report(report, output_path):
    """Save the generated report to a markdown file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Report saved to: {output_path}")


def main():
    """Main entry point for CLI usage"""
    if len(sys.argv) < 2:
        print("Usage: python summarizer.py <parsed_json_file> [site_name] [output_file]")
        print("\nExamples:")
        print('  python summarizer.py "output/parsed_messages.json"')
        print('  python summarizer.py "output/parsed_messages.json" "Site A Construction"')
        print('  python summarizer.py "output/parsed_messages.json" "Site A" "reports/eod_report.md"')
        print("\nEnvironment Variables:")
        print("  AI_PROVIDER=anthropic, openai, or openrouter (default: anthropic)")
        print("  ANTHROPIC_API_KEY=your-api-key")
        print("  OPENAI_API_KEY=your-api-key")
        print("  OPENROUTER_API_KEY=your-api-key")
        sys.exit(1)
    
    input_file = sys.argv[1]
    site_name = sys.argv[2] if len(sys.argv) >= 3 else None
    
    # Generate output filename if not provided
    if len(sys.argv) >= 4:
        output_file = sys.argv[3]
    else:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"output/{base_name}_eod_report.md"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        print(f"📄 Loading parsed messages from: {input_file}")
        
        # Load parsed messages
        with open(input_file, 'r', encoding='utf-8') as f:
            messages = json.load(f)
        
        print(f"✅ Loaded {len(messages)} messages")
        print(f"📅 Date range: {messages[0]['timestamp']} to {messages[-1]['timestamp']}")
        print()
        
        # Generate report
        report = generate_eod_report(messages, site_name)
        
        print("\n" + "="*60)
        print("GENERATED EOD REPORT")
        print("="*60 + "\n")
        print(report)
        print("\n" + "="*60 + "\n")
        
        # Save report
        save_report(report, output_file)
        
        print("✅ SUCCESS! EOD report generation complete.")
        
    except FileNotFoundError:
        print(f"❌ ERROR: File not found: {input_file}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ ERROR: Invalid JSON file: {input_file}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

