import streamlit as st

st.title("PCC Automation Tool")

uploaded_files = st.file_uploader("Upload PDFs", accept_multiple_files=True)

if st.button("Process"):
    if uploaded_files:
        for file in uploaded_files:
            st.write(f"Processing {file.name}")
        st.success("Done")
    else:
        st.warning("Upload files first")
