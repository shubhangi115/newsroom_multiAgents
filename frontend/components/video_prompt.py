import streamlit as st


def display_video_prompt(video_prompt):

    if video_prompt is None:
        return

    st.header("Video Prompt Report")

    st.subheader("Video Concept")
    st.write(video_prompt["video_concept"])

    st.subheader("Video Style")
    st.write(video_prompt["video_style"])

    st.subheader("Opening Scene")
    st.write(video_prompt["opening_scene"])

    st.subheader("Scene Breakdown")
    st.write(video_prompt["scene_breakdown"])

    st.subheader("Voiceover Direction")
    st.write(video_prompt["voiceover_direction"])

    st.subheader("Transitions")
    st.write(video_prompt["transitions"])

    st.subheader("Color Palette")
    st.write(video_prompt["color_palette"])

    st.subheader("Aspect Ratio")
    st.write(video_prompt["aspect_ratio"])

    st.subheader("Elements to Avoid")

    for i in video_prompt["elements_to_avoid"]:
        st.write(f"- {i}")