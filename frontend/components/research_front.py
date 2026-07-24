import streamlit as st


def display_research(research):

    if research is None:
        return

    st.header("Research Report")

    st.subheader("Topic Overview")
    st.write(research["topic_overview"])

    st.subheader("Key Facts")

    for i in research["key_facts"]:
        st.write(f"- {i}")

    st.subheader("Important Organizations")

    for j in research["important_organizations"]:
        st.write(f"- {j}")

    st.subheader("Relevant Dates & Statistics")

    for k in research["relevant_dates_and_statistics"]:
        st.write(f"- {k}")

    st.subheader("Claims Requiring Verification")

    for l in research["claims_requiring_verification"]:
        st.write(f"- {l}")

    st.subheader("Research Summary")
    st.write(research["research_summary"])

    st.subheader("Sources")

    for i in research["sources"]:
        st.markdown(f"[{i['title']}]({i['url']})")