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

### 1. Clone the repository
git clone <your-repo-url>
cd script-analyzer

### 2. Create a virtual environment
python -m venv venv

### 3. Activate the environment

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### 4. Install dependencies
pip install -r requirements.txt

### 5. Add your Gemini API key

Create a `.env` file in the root folder:

GEMINI_API_KEY=your_api_key_here

(Optional)
GEMINI_MODEL=gemini-3.1-flash-lite-preview

### 6. Run the application
streamlit run app.py

### 7. Open in browser
The app will automatically open at:
http://localhost:8501
