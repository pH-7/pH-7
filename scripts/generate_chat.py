#!/usr/bin/env python3
"""
Dynamic Chat Bot Generator for GitHub README
Generates creative programming-related chat messages

@copyright   (c) Pierre-Henry Soria <https://ph7.me>
@license     MIT <https://opensource.org/license/mit>
"""

import random
import json
from datetime import datetime
import os

class ChatBotGenerator:
    def __init__(self):
        self.config = self.load_config()
        self.programming_tips = [
            "💡 Pro tip: Use meaningful variable names - your future self will thank you!",
            "🚀 Remember: Premature optimization is the root of all evil. Make it work first!",
            "🧠 Clean code is not written by following a set of rules. It's written by programmers who care.",
            "⚡ Small commits with clear messages make debugging a breeze!",
            "🎯 The best code is no code at all. Sometimes deletion > addition.",
            "🔧 Refactoring is like cleaning your room - it feels great afterward!",
            "🌟 Code review is not about finding mistakes, it's about sharing knowledge.",
            "🎨 Good code is like a good joke - if you have to explain it, it's not that good.",
            "📚 Learning never stops in tech. Embrace the journey, not just the destination!",
            "🚀 Build something today, even if it's small. Progress beats perfection!"
        ]

        self.motivational_quotes = [
            "🌅 Today is a great day to write some amazing code!",
            "💪 Every expert was once a beginner. Keep coding, keep growing!",
            "🎯 Focus on progress, not perfection. You've got this!",
            "🌟 Your next breakthrough is just one commit away!",
            "🚀 Dream in code, build in reality, ship with confidence!",
            "💎 Great software is built one line at a time!",
            "🔥 Turn your ideas into code, your code into impact!",
            "⭐ Debugging teaches patience, coding teaches persistence!",
            "🎨 Code is poetry that computers can understand!",
            "🌈 Every bug fixed makes you a stronger developer!"
        ]

        self.personal_insights = [
            "🧀 Fun fact: Nothing beats a good Roquefort while coding - it's my secret fuel! ☕️",
            "☕️ Ristretto + coding = perfect combination for problem-solving sessions!",
            "🍇 Daily fuel check: Learning ✓ Coding ✓ Researching ✓ Fruit ✓ Hiking ✓ Energized! 😊",
            "🤩 Could talk about programming and IT all night - who's up for it?",
            "🧀 True cheese lover here! Roquefort makes every debugging session better!",
            "🍫 Dark chocolate + ristretto = ultimate coding productivity boost!",
            "🥾 Daily hiking keeps the mind sharp for those complex algorithms!",
            "🎯 Problem-solving enthusiast: Every bug is just a puzzle waiting to be solved!",
            "🤖 AI, ML, data science - the future is incredibly exciting! Let's build it!",
            "💫 Passionate engineer fueled by curiosity and great coffee! Reach me at https://ph7.me"
        ]

        self.fun_facts = [
            "🤖 Did you know? The first computer bug was an actual bug - a moth stuck in a relay!",
            "📊 Fun fact: JavaScript was created in just 10 days!",
            "🐍 Python was named after Monty Python's Flying Circus!",
            "☕ Java got its name from the coffee that developers drank while coding!",
            "🔍 The term 'bug' was popularized by Grace Hopper in 1947!",
            "🎮 The first video game was created in 1958 - Tennis for Two!",
            "💻 The '@' symbol was chosen for email because it was rarely used!",
            "🌐 The first website is still online: info.cern.ch!",
            "🔐 'Password' was the most common password for years!",
            "🚀 GitHub processes over 100 million repositories!"
        ]

        self.tech_trends = [
            "🔮 AI is reshaping how we code - embrace the future!",
            "🌊 WebAssembly is making the web faster than ever!",
            "⚡ Edge computing is bringing processing closer to users!",
            "🔗 Blockchain isn't just crypto - it's trust in code!",
            "🎭 Micro-frontends are revolutionizing large applications!",
            "🛡️ Zero-trust security is becoming the new standard!",
            "🌱 Green coding practices help save our planet!",
            "🔄 GitOps is automating deployment workflows!",
            "📱 Progressive Web Apps blur the line between web and native!",
            "🎯 JAMstack delivers lightning-fast user experiences!",
            "🤖 Machine Learning is democratizing AI - exciting times ahead!",
            "📊 Data science is revealing patterns we never knew existed!",
            "🧠 Emerging technologies are opening infinite possibilities!"
        ]

    def load_config(self):
        """Load configuration from JSON file"""
        try:
            with open("config/chat_bot_config.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️ Config file not found, using defaults")
            return self.get_default_config()
        except json.JSONDecodeError:
            print("⚠️ Invalid JSON in config file, using defaults")
            return self.get_default_config()

    def get_default_config(self):
        """Return default configuration if config file is missing"""
        return {
            "chat_bot": {
                "name": "AI Assistant",
                "avatar": "🤖",
                "theme": {
                    "primary_color": "#10a37f",
                    "secondary_color": "#0f7a5c",
                    "accent_color": "#1a9f6e",
                    "text_color": "white",
                    "sparkle_colors": ["#ffd700", "#64748b", "#6366f1", "#8b5cf6"]
                },
                "animation": {
                    "enable_pulse": True,
                    "enable_typing_dots": True,
                    "enable_sparkles": True,
                    "enable_floating_symbols": True,
                    "pulse_duration": "3s",
                    "typing_duration": "1.8s"
                },
                "message_types": {
                    "programming_tips": {"weight": 25, "enabled": True},
                    "motivational_quotes": {"weight": 20, "enabled": True},
                    "personal_insights": {"weight": 25, "enabled": True},
                    "fun_facts": {"weight": 15, "enabled": True},
                    "tech_trends": {"weight": 15, "enabled": True}
                },
                "contextual_messages": {
                    "weekend_mode": True,
                    "monday_motivation": True,
                    "friday_celebration": True,
                    "time_based_greeting": False
                }
            }
        }

    def get_weighted_message_type(self):
        """Select message type based on configured weights"""
        message_types = self.config["chat_bot"]["message_types"]
        enabled_types = [(name, data)
                         for name, data in message_types.items() if data["enabled"]]

        if not enabled_types:
            return "programming_tips"  # fallback

        # Create weighted list
        weighted_choices = []
        for name, data in enabled_types:
            weighted_choices.extend([name] * data["weight"])

        return random.choice(weighted_choices)

    def get_random_message(self):
        """Get a random message from all categories using configured weights"""
        message_type = self.get_weighted_message_type()

        if message_type == "programming_tips":
            return random.choice(self.programming_tips)
        elif message_type == "motivational_quotes":
            return random.choice(self.motivational_quotes)
        elif message_type == "personal_insights":
            return random.choice(self.personal_insights)
        elif message_type == "fun_facts":
            return random.choice(self.fun_facts)
        elif message_type == "tech_trends":
            return random.choice(self.tech_trends)
        else:
            return random.choice(self.programming_tips)  # fallback

    def get_multiple_messages(self, count=3):
        """Get multiple diverse messages for animated sequence"""
        messages = []
        used_types = []

        for i in range(count):
            # Try to get different message types for variety
            attempts = 0
            while attempts < 10:  # Prevent infinite loop
                message_type = self.get_weighted_message_type()
                if message_type not in used_types or len(used_types) >= 5:
                    used_types.append(message_type)
                    break
                attempts += 1

            if message_type == "programming_tips":
                messages.append(random.choice(self.programming_tips))
            elif message_type == "motivational_quotes":
                messages.append(random.choice(self.motivational_quotes))
            elif message_type == "personal_insights":
                messages.append(random.choice(self.personal_insights))
            elif message_type == "fun_facts":
                messages.append(random.choice(self.fun_facts))
            elif message_type == "tech_trends":
                messages.append(random.choice(self.tech_trends))
            else:
                messages.append(random.choice(self.programming_tips))

        return messages

    def get_contextual_message(self):
        """Get a message based on current context (day, time, etc.) if enabled"""
        contextual_config = self.config["chat_bot"]["contextual_messages"]
        now = datetime.now()
        day_of_week = now.weekday()  # 0 = Monday, 6 = Sunday
        hour = now.hour

        # Weekend vibes
        # Saturday or Sunday
        if day_of_week >= 5 and contextual_config.get("weekend_mode", True):
            weekend_messages = [
                "🏖️ Weekend coding sessions hit different - what are you building?",
                "☕ Perfect weekend for a side project and some good ristretto!",
                "🎮 Weekend hack: Try building something fun, not just functional!",
                "🌟 Weekends are for experimenting with that new framework!",
                "📚 Great time to dive deep into that tech book you've been meaning to read!",
                "🧀 Weekend fuel: Roquefort, ristretto, and some quality coding time!",
                "🥾 Perfect day for a hike followed by some AI/ML exploration!",
                "🍇 Weekend energy: Learning + coding + fruit + fresh air = happiness! 😊"
            ]
            return random.choice(weekend_messages)

        # Monday motivation
        # Monday
        elif day_of_week == 0 and contextual_config.get("monday_motivation", True):
            monday_messages = [
                "💪 Monday Motivation: This week, let's ship something amazing!",
                "🚀 New week, new features to build! What's on your roadmap?",
                "⚡ Monday Energy: Time to turn those weekend ideas into code!",
                "🎯 Week Goals: Learn something new, build something cool!",
                "🌟 Fresh start, fresh commits! Let's make this week count!",
                "☕ Monday ristretto + passionate problem-solving = perfect combo!",
                "🧀 New week fuel: Enthusiasm, curiosity, and maybe some good cheese! 😋"
            ]
            return random.choice(monday_messages)

        # Friday celebration
        # Friday
        elif day_of_week == 4 and contextual_config.get("friday_celebration", True):
            friday_messages = [
                "🎉 Friday Deploy: Hope your code is as solid as your weekend plans!",
                "🍻 TGIF - Time to Git Integrate Friday's features!",
                "🎊 Friday feeling: Your commits this week were fantastic!",
                "🌈 End the week strong - one last push before the weekend!",
                "🎈 Friday vibes: Celebrate every bug you squashed this week!"
            ]
            return random.choice(friday_messages)

        # Default to weighted random message
        return self.get_random_message()

    def generate_svg_chat(self, messages):
        """Generate an animated SVG with multiple chat messages using configured theme"""
        theme = self.config["chat_bot"]["theme"]
        animation = self.config["chat_bot"]["animation"]
        avatar = self.config["chat_bot"]["avatar"]

        # Handle both single message and multiple messages
        if isinstance(messages, str):
            messages = [messages]

        # Calculate dimensions based on longest message
        max_length = max(len(msg) for msg in messages)
        bubble_width = min(max(max_length * 8, 300), 550)
        svg_width = bubble_width + 100

        # Split messages into lines
        all_lines = []
        for message in messages:
            words = message.split()
            lines = []
            current_line = ""
            max_chars_per_line = 50

            for word in words:
                if len(current_line + " " + word) <= max_chars_per_line:
                    current_line += (" " + word) if current_line else word
                else:
                    if current_line:
                        lines.append(current_line)
                    current_line = word

            if current_line:
                lines.append(current_line)
            all_lines.append(lines)

        # Calculate height for the largest message
        max_lines = max(len(lines) for lines in all_lines)
        bubble_height = 40 + (max_lines * 16)
        svg_height = max(bubble_height + 40, 140)

        # Generate sparkle colors
        sparkle_colors = theme.get(
            "sparkle_colors", ["#ffd700", "#64748b", "#6366f1", "#8b5cf6"])
        sparkle_color = random.choice(sparkle_colors)

        # Check if multiple messages are enabled
        multiple_enabled = animation.get("multiple_messages", False)
        message_delay = animation.get("message_delay", "4s")

        # Generate standalone SVG content
        svg_content = f'''<!--
/**
 * @copyright   (c) Pierre-Henry Soria <https://ph7.me>
 * @license     MIT <https://opensource.org/license/mit>
 */
-->
<svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">
    <!-- Enhanced ChatGPT-style bubble animation -->
    <defs>
      <style>
        .ai-bubble {{
          fill: url(#bubbleGradient);
          filter: drop-shadow(0 4px 8px rgba(0,0,0,0.1));'''

        # Add pulse animation if enabled
        if animation.get("enable_pulse", True):
            svg_content += f'''
          animation: ai-pulse {animation.get("pulse_duration", "3s")} ease-in-out infinite alternate;'''

        svg_content += f'''
        }}
        .ai-text {{
          fill: {theme.get("text_color", "white")};
          font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
          font-size: 13px;
          font-weight: 500;
        }}'''

        # Add typing dots animation if enabled
        if animation.get("enable_typing_dots", True):
            svg_content += f'''
        .typing-dots {{
          fill: rgba(255,255,255,0.8);
          animation: typing-bounce {animation.get("typing_duration", "1.8s")} infinite;
        }}
        .dot1 {{ animation-delay: 0s; }}
        .dot2 {{ animation-delay: 0.3s; }}
        .dot3 {{ animation-delay: 0.6s; }}'''

        svg_content += f'''
        .ai-avatar {{
          fill: {theme.get("primary_color", "#10a37f")};
          animation: avatar-glow 4s ease-in-out infinite;
        }}'''

        # Add sparkle animation if enabled
        if animation.get("enable_sparkles", True):
            svg_content += f'''
        .sparkle {{
          fill: {sparkle_color};
          animation: sparkle-twinkle 2s ease-in-out infinite;
        }}'''

        # Add floating symbols animation if enabled
        if animation.get("enable_floating_symbols", True):
            svg_content += f'''
        .code-symbols {{
          font-family: 'Fira Code', 'JetBrains Mono', monospace;
          font-weight: bold;
          animation: float-rotate 6s ease-in-out infinite;
        }}'''

        # Add message cycling animation if multiple messages
        if multiple_enabled and len(messages) > 1:
            svg_content += f'''
        .message-group {{
          animation: message-cycle {len(messages) * 4}s infinite;
          opacity: 0;
        }}
        .message-group-1 {{ animation-delay: 0s; }}
        .message-group-2 {{ animation-delay: {message_delay}; }}
        .message-group-3 {{ animation-delay: {float(message_delay.replace('s', '')) * 2}s; }}'''

        # Add keyframes animations
        svg_content += f'''
        
        @keyframes ai-pulse {{
          0% {{ transform: scale(1) translateY(0px); opacity: 0.9; }}
          100% {{ transform: scale(1.02) translateY(-2px); opacity: 1; }}
        }}
        
        @keyframes typing-bounce {{
          0%, 60%, 100% {{ opacity: 0.3; transform: translateY(0px); }}
          30% {{ opacity: 1; transform: translateY(-4px); }}
        }}
        
        @keyframes avatar-glow {{
          0%, 100% {{ filter: drop-shadow(0 0 8px rgba(16,163,127,0.3)); }}
          50% {{ filter: drop-shadow(0 0 16px rgba(16,163,127,0.6)); }}
        }}
        
        @keyframes sparkle-twinkle {{
          0%, 100% {{ opacity: 0.4; transform: scale(1) rotate(0deg); }}
          50% {{ opacity: 1; transform: scale(1.2) rotate(180deg); }}
        }}
        
        @keyframes float-rotate {{
          0%, 100% {{ transform: translateY(0px) rotate(0deg); opacity: 0.6; }}
          33% {{ transform: translateY(-8px) rotate(120deg); opacity: 0.8; }}
          66% {{ transform: translateY(-4px) rotate(240deg); opacity: 0.7; }}
        }}'''

        if multiple_enabled and len(messages) > 1:
            # Calculate timing for smooth transitions
            display_duration = 25  # % of cycle time each message is visible
            transition_duration = 5  # % for fade transitions
            svg_content += f'''

        @keyframes message-cycle {{
          0%, {display_duration}% {{ opacity: 1; }}
          {display_duration + transition_duration}%, {100 - transition_duration}% {{ opacity: 0; }}
          100% {{ opacity: 0; }}
        }}'''

        svg_content += f'''
      </style>
      
      <!-- Gradient definitions -->
      <linearGradient id="bubbleGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{theme.get('primary_color', '#10a37f')};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{theme.get('secondary_color', '#0f7a5c')};stop-opacity:1" />
      </linearGradient>
      
      <linearGradient id="avatarGradient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" style="stop-color:{theme.get('primary_color', '#10a37f')};stop-opacity:1" />
        <stop offset="100%" style="stop-color:{theme.get('accent_color', '#1a9f6e')};stop-opacity:1" />
      </linearGradient>
    </defs>
    
    <!-- AI Avatar Circle -->
    <circle class="ai-avatar" cx="35" cy="35" r="20" fill="url(#avatarGradient)"/>
    <text x="35" y="42" text-anchor="middle" style="fill: {theme.get('text_color', 'white')}; font-size: 16px; font-weight: bold;">{avatar}</text>
    
    <!-- Main chat bubble with dynamic sizing -->
    <path class="ai-bubble" d="M65 20 Q70 15 80 15 L{bubble_width-10} 15 Q{bubble_width} 15 {bubble_width} 25 L{bubble_width} {bubble_height-10} Q{bubble_width} {bubble_height} {bubble_width-10} {bubble_height} L85 {bubble_height} L70 {bubble_height+10} L70 {bubble_height} Q65 {bubble_height} 65 {bubble_height-10} Z"/>
    
    <!-- Chat text lines -->'''

        # Add text content - support multiple messages or single message
        if multiple_enabled and len(messages) > 1:
            # Multiple messages with cycling animation
            for msg_idx, lines in enumerate(all_lines, 1):
                svg_content += f'\n    <g class="message-group message-group-{msg_idx}">'
                for i, line in enumerate(lines):
                    y_pos = 35 + (i * 16)
                    svg_content += f'\n      <text x="80" y="{y_pos}" class="ai-text">{line}</text>'
                svg_content += '\n    </g>'
        else:
            # Single message (use first message if multiple provided)
            lines = all_lines[0]
            for i, line in enumerate(lines):
                y_pos = 35 + (i * 16)
                svg_content += f'\n    <text x="80" y="{y_pos}" class="ai-text">{line}</text>'

        # Add typing indicator (use longest message for positioning)
        indicator_y = 35 + (max_lines * 16) + 10
        svg_content += f'''
    
    <!-- Typing indicator -->
    <circle class="typing-dots dot1" cx="{bubble_width-40}" cy="{indicator_y}" r="2.5"/>
    <circle class="typing-dots dot2" cx="{bubble_width-28}" cy="{indicator_y}" r="2.5"/>
    <circle class="typing-dots dot3" cx="{bubble_width-16}" cy="{indicator_y}" r="2.5"/>
    
    <!-- Floating sparkles -->
    <text x="15" y="25" class="sparkle" style="font-size: 12px;">✨</text>
    <text x="{svg_width-25}" y="30" class="sparkle" style="font-size: 10px; animation-delay: 1s;">⭐</text>
    <text x="{svg_width-30}" y="70" class="sparkle" style="font-size: 8px; animation-delay: 1.5s;">💫</text>
    
    <!-- Floating code symbols -->
    <text x="20" y="{svg_height-20}" class="code-symbols" style="fill: #64748b; font-size: 14px; animation-delay: 0.5s;">&lt;/&gt;</text>
    <text x="{svg_width-40}" y="{svg_height-25}" class="code-symbols" style="fill: #6366f1; font-size: 12px; animation-delay: 1.2s;">{{ }}</text>
    <text x="{svg_width//2}" y="{svg_height-15}" class="code-symbols" style="fill: #8b5cf6; font-size: 10px; animation-delay: 2s;">=&gt;</text>
</svg>'''

        return svg_content

    def generate_readme_svg_reference(self, message):
        """Generate a simple SVG reference for README (without embedded styles)"""
        return f'<div align="center">\n  <img src="chat_bubble.svg" alt="AI Chat Bubble" />\n</div>'


