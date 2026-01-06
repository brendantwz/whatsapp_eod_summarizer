"""
WhatsApp Chat Parser - Main Entry Point

Usage:
    python run.py <input_file> [output_file]

Example:
    python run.py "input/chat.txt"
    python run.py "input/chat.txt" "output/parsed.json"
"""

import sys
import os

# Add parent directory to path to import from engine
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from engine.parser import parse_whatsapp_chat, save_to_json, validate_messages


def main():
    # Check if input file is provided
    if len(sys.argv) < 2:
        print("Usage: python run.py <input_file> [output_file]")
        print("\nExample:")
        print('  python run.py "input/Netcore & Convx - QSR Team - test text.txt"')
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(input_file):
        print(f"✗ ERROR: File not found: {input_file}")
        sys.exit(1)
    
    # Generate output filename if not provided
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    else:
        base_name = os.path.splitext(os.path.basename(input_file))[0]
        output_file = f"output/{base_name}_parsed.json"
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    try:
        print(f"📱 Parsing WhatsApp chat: {input_file}")
        print()
        
        # Parse the chat
        messages = parse_whatsapp_chat(input_file)
        
        # Validate and show first 10 messages
        validate_messages(messages, num_to_show=10)
        
        # Save to JSON
        save_to_json(messages, output_file)
        
        print()
        print("✅ SUCCESS! Parsing complete with no crashes.")
        print(f"✅ Messages are clean and ready for summarization.")
        print(f"✅ Output saved to: {output_file}")
        
        return messages
        
    except Exception as e:
        print(f"✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

