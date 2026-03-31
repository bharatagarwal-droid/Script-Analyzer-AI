# # # import json
# # # import streamlit as st

# # # from analyzer import analyze_script

# # # st.set_page_config(page_title="Script Analyzer AI", page_icon="🎬", layout="wide")

# # # st.title("🎬 Script Analyzer AI")
# # # st.caption("Analyze short-form scripted content using an LLM")

# # # default_script = """Title: The Last Message

# # # Scene:
# # # Riya receives a message from her ex-boyfriend after five years.

# # # Dialogue:
# # # Riya: Why now?
# # # Arjun: Because today I learned the truth.
# # # Riya: What truth?
# # # Arjun: That the accident wasn't your fault.
# # # """

# # # script_input = st.text_area(
# # #     "Paste your script here",
# # #     value=default_script,
# # #     height=320
# # # )

# # # col1, col2 = st.columns([1, 1])

# # # with col1:
# # #     analyze_btn = st.button("Analyze Script", use_container_width=True)

# # # with col2:
# # #     clear_btn = st.button("Clear", use_container_width=True)

# # # if clear_btn:
# # #     st.rerun()

# # # if analyze_btn:
# # #     try:
# # #         with st.spinner("Analyzing story..."):
# # #             result = analyze_script(script_input)

# # #         st.success("Analysis complete")

# # #         st.subheader("Structured Output")
# # #         st.json(result)

# # #         st.subheader("Readable View")

# # #         st.markdown(f"### {result.get('title', 'Untitled Script')}")

# # #         st.markdown("#### Summary")
# # #         st.write(result["summary"])

# # #         st.markdown("#### Emotional Analysis")
# # #         emotions = result["emotional_analysis"]["dominant_emotions"]
# # #         st.write("**Dominant emotions:**", ", ".join(emotions))
# # #         st.write("**Emotional arc:**", result["emotional_analysis"]["emotional_arc"])

# # #         st.markdown("#### Engagement")
# # #         st.write(f"**Score:** {result['engagement']['score']} / 10")
# # #         for factor in result["engagement"]["factors"]:
# # #             st.write(f"- {factor}")

# # #         st.markdown("#### Improvements")
# # #         for item in result["improvements"]:
# # #             st.write(f"- {item}")

# # #         st.markdown("#### Cliffhanger")
# # #         st.write("**Moment:**", result["cliffhanger"]["moment"])
# # #         st.write("**Why it works:**", result["cliffhanger"]["why_it_works"])

# # #         st.subheader("Download JSON")
# # #         st.download_button(
# # #             label="Download analysis.json",
# # #             data=json.dumps(result, indent=2),
# # #             file_name="analysis.json",
# # #             mime="application/json"
# # #         )

# # #     except Exception as e:
# # #         st.error(f"Error: {e}")


# # import json
# # import streamlit as st

# # from analyzer import analyze_script

# # st.set_page_config(page_title="Script Analyzer AI", page_icon="🎬", layout="wide")

# # st.title("🎬 Script Analyzer AI")
# # st.caption("Analyze short-form scripts using Gemini")

# # default_script = """Title: The Last Message

# # Scene:
# # Riya receives a message from her ex-boyfriend after five years.

# # Dialogue:
# # Riya: Why now?
# # Arjun: Because today I learned the truth.
# # Riya: What truth?
# # Arjun: That the accident wasn't your fault.
# # """

# # script_input = st.text_area(
# #     "Paste your script here",
# #     value=default_script,
# #     height=320
# # )

# # if st.button("Analyze Script"):
# #     try:
# #         with st.spinner("Analyzing story..."):
# #             result = analyze_script(script_input)

# #         st.success("Analysis complete")
# #         st.json(result)

# #         st.subheader("Readable View")
# #         st.markdown(f"### {result.get('title', 'Untitled Script')}")
# #         st.write(result["summary"])

# #         st.markdown("#### Emotional Analysis")
# #         st.write("**Dominant emotions:**", ", ".join(result["emotional_analysis"]["dominant_emotions"]))
# #         st.write("**Emotional arc:**", result["emotional_analysis"]["emotional_arc"])

# #         st.markdown("#### Engagement")
# #         st.write(f"**Score:** {result['engagement']['score']} / 10")
# #         for factor in result["engagement"]["factors"]:
# #             st.write(f"- {factor}")

# #         st.markdown("#### Improvements")
# #         for item in result["improvements"]:
# #             st.write(f"- {item}")

# #         st.markdown("#### Cliffhanger")
# #         st.write("**Moment:**", result["cliffhanger"]["moment"])
# #         st.write("**Why it works:**", result["cliffhanger"]["why_it_works"])

# #         st.download_button(
# #             label="Download analysis.json",
# #             data=json.dumps(result, indent=2),
# #             file_name="analysis.json",
# #             mime="application/json"
# #         )

# #     except Exception as e:
# #         st.error(f"Error: {e}")



# import json
# import streamlit as st
# from analyzer import analyze_script

# st.set_page_config(page_title="Script Analyzer AI", page_icon="🎬", layout="wide")

# st.title("🎬 Script Analyzer AI")
# st.caption("AI-powered storytelling analysis using Gemini")

# default_script = """Title: The Last Message

# Scene:
# Riya receives a message from her ex-boyfriend after five years.

# Dialogue:
# Riya: Why now?
# Arjun: Because today I learned the truth.
# Riya: What truth?
# Arjun: That the accident wasn't your fault.
# """

# script_input = st.text_area("Enter Script", value=default_script, height=300)

# if st.button("Analyze Script"):

#     if not script_input.strip():
#         st.warning("Please enter a script")
#     else:
#         try:
#             with st.spinner("Analyzing..."):
#                 result = analyze_script(script_input)

#             st.success("Analysis Complete ✅")

#             # 🔹 JSON View
#             st.subheader("📦 Structured Output")
#             st.json(result)

#             # 🔹 Readable View
#             st.subheader("📖 Readable Analysis")

#             st.markdown(f"### {result.get('title', 'Untitled')}")

#             st.markdown("#### Summary")
#             st.write(result["summary"])

#             st.markdown("#### Emotional Analysis")
#             st.write("**Dominant emotions:**", ", ".join(result["emotional_analysis"]["dominant_emotions"]))
#             st.write("**Emotional arc:**", result["emotional_analysis"]["emotional_arc"])

#             st.markdown("#### Engagement")
#             st.write(f"**Score:** {result['engagement']['score']} / 10")
#             for f in result["engagement"]["factors"]:
#                 st.write(f"- {f}")

#             st.markdown("#### Improvements")
#             for imp in result["improvements"]:
#                 st.write(f"- {imp}")

#             st.markdown("#### Cliffhanger")
#             st.write("**Moment:**", result["cliffhanger"]["moment"])
#             st.write("**Why it works:**", result["cliffhanger"]["why_it_works"])

#             # 🔹 Download
#             st.download_button(
#                 "Download JSON",
#                 data=json.dumps(result, indent=2),
#                 file_name="analysis.json",
#                 mime="application/json"
#             )

#         except Exception as e:
#             st.error(f"Error: {e}")



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