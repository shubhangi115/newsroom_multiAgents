import streamlit as st


def display_final(final):

    if final is None:
        return

    st.header("Final Newsroom Package")

    st.subheader("Final Headline")
    st.write(final["final_headline"])

    st.subheader("Final Article")
    st.write(final["final_article"])

    st.subheader("Final SEO Package")
    st.write(final["final_seo_package"])

    st.subheader("Final Image Prompt")
    st.code(final["final_image_prompt"])

    st.subheader("Final Video Prompt")
    st.code(final["final_video_prompt"])

    st.subheader("Final Social Media Package")
    st.write(final["final_social_media_package"])

    st.subheader("Publication Notes")
    st.write(final["publication_notes"])

    st.subheader("Publication Status")
    st.success(final["publication_status"])