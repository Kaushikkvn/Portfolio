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
        Versatile Computer Science graduate with strong analytical,
        technical, and problem-solving skills. 
        Experienced in building end-to-end solutions across multiple domains:
        - As a **Software Developer**, built scalable full-stack apps using Python frameworks.
        - As a **Data Analyst**, developed data models and dashboards to extract actionable insights.
        - As a **Data Scientist**, implemented ML algorithms for classification and forecasting.
        - As a **Data Engineer**, automated ETL pipelines using Apache NiFi and Spark.
        - As an **ML Developer**, deployed deep learning models with TensorFlow and Streamlit.
        Passionate about bridging the gap between data and decision-making with scalable Python solutions.
        """)

# ---- EDUCATION SECTION ----
elif selected == "Education":
    st.subheader("🎓 Education")
    st.markdown("""
    🏫 **University of Kansas**  
    *M.S. in Computer Science*  
    GPA: 3.61/4.0 — *Expected May 2025*  
    - Specialized in **Machine Learning**, **Data Science**, and **Database Systems**  
    - Relevant coursework includes: Artificial Intelligence, Advanced DB Systems, and Cloud Computing  
    - Created ML pipelines for NLP and computer vision projects  
    - Designed Streamlit apps for real-time data visualization  
    - Active contributor to AI club, hosted student coding workshops  

    🏫 **Koneru Lakshmaiah University**  
    *B.Tech in Computer Science and Engineering*  
    GPA: 8.63/10.0 — *May 2022*  
    - Focused on core CS fundamentals: Algorithms, Web Technologies, and Operating Systems  
    - Built a Smart Assistant Android app using NLP and TTS APIs  
    - Final year project on sentiment analysis using ML in Python  
    - Participated in IEEE events, technical fests, and coding contests  
    """)

# ---- EXPERIENCE SECTION ----
elif selected == "Experience":
    st.subheader("💼 Work Experience")

    st.markdown("""
    🏢 **Virginia Department of Transportation (VDOT)** — *Business Intern*  
    *Jun 2024 – Aug 2024*  
    - Developed a **Traffic Forecasting Tool** with Tkinter UI and backend in Oracle SQL  
    - Applied regression models to automate traffic volume predictions (AADT)  
    - Presented deliverables to the executive committee with live demos  
    - Documented user manual, conducted stakeholder walkthroughs  

    🏫 **University of Kansas** — *Graduate Teaching Assistant (SQL)*  
    *Nov 2023 – May 2024*  
    - Guided over 80 students on relational schema design, MySQL, and query optimization  
    - Conducted lab sessions on indexing, joins, and normalization practices  
    - Graded assignments, clarified doubts, supported capstone DB projects  

    🏢 **Jio Platforms Limited** — *Data Engineer*  
    *Jul 2022 – Jul 2023*  
    - Created scalable ETL pipelines with NiFi and PySpark for telecom datasets  
    - Built Power BI dashboards to monitor KPIs and alert anomalies  
    - Integrated Kafka for streaming and reduced batch processing delays by 25%  
    - Automated audit reports and improved data quality pipelines  
    """)

# ---- PROJECTS SECTION ----
elif selected == "Projects":
    st.subheader("💻 Projects")
    df = pd.read_csv("data.csv", sep=";")
    col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

    with col3:
        for index, row in df[:10].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

    with col4:
        for index, row in df[10:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

# ---- RESUME SECTION ----
elif selected == "Resume":
    st.subheader("📄 My Resume")
    st.markdown("[Click here to view/download my resume](https://drive.google.com/file/d/1csB2Ckh8YgpXOAmAPqjzJ2ixoj7KhyHX/view?usp=sharing)", unsafe_allow_html=True)

# ---- INTERNSHIP FEEDBACK SECTION ----
elif selected == "Internship Feedback":
    st.subheader("📳 Internship Feedback")
    st.markdown("""
    > "Kaushik quickly picked up tools like Tkinter, Oracle, and linear regression models. He created a prototype for forecasting with minimal supervision."

    > "His GUI design was intuitive and responsive. Users found it easy to input parameters and receive real-time forecasts."

    > "Kaushik's proactive communication and commitment to deadlines were impressive. He would be a great asset to any data-driven organization."

    📄 [Click here to view Internship Feedback Document](https://drive.google.com/file/d/1dK96avPjpMd8_jyfRbE1-zKz9T7NHjlv/view?usp=sharing)
    """)
