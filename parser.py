import re
import json
import sys
from datetime import datetime

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

def clean_whatsapp_text(text):
    """Remove WhatsApp special Unicode characters (directional marks, etc.)"""
    # Remove invisible Unicode characters used in WhatsApp mentions
    # U+2068 (FIRST STRONG ISOLATE), U+2069 (POP DIRECTIONAL ISOLATE)
    text = text.replace('\u2068', '').replace('\u2069', '')
    return text.strip()


def parse_whatsapp_chat(file_path):
    """
    Parse WhatsApp exported chat TXT file.
    
    Args:
        file_path: Path to the WhatsApp chat export file
        
    Returns:
        List of dictionaries with keys: timestamp, sender, message
    """
    # Regex pattern for WhatsApp message line: DD/MM/YYYY, HH:MM - Sender: Message
    message_pattern = re.compile(r'^(\d{2}/\d{2}/\d{4}, \d{2}:\d{2}) - ([^:]+): (.*)$')
    
    messages = []
    current_message = None
    
    # System message indicators to filter out
    system_indicators = [
        'Messages and calls are end-to-end encrypted',
        'created group',
        'added you',
        'added ',
        'removed ',
        'changed the subject',
        'changed this group\'s icon',
        'changed their phone number',
        'left',
        'joined using this group\'s invite link',
        'You created group',
        'security code changed'
    ]
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')
            
            # Try to match a new message line
            match = message_pattern.match(line)
            
            if match:
                # Save previous message if exists
                if current_message:
                    messages.append(current_message)
                
                timestamp_str = match.group(1)
                sender = clean_whatsapp_text(match.group(2))
                message_text = clean_whatsapp_text(match.group(3))
                
                # Check if this is a system message (no colon after sender or contains system indicators)
                is_system = any(indicator in line for indicator in system_indicators)
                
                # Also filter messages without proper sender format (system messages)
                if not is_system:
                    current_message = {
                        'timestamp': timestamp_str,
                        'sender': sender,
                        'message': message_text
                    }
                else:
                    current_message = None
            else:
                # Continuation of previous message (multi-line)
                if current_message and line.strip():
                    current_message['message'] += '\n' + clean_whatsapp_text(line)
        
        # Don't forget the last message
        if current_message:
            messages.append(current_message)
    
    return messages


def save_to_json(messages, output_path):
    """Save parsed messages to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    print(f"✓ Saved {len(messages)} messages to {output_path}")


def validate_messages(messages, num_to_show=10):
    """Validate and display first N messages"""
    print(f"\n{'='*60}")
    print(f"VALIDATION: Showing first {num_to_show} messages")
    print(f"{'='*60}\n")
    
    for i, msg in enumerate(messages[:num_to_show], 1):
        print(f"[{i}] {msg['timestamp']}")
        print(f"    Sender: {msg['sender']}")
        print(f"    Message: {msg['message'][:100]}{'...' if len(msg['message']) > 100 else ''}")
        print()
    
    print(f"{'='*60}")
    print(f"Total messages parsed: {len(messages)}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    # Example usage
    input_file = "input/Netcore & Convx - QSR Team - test text.txt"
    output_file = "output/parsed_messages.json"
    
    try:
        print("Parsing WhatsApp chat...")
        messages = parse_whatsapp_chat(input_file)
        
        # Validate
        validate_messages(messages, num_to_show=10)
        
        # Save to JSON
        save_to_json(messages, output_file)
        
        print("✓ Parsing complete! No crashes detected.")
        
    except Exception as e:
        print(f"✗ ERROR: {e}")
        raise

