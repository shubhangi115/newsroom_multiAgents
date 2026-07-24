import streamlit as st


def display_validation(validation):

    if validation is None:
        return

    st.header("Validation Report")

    st.subheader("Overall Assessment")
    st.write(validation["overall_assessment"])

    st.subheader("Research & Article Consistency")
    st.write(validation["research_and_article_consistency"])

    st.subheader("Fact Check Compliance")
    st.write(validation["fact_check_compliance"])

    st.subheader("SEO & Headline Consistency")
    st.write(validation["seo_and_headline_consistency"])

    st.subheader("Visual Prompt Consistency")
    st.write(validation["visual_prompt_consistency"])

    st.subheader("Social Media Consistency")
    st.write(validation["social_media_consistency"])

    st.subheader("Issues Found")

    for i in validation["issues_found"]:
        st.write(f"- {i}")

    st.subheader("Recommended Changes")

    for j in validation["recommended_changes"]:
        st.write(f"- {j}")

    st.subheader("Final Recommendation")
    st.write(validation["final_recommendation"])