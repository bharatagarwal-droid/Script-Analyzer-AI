# import os
# import json
# from typing import Any, Dict

# from dotenv import load_dotenv
# from google import genai
# from google.genai import types

# load_dotenv()

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")


# def get_story_schema() -> Dict[str, Any]:
#     return {
#         "type": "object",
#         "properties": {
#             "title": {"type": "string"},
#             "summary": {"type": "string"},
#             "emotional_analysis": {
#                 "type": "object",
#                 "properties": {
#                     "dominant_emotions": {
#                         "type": "array",
#                         "items": {"type": "string"}
#                     },
#                     "emotional_arc": {"type": "string"}
#                 },
#                 "required": ["dominant_emotions", "emotional_arc"]
#             },
#             "engagement": {
#                 "type": "object",
#                 "properties": {
#                     "score": {"type": "number"},
#                     "factors": {
#                         "type": "array",
#                         "items": {"type": "string"}
#                     }
#                 },
#                 "required": ["score", "factors"]
#             },
#             "improvements": {
#                 "type": "array",
#                 "items": {"type": "string"}
#             },
#             "cliffhanger": {
#                 "type": "object",
#                 "properties": {
#                     "moment": {"type": "string"},
#                     "why_it_works": {"type": "string"}
#                 },
#                 "required": ["moment", "why_it_works"]
#             }
#         },
#         "required": [
#             "title",
#             "summary",
#             "emotional_analysis",
#             "engagement",
#             "improvements",
#             "cliffhanger"
#         ]
#     }


# def build_prompt(script_text: str) -> str:
#     return f"""
# You are an expert story analyst.

# Analyze the script and return STRICT VALID JSON.

# IMPORTANT RULES:
# - Return ONLY JSON (no text outside JSON)
# - Do NOT use numbering like 0:, 1:
# - Do NOT generate invalid JSON
# - Give specific, non-generic insights

# TASKS:
# 1. Write a 3-4 line summary
# 2. Identify dominant emotions
# 3. Explain emotional arc (start → middle → end)
# 4. Give engagement score (0-10)
# 5. Explain engagement factors clearly
# 6. Suggest improvements (practical)
# 7. Identify cliffhanger moment

# SCORING GUIDE:
# - 0-3: weak
# - 4-6: average
# - 7-8.5: strong
# - 8.5-10: highly engaging

# HALLUCINATION GUIDE:
# - Please ensure the response remains consistent each time the prompt is executed.

# SCRIPT:
# {script_text}
# """.strip()


# def analyze_script(script_text: str) -> Dict[str, Any]:
#     script_text = (script_text or "").strip()

#     if not script_text:
#         raise ValueError("Script text is empty.")

#     if not GEMINI_API_KEY:
#         raise ValueError("GEMINI_API_KEY missing")

#     client = genai.Client(api_key=GEMINI_API_KEY)

#     response = client.models.generate_content(
#         model=GEMINI_MODEL,
#         contents=build_prompt(script_text),
#         config=types.GenerateContentConfig(
#             temperature=0.3,
#             response_mime_type="application/json",
#             response_schema=get_story_schema(),
#         ),
#     )

#     text = (response.text or "").strip()

#     if not text:
#         raise RuntimeError("Empty response from Gemini")

#     # 🔥 SAFE JSON PARSE (IMPORTANT)
#     try:
#         return json.loads(text)
#     except json.JSONDecodeError:
#         # fallback cleaning
#         cleaned = text.replace("\n", "").replace("\t", "")
#         try:
#             return json.loads(cleaned)
#         except:
#             raise RuntimeError(f"Invalid JSON output:\n{text}")







import os
import json
from typing import Any, Dict

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite-preview")


def get_story_schema() -> Dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "summary": {"type": "string"},
            "emotional_analysis": {
                "type": "object",
                "properties": {
                    "dominant_emotions": {
                        "type": "array",
                        "items": {"type": "string"}
                    },
                    "emotional_arc": {"type": "string"}
                },
                "required": ["dominant_emotions", "emotional_arc"]
            },
            "engagement": {
                "type": "object",
                "properties": {
                    "score": {"type": "number"},
                    "factors": {
                        "type": "array",
                        "items": {"type": "string"}
                    }
                },
                "required": ["score", "factors"]
            },
            "improvements": {
                "type": "array",
                "items": {"type": "string"}
            },
            "cliffhanger": {
                "type": "object",
                "properties": {
                    "moment": {"type": "string"},
                    "why_it_works": {"type": "string"}
                },
                "required": ["moment", "why_it_works"]
            }
        },
        "required": [
            "title",
            "summary",
            "emotional_analysis",
            "engagement",
            "improvements",
            "cliffhanger"
        ]
    }


def build_prompt(script_text: str) -> str:
    return f"""
You are a careful script analysis system.

Analyze the given short script and return STRICT VALID JSON only.

Hard rules:
- Return only JSON.
- Do not include markdown.
- Do not include numbering like 0:, 1:.
- Base every claim only on the exact script text.
- Do not assume backstory, visuals, off-screen events, or future events unless explicitly stated.
- Keep the wording concise and grounded.
- Avoid dramatic exaggeration.
- If evidence is limited, say so briefly but stay useful.

Output instructions:
- summary: exactly 3 sentences.
- emotional_analysis.dominant_emotions: give 3 to 5 emotions.
- emotional_analysis.emotional_arc: explain emotional progression from beginning to end in 1 to 2 sentences.
- engagement.score: a score from 0 to 10.
- engagement.factors: exactly 3 concise reasons based only on the script.
- improvements: exactly 3 practical storytelling suggestions.
- cliffhanger: identify the most suspenseful moment if present; otherwise use a grounded low-suspense explanation.

Engagement scoring rubric:
Consider these dimensions before deciding the final score:
- opening hook
- character conflict
- tension or revelation
- emotional payoff
- cliffhanger strength

Use the rubric consistently, and make the score conservative rather than inflated.

SCRIPT:
{script_text}
""".strip()


def normalize_output(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Stabilize a few fields so repeated runs look less different.
    """
    # Round score to one decimal place
    if "engagement" in data and "score" in data["engagement"]:
        try:
            data["engagement"]["score"] = round(float(data["engagement"]["score"]), 1)
        except Exception:
            pass

    # Keep only first 3 factors / improvements if model returns more
    if "engagement" in data and "factors" in data["engagement"]:
        data["engagement"]["factors"] = data["engagement"]["factors"][:3]

    if "improvements" in data:
        data["improvements"] = data["improvements"][:3]

    # Clean blank strings if any
    if "emotional_analysis" in data and "dominant_emotions" in data["emotional_analysis"]:
        data["emotional_analysis"]["dominant_emotions"] = [
            str(x).strip() for x in data["emotional_analysis"]["dominant_emotions"] if str(x).strip()
        ]

    return data


def analyze_script(script_text: str) -> Dict[str, Any]:
    script_text = (script_text or "").strip()

    if not script_text:
        raise ValueError("Script text is empty.")

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY missing")

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=build_prompt(script_text),
        config=types.GenerateContentConfig(
            # Gemini structured output supports JSON-schema-constrained responses.
            # Gemini 3 docs recommend default temperature 1.0 for these models.
            temperature=1.0,
            response_mime_type="application/json",
            response_schema=get_story_schema(),
        ),
    )

    text = (response.text or "").strip()

    if not text:
        raise RuntimeError("Empty response from Gemini")

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Invalid JSON output: {e}\n{text}") from e

    return normalize_output(data)



















