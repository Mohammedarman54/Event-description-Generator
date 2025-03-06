EVENT_DESCRIPTION_PROMPT = """
You are an AI assistant that generates structured event descriptions. **Return ONLY valid JSON output** with NO extra text, explanations, or markdown formatting.

### **Event Details:**
- Event Name: {event_name}
- Date: {date}
- Location: {location}
- Audience: {audience}
- Key Attractions: {key_attractions}
- Event Type: {event_type}

### **Strictly return JSON in this format:**
{{
  "event_description": "A professional event description in 3-4 sentences.",
  "social_media_post": "A short, engaging social media post in 1-2 sentences with relevant hashtags."
}}

⚠️ **Do not include any explanations, <think> sections, or additional text. Return ONLY JSON output in plain text.**  
"""
