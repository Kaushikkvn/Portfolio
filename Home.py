import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kaushik Kommineni Portfolio", layout="wide")

# ---- NAVIGATION MENU ----
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Education", "Experience", "Projects", "Resume", "Internship Feedback"],
        icons=["house", "book", "briefcase", "code-slash", "file-earmark-pdf", "chat-left-quote"],
        menu_icon="cast",
        default_index=0
    )

# ---- HOME SECTION ----
if selected == "Home":
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/image.jpeg", width=350)

    with col2:
        st.title("Kaushik Kommineni")
        st.markdown("""
        Versatile Computer Science graduate with strong analytical, technical, and problem-solving skills.  
        Experienced in designing and deploying end-to-end solutions across software and data systems.

        - Developed **scalable full-stack applications** using Python frameworks (Flask, Django)  
        - Engineered **automated data pipelines** and real-time systems using Apache NiFi, Spark, and Kafka  
        - Built **interactive dashboards and reports** with Power BI and SQL to drive business insights  
        - Applied **machine learning and deep learning models** for forecasting, classification, and anomaly detection  
        - Deployed models and apps using **Streamlit, TensorFlow**, and REST APIs for real-world impact  

        Passionate about transforming raw data into reliable, production-ready systems that support data-driven decision-making.
        """)


# ---- EDUCATION SECTION ----
elif selected == "Education":
    st.subheader("🎓 Education")
    st.markdown("""
    🏫 **University of Kansas**  
    *Master of Science in Computer Science*  
    GPA: 3.7/4.0 — *Aug 2023 – May 2025 (Expected)*  
    - Minor in **Data Science** with focus on scalable systems and analytics  
    - Relevant coursework: Advanced Data Science, Machine Learning, Deep Reinforcement Learning  
    - Built end-to-end ML pipelines for NLP and computer vision projects using Python and TensorFlow  
    - Developed Streamlit dashboards for real-time data exploration and model demos  
    - Active in AI and Data Science communities, conducted hands-on workshops for peers  

    🏫 **Koneru Lakshmaiah University**, India  
    *Bachelor of Technology in Computer Science and Engineering*  
    GPA: 8.63/10 — *Jul 2018 – May 2022*  
    - Minor in **Cyber Security**, with coursework in SQL, Python, Digital Forensics, and Web Technologies  
    - Final year project: Sentiment analysis system using supervised ML in Python  
    - Built a Smart Assistant Android app using NLP and Text-to-Speech APIs  
    - Held leadership roles in tech fests, IEEE student chapter, and university radio initiatives  
    """)


# ---- EXPERIENCE SECTION ----
elif selected == "Experience":
    st.subheader("💼 Work Experience")

    st.markdown("""
    🏢 **Virginia Department of Transportation (VDOT)** — *Business Intern*  
    *Jun 2024 – Aug 2024*  
    - Engineered Python-based automation scripts to extract and process traffic data from Oracle DB, reducing manual reporting time by 40%  
    - Designed a dynamic **Tkinter GUI** with 10+ user input parameters and integrated real-time backend validation, reducing data entry errors by 30%  
    - Applied linear regression models to 5+ years of historical AADT data, increasing forecast accuracy by 25% for HPMS submissions  
    - Built data pipelines to clean, normalize, and validate inputs across multiple schemas and tables from 3+ Oracle databases  
    - Developed robust exception handling and fail-safe mechanisms to minimize processing failures by 90% during batch runs  
    - Streamlined cross-functional workflows, enabling faster decision-making for 4+ stakeholder teams and reducing review cycles by 50%  
    - Authored detailed documentation and led interactive walkthroughs for end users and senior stakeholders  

    🏫 **University of Kansas** — *Graduate Teaching Assistant (SQL & Databases)*  
    *Nov 2023 – May 2024*  
    - Mentored over 80 undergraduate students in SQL, relational schema design, and database architecture  
    - Conducted weekly lab sessions on **query optimization**, **indexing**, **joins**, and **normalization** using MySQL  
    - Designed and evaluated practical assignments and projects simulating real-world database use cases  
    - Provided 1:1 guidance on performance tuning, schema best practices, and complex query formulation  
    - Supported capstone projects by offering feedback on DB design, scalability, and data access patterns  

    🏢 **Jio Platforms Limited** — *Data Engineer*  
    *Jul 2022 – Jul 2023*  
    - Spearheaded development of ingestion pipelines using **Apache NiFi** and **Kafka**, enabling real-time data flow across telecom systems and boosting pipeline efficiency by 40%  
    - Migrated 10TB+ of data from Oracle DB to **HIVE** via **Apache Spark**, cutting ETL processing time by 50% for the flagship Dynamite Project  
    - Automated export of 2M+ records using **Sqoop**, improving data availability and reducing manual intervention for downstream analytics  
    - Integrated CI/CD pipelines into the deployment lifecycle, reducing production incidents by 20% and improving system uptime  
    - Optimized complex SQL queries and redesigned schemas to reduce dashboard rendering latency by 35% in Power BI reports  
    - Led and trained a 3-member analytics team on data pipeline design, documentation standards, and tooling (Hive, MySQL, NiFi)  
    """)


# ---- PROJECTS SECTION ----
elif selected == "Projects":
    st.subheader("💻 Projects")
    df = pd.read_csv("data.csv", sep=";")
    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

    with col3:
        for index, row in df[:6].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

    with col4:
        for index, row in df[6:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

# ---- RESUME SECTION ----
elif selected == "Resume":
    st.subheader("📄 My Resume")

    resume_option = st.selectbox(
        "Select a version to view or download:",
        ["Data Engineering Resume", "Data Analysis Resume", "Backend Engineering Resume"]
    )

    resume_links = {
        "Data Engineering Resume": "https://drive.google.com/file/d/13J8gKrjnuN_-Q8MEbO-4ShIkuNDmM7x5/view?usp=sharing",
        "Data Analysis Resume": "https://drive.google.com/file/d/1Tsn62aC_Jm_NMr4gc3YGZDywEJJWKpIs/view?usp=sharing",
        "Backend Engineering Resume": "https://drive.google.com/file/d/1aVRxlGmLX98C9xQeQj9ApaFVawT3tolu/view?usp=sharing"
    }

    st.markdown(f"[Click here to view/download the **{resume_option}**]({resume_links[resume_option]})", unsafe_allow_html=True)


# ---- INTERNSHIP FEEDBACK SECTION ----
elif selected == "Internship Feedback":
    st.subheader("📳 Internship Feedback")
    st.markdown("""
    > "Kaushik quickly picked up tools like Tkinter, Oracle, and linear regression models. He created a prototype for forecasting with minimal supervision."

    > "His GUI design was intuitive and responsive. Users found it easy to input parameters and receive real-time forecasts."

    > "Kaushik's proactive communication and commitment to deadlines were impressive. He would be a great asset to any data-driven organization."

    📄 [Click here to view Internship Feedback Document](https://drive.google.com/file/d/1dK96avPjpMd8_jyfRbE1-zKz9T7NHjlv/view?usp=sharing)
    """)