import streamlit as st


def display_social_media(social_media):

    if social_media is None:
        return

    st.header("Social Media Report")

    st.subheader("X (Twitter) Post")
    st.write(social_media["x_post"])

    st.subheader("LinkedIn Post")
    st.write(social_media["linkedin_post"])

    st.subheader("Instagram Caption")
    st.write(social_media["instagram_caption"])

    st.subheader("Facebook Post")
    st.write(social_media["facebook_post"])

    st.subheader("Hashtags")

    for i in social_media["hashtags"]:
        st.write(f"- {i}")

    st.subheader("Call To Action")
    st.write(social_media["call_to_action"])