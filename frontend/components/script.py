import streamlit as st


def display_script(script):

    if script is None:
        return

    st.header("Script Report")

    st.subheader("Headline")
    st.write(script["headline"])

    st.subheader("Lead")
    st.write(script["lead"])

    st.subheader("Body")
    st.write(script["body"])

    st.subheader("Conclusion")
    st.write(script["conclusion"])