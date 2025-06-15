import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kaushik Kommineni Portfolio", layout="wide")

# ---- SIDEBAR NAVIGATION ----
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Education", "Experience", "Projects", "Resume", "Internship Feedback", "Skills"],
        icons=["house", "book", "briefcase", "code-slash", "file-earmark-pdf", "chat-left-quote", "tools"],
        menu_icon="cast",
        default_index=0
    )

    # ---- GLOBAL CONTACT SECTION ----
    st.markdown("---")
    st.markdown("📬 **Get in Touch**")
    st.markdown("📧 kaushik.kommineni@gmail.com")
    st.markdown("📍 Kansas, USA")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/kaushik-kommineni)")
    st.markdown("[Portfolio](https://portfolio-kaushikkommineni.streamlit.app/)")

# ---- HOME SECTION ----
if selected == "Home":
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/image.jpeg", width=350)

    with col2:
        st.title("Kaushik Kommineni")
        st.markdown("###")
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
    st.markdown("---")
    st.markdown("""
    🏫 **University of Kansas, USA**  
    *Master of Science in Computer Science*  
    GPA: 3.7 / 4.0 — *Aug 2023 – May 2025 (Expected)*  
    - 📘 Minor: **Data Science**  
    - 💡 Relevant Coursework: Advanced Data Science, Machine Learning, Deep Reinforcement Learning, Big Data Analytics, AI Ethics  
    - 🧪 Projects:  
        • Built ML pipelines for NLP & computer vision tasks using TensorFlow, Scikit-learn  
        • Created real-time data visualization tools using Streamlit and Plotly  
    - 👨‍🏫 Activities:  
        • Conducted workshops on MySQL and Streamlit for undergrad students  
        • Active member of the AI and Data Science Club  
        • Participated in KU Hackathon 2024 (Top 10 finalist)

    🏫 **Koneru Lakshmaiah University, India**  
    *Bachelor of Technology in Computer Science and Engineering*  
    GPA: 8.63 / 10 — *Jul 2018 – May 2022*  
    - 🔐 Minor: **Cyber Security**  
    - 🛠️ Focus Areas: Data Structures, Algorithms, Web Technologies, Digital Forensics  
    - 🧪 Final Project:  
        • Built a sentiment analysis engine using supervised ML models and Python (NLP + Scikit-learn)  
    - 📱 Other Projects:  
        • Smart Assistant Android app with NLP and TTS APIs  
    - 🎙️ Extracurriculars:  
        • Head of PR – Ivarna Fest (10,000+ attendees)  
        • Board Member – KL University Radio  
        • IEEE Student Chapter – Volunteer & Event Organizer  
    """)

# ---- EXPERIENCE SECTION ----
elif selected == "Experience":
    st.subheader("💼 Work Experience")
    st.markdown("---")

    st.markdown("""
    🏢 **Virginia Department of Transportation (VDOT)** — *Business Intern*  
    *Jun 2024 – Aug 2024*  
    - Engineered Python-based automation scripts to extract and process traffic data from Oracle DB, reducing manual reporting time by **40%**  
    - Designed a dynamic **Tkinter GUI** with 10+ user input parameters and integrated real-time backend validation, reducing data entry errors by **30%**  
    - Applied **linear regression models** to 5+ years of historical AADT data, increasing forecast accuracy by **25%** for HPMS submissions  
    - Built data pipelines to clean, normalize, and validate inputs across multiple schemas from 3+ Oracle databases  
    - Developed robust **exception handling and fail-safe mechanisms**, minimizing processing failures by **90%** during batch runs  
    - Streamlined cross-functional workflows, improving review cycle efficiency by **50%** for 4+ stakeholder teams  
    - Authored detailed documentation and conducted walkthroughs for end users and senior leadership  

    🏫 **University of Kansas** — *Graduate Teaching Assistant (SQL & Databases)*  
    *Nov 2023 – May 2024*  
    - Mentored over 80 undergraduate students in SQL, relational schema design, and database architecture  
    - Conducted weekly labs on **query optimization**, **indexing**, **joins**, and **normalization** using MySQL  
    - Designed and graded practical assignments and semester projects simulating industry database problems  
    - Provided one-on-one guidance on performance tuning, schema design best practices, and complex SQL formulation  
    - Supported student capstone teams with architectural reviews and DB scalability feedback  

    🏢 **Jio Platforms Limited** — *Data Engineer*  
    *Jul 2022 – Jul 2023*  
    - Spearheaded ingestion pipelines using **Apache NiFi**, **Kafka**, and **PySpark**, boosting data throughput by **40%**  
    - Migrated 10TB+ of data from Oracle DB to **Hive** via **Apache Spark**, cutting ETL load time by **50%**  
    - Automated export of 2M+ records using **Sqoop**, enhancing data availability and reducing manual reporting time  
    - Integrated **CI/CD pipelines** into deployment cycles, improving system reliability and cutting release errors by **20%**  
    - Optimized complex SQL queries and restructured schemas, improving **Power BI** dashboard latency by **35%**  
    - Mentored a team of 3 junior analysts, and led knowledge transfer on tools like Hive, MySQL, and NiFi  
    """)

