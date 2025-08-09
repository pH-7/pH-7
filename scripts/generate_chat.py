#!/usr/bin/env python3
"""
Dynamic Chat Bot Generator for GitHub README
Generates creative programming-related chat messages

@copyright   (c) Pierre-Henry Soria <https://ph7.me>
@license     MIT <https://opensource.org/license/mit>
"""

import random
import json
from datetime import datetime, timedelta
import os
import calendar


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

    def get_dynamic_context(self):
        """Get dynamic real-time context information"""
        now = datetime.now()
        context = {
            'date': now,
            'year': now.year,
            'month': now.month,
            'day': now.day,
            'weekday': now.weekday(),
            'hour': now.hour,
            'season': self.get_season(now),
            'is_holiday': self.check_holidays(now),
            'milestone': self.check_coding_milestones(now),
            'tech_anniversary': self.check_tech_anniversaries(now),
            'moon_phase': self.get_moon_phase(now),
            'developer_day': self.check_developer_special_days(now)
        }
        return context

    def get_season(self, date):
        """Determine current season"""
        month = date.month
        day = date.day
        
        if (month == 12 and day >= 21) or month in [1, 2] or (month == 3 and day < 20):
            return "winter"
        elif (month == 3 and day >= 20) or month in [4, 5] or (month == 6 and day < 21):
            return "spring"
        elif (month == 6 and day >= 21) or month in [7, 8] or (month == 9 and day < 22):
            return "summer"
        else:
            return "autumn"

    def check_holidays(self, date):
        """Check for major holidays and special occasions"""
        month, day = date.month, date.day
        
        holidays = {
            (1, 1): "New Year's Day 🎆",
            (2, 14): "Valentine's Day 💝",
            (3, 17): "St. Patrick's Day 🍀",
            (4, 1): "April Fools' Day 😄",
            (5, 1): "May Day 🌸",
            (7, 4): "Independence Day 🇺🇸",
            (10, 31): "Halloween 🎃",
            (12, 24): "Christmas Eve 🎄",
            (12, 25): "Christmas Day 🎅",
            (12, 31): "New Year's Eve 🎊"
        }
        
        # Dynamic holidays (Easter, Thanksgiving, etc.)
        year = date.year
        
        # Thanksgiving (4th Thursday of November in US)
        if month == 11:
            first_day = datetime(year, 11, 1)
            first_thursday = 1 + (3 - first_day.weekday()) % 7
            thanksgiving = first_thursday + 21  # 4th Thursday
            if day == thanksgiving:
                return "Thanksgiving 🦃"
        
        # Check basic holidays
        return holidays.get((month, day))

    def check_coding_milestones(self, date):
        """Check for coding and tech milestones"""
        year, month, day = date.year, date.month, date.day
        
        milestones = {
            (1, 3): f"🎂 Happy Birthday to JavaScript! Born in 1995 - {year - 1995} years of powering the web!",
            (2, 19): f"💎 Ruby's birthday! Created by Yukihiro Matsumoto in 1993 - {year - 1993} years of elegance!",
            (3, 15): f"📱 Happy Birthday to the World Wide Web! Created in 1989 - {year - 1989} years of connectivity!",
            (4, 1): f"🏢 April Fools' Day - Perfect time to deploy that 'harmless' feature! 😉",
            (5, 23): f"☕ Java's birthday! Released in 1995 - {year - 1995} years of 'write once, run anywhere'!",
            (6, 23): f"🎮 Happy Birthday to Pac-Man! Released in 1980 - {year - 1980} years of gaming history!",
            (9, 17): f"🐍 Python's birthday! First released in 1991 - {year - 1991} years of readable code!",
            (10, 5): f"📱 Steve Jobs' birthday! The man who revolutionized computing - remembered forever!",
            (12, 9): f"🎉 Happy Birthday to Ada Lovelace! Born 1815 - the world's first programmer!"
        }
        
        return milestones.get((month, day))

    def check_tech_anniversaries(self, date):
        """Check for significant tech company and product anniversaries"""
        year, month, day = date.year, date.month, date.day
        
        anniversaries = {
            (1, 9): f"📱 iPhone announcement anniversary! Steve Jobs unveiled it in 2007 - {year - 2007} years ago!",
            (2, 4): f"👥 Facebook founded! Mark Zuckerberg started it in 2004 - {year - 2004} years of social networking!",
            (4, 4): f"🌐 Microsoft founded! Bill Gates & Paul Allen started it in 1975 - {year - 1975} years of software!",
            (4, 28): f"🖥️ Windows 95 development milestone! The OS that changed everything!",
            (6, 15): f"💿 DVD format announced! In 1995 - {year - 1995} years of digital media evolution!",
            (7, 15): f"🛒 Amazon founded! Jeff Bezos started it in 1994 - {year - 1994} years of e-commerce!",
            (9, 4): f"🔍 Google founded! Larry Page & Sergey Brin started it in 1998 - {year - 1998} years of search!",
            (10, 5): f"🖥️ MacOS birthday! First Mac OS released in 1984 - {year - 1984} years of innovation!"
        }
        
        return anniversaries.get((month, day))

    def get_moon_phase(self, date):
        """Get approximate moon phase for extra creativity"""
        # Simplified moon phase calculation
        days_since_new_moon = (date - datetime(2000, 1, 6)).days % 29.53
        
        if days_since_new_moon < 7.38:
            return "🌑 New Moon - Perfect time for new coding projects!"
        elif days_since_new_moon < 14.77:
            return "🌓 First Quarter - Build momentum on your code!"
        elif days_since_new_moon < 22.15:
            return "🌕 Full Moon - Full stack energy tonight!"
        else:
            return "🌗 Last Quarter - Time to refactor and optimize!"

    def check_developer_special_days(self, date):
        """Check for developer-specific special days"""
        month, day = date.month, date.day
        weekday = date.weekday()
        
        special_days = {
            (1, 31): "👨‍💻 Happy System Administrator Appreciation Day!",
            (5, 25): "🌍 Geek Pride Day! Embrace your inner geek!",
            (9, 13): "👨‍💻 International Programmers' Day! (256th day of the year)",
            (10, 24): "🌐 World Development Information Day!",
            (11, 30): "💻 Computer Security Day - Keep your code secure!"
        }
        
        # Specific day calculations
        if month == 9 and day == 13:  # 256th day (or 12th in leap years)
            return "👨‍💻 International Programmers' Day! Day 256 = 2^8 🎉"
        
        # First Friday of October - World Smile Day
        if month == 10 and weekday == 4:
            first_friday = 1 + (4 - datetime(date.year, 10, 1).weekday()) % 7
            if day == first_friday:
                return "😊 World Smile Day - Your code makes people smile!"
        
        return special_days.get((month, day))

    def get_holiday_message(self, holiday, context):
        """Generate special holiday messages with Pierre-Henry's personality"""
        holiday_messages = {
            "New Year's Day 🎆": [
                f"🎆 Happy New Year {context['year']}! Time to commit to even more amazing code!",
                f"🥳 New Year, New Commits! Ready to build revolutionary software in {context['year']}?",
                "🍾 Cheers to another year of turning caffeine into code and dreams into applications!"
            ],
            "Valentine's Day 💝": [
                "💝 Happy Valentine's Day! Today we love our code as much as our ristretto!",
                "💖 Roses are red, violets are blue, clean code is beautiful, and so are you!",
                "💕 Love is in the air... and in every elegant function we write!"
            ],
            "St. Patrick's Day 🍀": [
                "🍀 Happy St. Patrick's Day! May your code be bug-free and your commits be green!",
                "☘️ Feeling lucky? Today's the perfect day to tackle that challenging algorithm!",
                "🌈 Looking for gold? Found it in our perfectly optimized codebase!"
            ],
            "April Fools' Day 😄": [
                "😄 April Fools' Day! Time to add some 'harmless' easter eggs to the code... 😉",
                "🃏 Today's prank: Making legacy code work flawlessly on the first try!",
                "😂 April Fools! Your code actually compiled without any warnings!"
            ],
            "Independence Day 🇺🇸": [
                "🇺🇸 Happy 4th of July! Celebrating freedom... from spaghetti code!",
                "🎆 Fireworks and code reviews - both light up the night!",
                "🗽 Independence Day: When your app finally runs independent of external dependencies!"
            ],
            "Halloween 🎃": [
                "🎃 Happy Halloween! Debugging scary code all night - trick or treat?",
                "👻 Boo! Hope your code isn't haunted by memory leaks!",
                "🕷️ Spider webs in the basement, spider diagrams in the documentation!"
            ],
            "Thanksgiving 🦃": [
                "🦃 Happy Thanksgiving! Grateful for: Fast CPUs, reliable frameworks, and unlimited ristretto!",
                "🙏 Thankful for the dev community, Stack Overflow, and Pierre-Henry's determination!",
                "🍂 Giving thanks for every successful deployment and every lesson learned from bugs!"
            ],
            "Christmas Eve 🎄": [
                "🎄 Christmas Eve magic! Santa's checking his list... of GitHub commits!",
                "🎅 Ho ho ho! Even Santa needs version control for his nice/naughty database!",
                "✨ Christmas Eve peace: No production deployments, just family and ristretto!"
            ],
            "Christmas Day 🎅": [
                "🎅 Merry Christmas! Best gift ever: Code that works perfectly on Christmas morning!",
                "🎁 Christmas miracle: All tests passing, all users happy, all systems green!",
                "🌟 Christmas joy: Sharing the gift of knowledge and elegant code!"
            ],
            "New Year's Eve 🎊": [
                "🎊 New Year's Eve! Counting down to midnight... and to our next major release!",
                "🥂 Toast to another year of innovation, learning, and Pierre-Henry's unstoppable energy!",
                f"⏰ Final commits of {context['year']} - let's end with style!"
            ]
        }
        
        messages = holiday_messages.get(holiday, [f"🎉 Happy {holiday}! Perfect day for some inspired coding!"])
        return random.choice(messages)
    def get_contextual_message(self):
        """Get a message based on dynamic real-time context"""
        contextual_config = self.config["chat_bot"]["contextual_messages"]
        context = self.get_dynamic_context()
        now = context['date']
        day_of_week = context['weekday']
        hour = context['hour']
        
        # Priority 1: Special holidays and occasions
        if context['is_holiday']:
            return self.get_holiday_message(context['is_holiday'], context)
        
        # Priority 2: Tech anniversaries and milestones
        if context['milestone']:
            return context['milestone']
        
        if context['tech_anniversary']:
            return context['tech_anniversary']
        
        # Priority 3: Developer special days
        if context['developer_day']:
            return context['developer_day']
        
        # Priority 4: Seasonal and time-based messages
        if context['season'] == "winter":
            winter_messages = [
                "❄️ Winter coding sessions with hot ristretto - pure productivity!",
                "🔥 Let's warm up this cold day with some blazing fast algorithms!",
                "⛄ Building snowmen? Nah, building software architectures instead!",
                "🧣 Cozy winter vibes: Fireplace + laptop + Pierre-Henry's determination = magic!",
                f"🌙 {context['moon_phase']}"
            ]
            if random.random() < 0.7:  # 70% chance for seasonal message
                return random.choice(winter_messages)
        
        elif context['season'] == "spring":
            spring_messages = [
                "🌸 Spring cleaning your codebase? Time to refactor those legacy functions!",
                "� New season, new features! What's growing in your repository?",
                "🐝 Busy as a bee coding - spring energy is unstoppable!",
                "🌈 After every debugging storm comes a rainbow of working code!",
                f"🌙 {context['moon_phase']}"
            ]
            if random.random() < 0.7:
                return random.choice(spring_messages)
        
        elif context['season'] == "summer":
            summer_messages = [
                "☀️ Summer vibes: Outdoor hiking + indoor coding = perfect balance!",
                "🏖️ Beach day? Maybe later - these algorithms won't optimize themselves!",
                "🌻 Bright summer day, bright coding ideas! Let the creativity flow!",
                "� Tropical coding session: refreshing ideas under the warm sun!",
                f"🌙 {context['moon_phase']}"
            ]
            if random.random() < 0.7:
                return random.choice(summer_messages)
        
        elif context['season'] == "autumn":
            autumn_messages = [
                "🍂 Autumn leaves falling, code commits rising! Season of productivity!",
                "🍁 Harvest season for developers - reaping the benefits of good architecture!",
                "🎃 Pumpkin spice and everything nice... including clean, readable code!",
                "🌰 Nuts about coding! Autumn inspiration hits different!",
                f"🌙 {context['moon_phase']}"
            ]
            if random.random() < 0.7:
                return random.choice(autumn_messages)
        
        # Priority 5: Time-based dynamic messages
        if 5 <= hour < 12:  # Morning
            morning_messages = [
                f"🌅 Good morning! Day {now.timetuple().tm_yday} of {now.year} - let's make it count!",
                "☕ Morning ristretto + fresh ideas = unstoppable combination!",
                "🐓 Early bird catches the bug... and fixes it before anyone notices!",
                f"🌤️ Beautiful {calendar.day_name[day_of_week]} morning for some quality coding!",
                "🥐 French breakfast vibes: croissant, ristretto, and elegant algorithms!"
            ]
            if random.random() < 0.6:
                return random.choice(morning_messages)
        
        elif 12 <= hour < 17:  # Afternoon
            afternoon_messages = [
                "🍽️ Lunch break coding thoughts: How can we make this more efficient?",
                "⚡ Afternoon energy spike! Perfect time for complex problem-solving!",
                "🧀 Midday fuel check: Roquefort ✓ Determination ✓ Clean code ✓",
                f"📊 Productive {calendar.day_name[day_of_week]} afternoon - commits are flowing!",
                "🎯 Post-lunch focus: When your brain runs at maximum optimization!"
            ]
            if random.random() < 0.6:
                return random.choice(afternoon_messages)
        
        elif 17 <= hour < 21:  # Evening
            evening_messages = [
                "� Golden hour for golden code! Evening productivity hits different!",
                "🥾 Evening hike planned? Perfect time to think through architecture!",
                "🍷 End of day reflection: What elegant solution did we build today?",
                f"🌟 {calendar.day_name[day_of_week]} evening vibes - code, reflect, improve!",
                "🔥 Night owl mode activating... time for deep focus sessions!"
            ]
            if random.random() < 0.6:
                return random.choice(evening_messages)
        
        elif hour >= 21 or hour < 5:  # Night/Late night
            night_messages = [
                "🌙 Late night coding session? Pierre-Henry's dedication never sleeps!",
                "⭐ When the world sleeps, developers dream in code!",
                "🦉 Night owl productivity: Quiet hours, loud keyboard clicks!",
                "💤 Remember: Even the best developers need sleep for optimal brain.compile()!",
                f"🌌 {context['moon_phase']} - Perfect coding atmosphere!"
            ]
            if random.random() < 0.6:
                return random.choice(night_messages)
        
        # Priority 6: Day-specific messages (enhanced)
        if day_of_week == 0 and contextual_config.get("monday_motivation", True):  # Monday
            monday_messages = [
                "💪 Motivational Monday! This week: Pierre-Henry builds something extraordinary!",
                f"🚀 Monday Mission {now.strftime('%B %d')}: Turn weekend ideas into production code!",
                "⚡ Monday Energy: 12+ years of experience + fresh week = unlimited potential!",
                "🎯 Week Goal: Learn something new, build something amazing, share knowledge!",
                "🌟 Monday Mantra: From prototype to production, we make it happen!",
                "☕ Monday ristretto ritual: Fuel up for a week of innovative solutions!"
            ]
            return random.choice(monday_messages)
        
        elif day_of_week == 1:  # Tuesday
            tuesday_messages = [
                "🔧 Tool Tuesday! What new framework are we exploring today?",
                "⚙️ Tuesday Technique: Clean Code + SOLID principles = maintainable magic!",
                "🧩 Problem-solving Tuesday: Every bug is just a puzzle waiting for Pierre-Henry!",
                f"📈 Tuesday Progress Report: Day {now.timetuple().tm_yday} of building the future!"
            ]
            if random.random() < 0.4:
                return random.choice(tuesday_messages)
        
        elif day_of_week == 2:  # Wednesday
            wednesday_messages = [
                "📚 Wisdom Wednesday! Sharing knowledge makes the whole dev community stronger!",
                "🔄 Mid-week momentum: Agile methodologies keeping us on track!",
                "🎨 Wednesday Wonder: Code is poetry that computers can understand!",
                f"⚖️ Work-Life Wednesday: Coding + Hiking + Cheese = Perfect balance!"
            ]
            if random.random() < 0.4:
                return random.choice(wednesday_messages)
        
        elif day_of_week == 3:  # Thursday
            thursday_messages = [
                "🎲 Throwback Thursday: Remember when Pierre-Henry built pH7CMS at 17? Still innovating!",
                "⚡ Thursday Thoughts: Fast-paced changes, faster adaptations!",
                "🏗️ Thursday Build: From concept to deployment in record time!",
                "🧀 Thursday Tradition: Roquefort + coding = proven productivity formula!"
            ]
            if random.random() < 0.4:
                return random.choice(thursday_messages)
        
        # Weekend vibes (enhanced)
        elif day_of_week >= 5 and contextual_config.get("weekend_mode", True):
            weekend_messages = [
                f"🏖️ {calendar.day_name[day_of_week]} coding sessions hit different - what are you building?",
                "☕ Perfect weekend for a side project and some good ristretto!",
                "🎮 Weekend hack: Try building something fun, not just functional!",
                "🌟 Weekends are for experimenting with that new framework you bookmarked!",
                "📚 Great time to dive deep into that tech book you've been meaning to read!",
                "🧀 Weekend fuel: Roquefort, ristretto, and some quality coding time!",
                "🥾 Perfect day for a hike followed by some AI/ML exploration!",
                "🍇 Weekend energy: Learning + coding + fruit + fresh air = happiness! 😊",
                f"🛠️ Saturday Side Project: What innovative solution are we prototyping today?",
                f"🌈 {calendar.day_name[day_of_week]} vibes: Where creativity meets technical excellence!"
            ]
            return random.choice(weekend_messages)
        
        # Friday celebration (enhanced)
        elif day_of_week == 4 and contextual_config.get("friday_celebration", True):
            friday_messages = [
                "� TGIF! Time to Git Integrate Friday's features and celebrate the wins!",
                "🍻 Friday Deploy: Hope your code is as solid as your weekend plans!",
                "🎊 Friday feeling: Your commits this week were absolutely fantastic!",
                "🌈 End the week strong - one last push before the weekend adventures!",
                "🎈 Friday vibes: Celebrate every bug you've conquered this week!",
                "🏆 Week Review: From Monday's goals to Friday's achievements - well done!",
                f"🚀 Friday {now.strftime('%B %d')}: Another week of Pierre-Henry excellence!"
            ]
            return random.choice(friday_messages)
        
        # Default to enhanced weighted random message with context
        base_message = self.get_random_message()
        
        # Add contextual flair to regular messages
        context_additions = [
            f" (Day {now.timetuple().tm_yday}/{365 + calendar.isleap(now.year)} of {now.year})",
            f" - {calendar.day_name[day_of_week]} energy!",
            f" Perfect for this {context['season']} day!",
            ""  # Sometimes no addition for variety
        ]
        
        return base_message + random.choice(context_additions)

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
