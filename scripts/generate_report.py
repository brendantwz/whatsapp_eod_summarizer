"""
Complete End-to-End EOD Report Generator

This script combines parsing and summarization into one command.
Usage: python generate_report.py "input/chat.txt" [site_name]
"""

import sys
import os

# Add parent directory to path to import from engine
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from engine.parser import parse_whatsapp_chat, save_to_json, validate_messages
from engine.summarizer import generate_eod_report, save_report


def main():
    if len(sys.argv) < 2:
        print("=" * 70)
        print("WhatsApp EOD Report Generator - Complete Pipeline")
        print("=" * 70)
        print("\nUsage: python generate_report.py <input_file> [site_name]")
        print("\nExamples:")
        print('  python generate_report.py "input/team-chat.txt"')
        print('  python generate_report.py "input/team-chat.txt" "Site A Construction"')
        print("\nEnvironment Variables Required:")
        print("  AI_PROVIDER=anthropic or openai")
        print("  ANTHROPIC_API_KEY=your-key (if using Claude)")
        print("  OPENAI_API_KEY=your-key (if using GPT-4)")
        print("\nOutput:")
        print("  - Parsed JSON: output/<filename>_parsed.json")
        print("  - EOD Report: output/<filename>_eod_report.md")
        print("=" * 70)
        sys.exit(1)
    
    input_file = sys.argv[1]
    site_name = sys.argv[2] if len(sys.argv) >= 3 else None
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"❌ ERROR: File not found: {input_file}")
        sys.exit(1)
    
    # Generate output filenames
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    json_output = f"output/{base_name}_parsed.json"
    report_output = f"output/{base_name}_eod_report.md"
    
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    print("=" * 70)
    print("STEP 1: PARSING WHATSAPP CHAT")
    print("=" * 70)
    print()
    
    try:
        # Step 1: Parse WhatsApp chat
        print(f"📱 Parsing: {input_file}")
        messages = parse_whatsapp_chat(input_file)
        
        # Validate
        validate_messages(messages, num_to_show=5)
        
        # Save parsed JSON
        save_to_json(messages, json_output)
        
        print("\n" + "=" * 70)
        print("STEP 2: GENERATING EOD REPORT")
        print("=" * 70)
        print()
        
        # Step 2: Generate EOD report
        print(f"🤖 Analyzing {len(messages)} messages with AI...")
        if site_name:
            print(f"📍 Site: {site_name}")
        print()
        
        report = generate_eod_report(messages, site_name)
        
        # Display report
        print("\n" + "=" * 70)
        print("GENERATED EOD REPORT")
        print("=" * 70 + "\n")
        print(report)
        print("\n" + "=" * 70 + "\n")
        
        # Save report
        save_report(report, report_output)
        
        print("\n" + "=" * 70)
        print("✅ SUCCESS! Complete pipeline executed.")
        print("=" * 70)
        print(f"\n📁 Parsed data: {json_output}")
        print(f"📄 EOD Report: {report_output}")
        print("\n✅ Ready to share!\n")
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

