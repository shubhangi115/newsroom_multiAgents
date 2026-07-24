import streamlit as st


def display_fact_check(fact_check):

    if fact_check is None:
        return

    st.header("Fact Check Report")

    st.subheader("Claims Examined")

    for i in fact_check["claims_examined"]:
        st.write(f"- {i}")

    st.subheader("Supported Claims")

    for j in fact_check["supported_claims"]:
        st.write(f"- {j}")

    st.subheader("Claims Requiring Verification")

    for k in fact_check["claims_requiring_verification"]:
        st.write(f"- {k}")

    st.subheader("Unsupported Claims")

    for l in fact_check["unsupported_claims"]:
        st.write(f"- {l}")

    st.subheader("Overall Verdict")
    st.write(fact_check["overall_verdict"])