def main():
    """Main function to generate and save the chat content"""
    generator = ChatBotGenerator()

    # Check if multiple messages are enabled
    animation_config = generator.config["chat_bot"]["animation"]
    multiple_enabled = animation_config.get("multiple_messages", False)

    if multiple_enabled:
        # Get multiple messages for cycling animation
        message_count = animation_config.get("message_count", 3)
        messages = generator.get_multiple_messages(message_count)
        primary_message = messages[0]  # First message for JSON storage
    else:
        # Get a single contextual message
        messages = generator.get_contextual_message()
        primary_message = messages

    # Generate SVG for standalone file
    svg_content = generator.generate_svg_chat(messages)

    # Generate simple reference for README
    readme_svg = generator.generate_readme_svg_reference(primary_message)

    # Save the message and timestamp
    data = {
        "message": primary_message,
        "svg": readme_svg,  # Use simple reference for README
        "timestamp": datetime.now().isoformat(),
        "last_updated": datetime.now().strftime("%B %d, %Y at %H:%M UTC")
    }

    if multiple_enabled:
        data["all_messages"] = messages

    # Ensure the data directory exists
    os.makedirs("data", exist_ok=True)

    # Save to JSON file
    with open("data/chat_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Save standalone SVG file
    with open("chat_bubble.svg", "w", encoding="utf-8") as f:
        f.write(svg_content)

    print(f"✅ Generated new chat message: {primary_message[:50]}...")
    print(f"📅 Timestamp: {data['last_updated']}")
    print(f"🎨 Created standalone SVG: chat_bubble.svg")

    if multiple_enabled:
        print(f"🔄 Multiple messages mode: {len(messages)} messages cycling")

    return data


if __name__ == "__main__":
    main()
