import streamlit as st


def display_headline(headline):

    if headline is None:
        return

    st.header("Headline Report")

    st.subheader("Recommended Headline")
    st.write(headline["recommended_headline"])

    st.subheader("SEO Headline")
    st.write(headline["seo_headline"])

    st.subheader("Breaking News Headline")
    st.write(headline["breaking_news_headline"])

    st.subheader("Mobile-Friendly Headline")
    st.write(headline["mobile_friendly_headline"])

    st.subheader("Reasoning")
    st.write(headline["reasoning"])