# ---- PROJECTS SECTION ----
elif selected == "Projects":
    st.subheader("💻 Projects")
    st.markdown("---")
    df = pd.read_csv("data.csv", sep=";")
    col3, _, col4 = st.columns([1.5, 0.5, 1.5])

    def render_project(row):
        st.header(row["title"])
        st.write(row["description"])
        if "tags" in row:
            st.markdown(f"**🧩 Tech Stack:** `{row['tags']}`")
        st.image("images/" + row["image"])
        st.write(f"[🔗 Source Code]({row['url']})")

    with col3:
        for _, row in df[:6].iterrows():
            render_project(row)

    with col4:
        for _, row in df[6:].iterrows():
            render_project(row)

# ---- RESUME SECTION ----
elif selected == "Resume":
    st.subheader("📄 My Resume")
    st.markdown("---")

    resume_option = st.radio(
        "Select a version:",
        ["📊 Data Engineering Resume", "📈 Data Analysis Resume", "🖥️ Backend Engineering Resume"],
        horizontal=True
    )

    resume_links = {
        "📊 Data Engineering Resume": "https://drive.google.com/file/d/13J8gKrjnuN_-Q8MEbO-4ShIkuNDmM7x5/view?usp=sharing",
        "📈 Data Analysis Resume": "https://drive.google.com/file/d/1Tsn62aC_Jm_NMr4gc3YGZDywEJJWKpIs/view?usp=sharing",
        "🖥️ Backend Engineering Resume": "https://drive.google.com/file/d/1aVRxlGmLX98C9xQeQj9ApaFVawT3tolu/view?usp=sharing"
    }

    st.success(f"[📂 Click here to view/download the **{resume_option}**]({resume_links[resume_option]})", icon="📄")

# ---- INTERNSHIP FEEDBACK SECTION ----
elif selected == "Internship Feedback":
    st.subheader("📳 Internship Feedback")
    st.markdown("---")

    with st.expander("🔍 View Testimonials"):
        st.markdown("""
        🗣️ *"Kaushik quickly picked up tools like Tkinter, Oracle, and regression models. Created a working prototype with minimal guidance."*  
        🎯 *"His UI/UX was intuitive. Users appreciated the responsiveness and accuracy of real-time forecasts."*  
        🌟 *"Excellent communicator and proactive contributor. A valuable asset to any data team."*
        """)

    st.markdown("📎 [Full Feedback Document](https://drive.google.com/file/d/1dK96avPjpMd8_jyfRbE1-zKz9T7NHjlv/view?usp=sharing)")

# ---- SKILLS SECTION ----
elif selected == "Skills":
    st.subheader("🛠️ Skills & Tools")
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🧠 Programming & Querying")
        st.markdown("`Python`  `SQL (Oracle & MySQL)`  `C++`  `Bash`  `HTML/CSS`")

        st.markdown("### 📊 Data Analysis & BI")
        st.markdown("`Power BI`  `Tableau`  `Excel (Advanced)`  `Pandas`  `NumPy`")

        st.markdown("### 🌐 Web Development")
        st.markdown("`Flask`  `Django`  `REST APIs`")

    with col2:
        st.markdown("### ⚙️ Data Engineering & Pipelines")
        st.markdown("`Apache NiFi`  `Kafka`  `Spark`  `Hive`  `Sqoop`")

        st.markdown("### 🧪 ML & Visualization")
        st.markdown("`Scikit-learn`  `TensorFlow`  `Streamlit`  `Matplotlib`  `Seaborn`")

        st.markdown("### 🧰 Tools & Workflow")
        st.markdown("`Git`  `CI/CD`  `MySQL Workbench`  `Jupyter`  `Postman`")
