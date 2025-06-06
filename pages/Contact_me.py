import streamlit as st

st.set_page_config(page_title="Resume", page_icon="📄")

st.title("📄 My Resume")

st.markdown(
    """
    Click the button below to view my resume in a new tab.
    """
)

resume_url = "https://github.com/Kaushikkvn/Portfolio/blob/master/KAUSHIK%20KOMMINENI_RESUME_KDOT.pdf"  # replace this with your actual link

st.markdown(f"""
    <a href="{resume_url}" target="_blank">
        <button style='padding: 10px 20px; font-size: 16px;'>📄 View Resume</button>
    </a>
""", unsafe_allow_html=True)
