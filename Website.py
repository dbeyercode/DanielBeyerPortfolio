import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.set_page_config(page_title="Daniel Beyer Data Analyst")

st.markdown(
    """
    <style>
    body {
        font-size: 28px;
    }
    h1, h2, h3, h4, h5, h6 {
        font-size: 2em;
    }
    .stMarkdown, .stTitle, .stHeader, .stSubheader {
        font-size: 1.5em;
    }
    .stText {
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def load_animation(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

animation1= load_animation("https://lottie.host/e244151c-fa62-4f6e-9eb7-633e077fd061/Yt7mranC2X.json")
animation2 = load_animation("https://lottie.host/03cf2d32-119a-440c-b342-ba9f6c6eeed7/Jc3yCPcagK.json")
animation3 = load_animation("https://lottie.host/4f4fa32e-95ab-4b7a-8fe3-92347e370904/O1KCrRDgb6.json")
animation4 = load_animation("https://lottie.host/19ab0bf1-7f1e-4fe2-b1ba-97bb7870f6b6/JdNkElNuwk.json")

resumeurl = "https://drive.google.com/file/d/1NmMYl0dy6eUI1KPJwPKl55uGkZvjM-7R/view?usp=sharing"
billionurl = "https://drive.google.com/file/d/18qiLloCXzVnNOewXz3EKin_-JpdxPJGx/view?usp=sharing"
safeurl = "https://drive.google.com/file/d/1CIiKpWjlM2t1L2-gsDFlLuLnbXr5nldM/view?usp=sharing"
websiteurl = "https://drive.google.com/file/d/1UFH13tFLyMHX_-us1zuseYNMOE3eoH5x/view?usp=sharing"

with st.container():
    st.subheader("Hello!")
    st.title("I'm Daniel Beyer")
    st.write("A data analyst passionate about Insurtech and opening new doors for technological developments in the insurance industry.")
    st_lottie(animation1, height=200)

with st.container():
    st.write("---")
    st.header("My Skills")
    st.write(
        """
        - SQL, Python, R, and Excel (see "My Projects" section).
        - 6 years of insurance education and experience.
            - Understanding of the current insurance market and industry trends.
            - Familiar with key ratios and metrics used to determine insurance company performance.
            - Advanced understanding of insurance company database structures.
        """
        )
    st.write("Download my resume below")
    st.markdown(f"[Download Resume]({resumeurl})", unsafe_allow_html=True)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Interests")
        st.write(
            """
            - Actuarial
            - Operations
            - Claims
            - Catastrophe Modeling
            """
        )
    with right_column:
        st_lottie(animation2, height=300)

with st.container():
    st.write("---")
    left_column2, right_column2 = st.columns(2)
    with left_column2:
        st.header("My Projects")
        st.markdown(f"[Download Project 1]({billionurl})", unsafe_allow_html=True)
        st.markdown(f"[Download Project 2]({safeurl})", unsafe_allow_html=True)
        st.markdown(f"[Download Project 3]({websiteurl})", unsafe_allow_html=True)
        st.write(
            """
            - Project 1: Billion Dollar Disasters - The Costs of a Changing Economy and Climate on Insurers
            - Project 2: SafeHaven Insurance - Catastrophe Report and User Application
            - Project 3: This website! Take a look at the code behind it
            
            """
        )
    with right_column2:
        st_lottie(animation3, height=300)

with st.container():
    st.write("---")
    left_column3, right_column3 = st.columns(2)
    with left_column3:
     st.subheader("Want to learn more? Let's talk!")
     st.write(
        """
        - LinkedIn: https://www.linkedin.com/in/daniel-beyer1/
        - Phone: 309-242-9909
        - Email: danielrbeyer1@gmail.com
        """
     )
    with right_column3:
        st_lottie(animation4, height=300)


