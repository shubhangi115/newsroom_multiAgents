import streamlit as st


def display_image_prompt(image_prompt):

    if image_prompt is None:
        return

    st.header("Image Prompt")

    st.subheader("Image Concept")
    st.write(image_prompt["image_concept"])

    st.subheader("Image Type")
    st.write(image_prompt["image_type"])

    st.subheader("Generation Prompt")
    st.code(image_prompt["generation_prompt"])

    st.subheader("Color Palette")
    st.write(image_prompt["color_palette"])

    st.subheader("Aspect Ratio")
    st.write(image_prompt["aspect_ratio"])

    st.subheader("Elements to Avoid")

    for i in image_prompt["elements_to_avoid"]:
        st.write(f"- {i}")