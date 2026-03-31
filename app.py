
import json
import streamlit as st
from analyzer import analyze_script

st.set_page_config(page_title="Script Analyzer AI", page_icon="🎬", layout="wide")

st.title("🎬 Script Analyzer AI")
st.caption("Story analysis with Gemini")

default_script = """Title: The Last Message

Scene:
Riya receives a message from her ex-boyfriend after five years.

Dialogue:
Riya: Why now?
Arjun: Because today I learned the truth.
Riya: What truth?
Arjun: That the accident wasn't your fault.
"""

script_input = st.text_area("Enter Script", value=default_script, height=300)

if st.button("Analyze Script"):
    if not script_input.strip():
        st.warning("Please enter a script.")
    else:
        try:
            with st.spinner("Analyzing..."):
                result = analyze_script(script_input)

            st.success("Analysis complete")

            st.subheader("Structured Output")
            st.json(result)

            st.subheader("Readable View")
            st.markdown(f"### {result.get('title', 'Untitled')}")

            st.markdown("#### Summary")
            st.write(result["summary"])

            st.markdown("#### Emotional Analysis")
            st.write(
                "**Dominant emotions:**",
                ", ".join(result["emotional_analysis"]["dominant_emotions"])
            )
            st.write(
                "**Emotional arc:**",
                result["emotional_analysis"]["emotional_arc"]
            )

            st.markdown("#### Engagement")
            st.write(f"**Score:** {result['engagement']['score']} / 10")
            for factor in result["engagement"]["factors"]:
                st.write(f"- {factor}")

            st.markdown("#### Improvements")
            for item in result["improvements"]:
                st.write(f"- {item}")

            st.markdown("#### Cliffhanger")
            st.write("**Moment:**", result["cliffhanger"]["moment"])
            st.write("**Why it works:**", result["cliffhanger"]["why_it_works"])

            st.download_button(
                "Download JSON",
                data=json.dumps(result, indent=2),
                file_name="analysis.json",
                mime="application/json",
            )

        except Exception as e:
            st.error(f"Error: {e}")
