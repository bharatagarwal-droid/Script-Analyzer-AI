# Script Analyzer AI
A lightweight AI system that analyzes short-form scripts and generates structured storytelling insights using the Gemini API.
##  Overview
This project builds an AI-powered system that understands and evaluates short scripts.  
It extracts meaningful insights such as summary, emotional tone, engagement potential, and improvement suggestions.
The goal is not just to generate text, but to produce **structured, useful analysis** that helps evaluate storytelling quality.

##  Features

-  Accepts short script input (1–3 scenes or dialogues)
-  Generates a concise 3–4 line summary
-  Identifies dominant emotions
-  Explains emotional arc (beginning → middle → end)
-  Calculates engagement score (0–10)
-  Explains factors influencing engagement
-  Suggests practical improvements
-  Detects cliffhanger / suspense moment
-  Returns structured JSON output
-  Includes Streamlit UI for easy interaction

---

##  Approach

The system is designed as a **single-step LLM pipeline**:
