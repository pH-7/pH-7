#!/usr/bin/env python3
"""
README Updater for Dynamic Chat Bot
Updates the README.md file with the latest generated chat content
"""

import json
import re
import os
from datetime import datetime

def load_config():
    """Load configuration from JSON file"""
    try:
        with open("config/chat_bot_config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Config file not found, using defaults")
        return {
            "readme": {
                "insert_position": "after_subtitle",
                "include_timestamp": True,
                "include_message_preview": True,
                "section_markers": {
                    "start": "<!-- DYNAMIC_CHAT:START -->",
                    "end": "<!-- DYNAMIC_CHAT:END -->"
                }
            }
        }
    except json.JSONDecodeError:
        print("⚠️ Invalid JSON in config file, using defaults")
        return {
            "readme": {
                "insert_position": "after_subtitle",
                "include_timestamp": True,
                "include_message_preview": True,
                "section_markers": {
                    "start": "<!-- DYNAMIC_CHAT:START -->",
                    "end": "<!-- DYNAMIC_CHAT:END -->"
                }
            }
        }

def load_chat_data():
    """Load the latest chat data from JSON file"""
    try:
        with open("data/chat_data.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Chat data file not found. Please run generate_chat.py first.")
        return None
    except json.JSONDecodeError:
        print("❌ Invalid JSON in chat data file.")
        return None

def update_readme(chat_data):
    """Update the README.md file with new chat content"""
    if not chat_data:
        return False
    
    # Load configuration
    config = load_config()
    readme_config = config.get("readme", {})
    
    try:
        # Read current README
        with open("README.md", "r", encoding="utf-8") as f:
            readme_content = f.read()
        
        # Get section markers from config
        markers = readme_config.get("section_markers", {})
        start_marker = markers.get("start", "<!-- DYNAMIC_CHAT:START -->")
        end_marker = markers.get("end", "<!-- DYNAMIC_CHAT:END -->")
        
        # Create the new chat section content
        chat_section_content = f"{chat_data['svg']}"
        
        # Add message preview if enabled
        if readme_config.get("include_message_preview", True):
            chat_section_content += f'\n\n<div align="center">\n  <em>🤖 AI Bot says: "{chat_data["message"]}"</em>'
        
        # Add timestamp if enabled  
        if readme_config.get("include_timestamp", True):
            if readme_config.get("include_message_preview", True):
                chat_section_content += f'<br>\n  <small>Last updated: {chat_data["last_updated"]}</small>\n</div>'
            else:
                chat_section_content += f'\n\n<div align="center">\n  <small>Last updated: {chat_data["last_updated"]}</small>\n</div>'
        elif readme_config.get("include_message_preview", True):
            chat_section_content += '\n</div>'
        
        new_chat_section = f"""{start_marker}
{chat_section_content}
{end_marker}"""
        
        # Check if markers exist
        if start_marker in readme_content and end_marker in readme_content:
            # Replace existing content between markers
            pattern = f"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
            updated_content = re.sub(pattern, new_chat_section, readme_content, flags=re.DOTALL)
        else:
            # Add the chat section after the main header
            # Find the position after the first main header and subtitle
            header_pattern = r"(### 🎡 𝗣𝗮𝘀𝘀𝗶𝗼𝗻𝗮𝘁𝗲 Creative 𝗦𝗼𝗳𝘁𝘄𝗮𝗿𝗲 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿 💡\n\n)"
            
            if re.search(header_pattern, readme_content):
                updated_content = re.sub(
                    header_pattern,
                    r"\1" + new_chat_section + "\n\n",
                    readme_content,
                    count=1
                )
            else:
                # Fallback: add at the beginning after the title
                lines = readme_content.split('\n')
                # Find the first empty line after the title
                insert_index = 3  # Default position
                for i, line in enumerate(lines[:10]):  # Check first 10 lines
                    if i > 2 and line.strip() == "":
                        insert_index = i
                        break
                
                lines.insert(insert_index, new_chat_section)
                lines.insert(insert_index + 1, "")
                updated_content = '\n'.join(lines)
        
        # Write the updated README
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(updated_content)
        
        print("✅ README.md updated successfully!")
        print(f"📝 New message: {chat_data['message'][:80]}...")
        return True
        
    except Exception as e:
        print(f"❌ Error updating README: {e}")
        return False

def main():
    """Main function"""
    print("🤖 Starting README update process...")
    
    # Load chat data
    chat_data = load_chat_data()
    if not chat_data:
        return False
    
    # Update README
    success = update_readme(chat_data)
    
    if success:
        print("🎉 README update completed successfully!")
        print("📋 Configuration settings applied from chat_bot_config.json")
    else:
        print("❌ README update failed!")
    
    return success

if __name__ == "__main__":
    main()
