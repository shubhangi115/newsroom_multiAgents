import streamlit as st


def display_seo(seo):

    if seo is None:
        return

    st.header("SEO Report")

    st.subheader("SEO Title")
    st.write(seo["seo_title"])

    st.subheader("Meta Description")
    st.write(seo["meta_description"])

    st.subheader("Primary Keywords")

    for i in seo["primary_keywords"]:
        st.write(f"- {i}")

    st.subheader("Secondary Keywords")

    for j in seo["secondary_keywords"]:
        st.write(f"- {j}")

    st.subheader("URL Slug")
    st.code(seo["url_slug"])

    st.subheader("Search Intent")
    st.write(seo["search_intent"])