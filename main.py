
import streamlit as st
from pypdf import PdfReader
from openai import OpenAI

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>

/* Background Animation */
.stApp {
    background: linear-gradient(-45deg, #0f172a, #1e293b, #0f766e, #1d4ed8);
    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
    color: white;
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

/* Main Title */
.main-title {
    font-size: 55px;
    font-weight: bold;
    text-align: center;
    color: white;
    animation: fadeIn 2s ease-in-out;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #d1d5db;
    margin-bottom: 40px;
    animation: fadeIn 3s ease-in-out;
}

/* Upload Box */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
}

/* Button Styling */
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    border: none;
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    font-size: 20px;
    font-weight: bold;
    transition: 0.3s;
    box-shadow: 0px 0px 20px rgba(59,130,246,0.5);
}

/* Button Hover */
.stButton>button:hover {
    transform: scale(1.03);
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    box-shadow: 0px 0px 30px rgba(236,72,153,0.7);
}

/* Result Card */
.result-box {
    background: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);
    animation: fadeIn 1.5s ease-in-out;
}

/* Fade Animation */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0px);
    }
}

/* Spinner Text */
.stSpinner > div {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ------------------- HEADER -------------------
st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Upload your resume and get instant ATS analysis powered by AI 🚀</div>',
    unsafe_allow_html=True
)

# ------------------- ORIGINAL CODE -------------------
client = OpenAI(api_key="YOUR_API_KEY")

uploaded_file = st.file_uploader("Please upload your CV", type=["pdf"])

if st.button("Analyze"):

    if uploaded_file:

        with st.spinner("Extracting text from PDF..."):

            resume_text = ""

            reader = PdfReader(uploaded_file)

            for page in reader.pages:
                resume_text = resume_text + page.extract_text()

        with st.spinner("Analyzing Resume..."):

            prompt = f"Analyze the following Resume and suggest: Weak Area, Missing Skills, Improvement suggestion and check how much it is ATS friendly. for Resume : {resume_text}"

            response = client.responses.create(
                model="gpt-4o-mini",
                input=prompt
            )

        ai_output = response.output_text

        st.markdown(
            f"""
            <div class="result-box">
                <h2>📊 Analysis Result</h2>
                <p>{ai_output}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    else:
        st.warning("Please upload your CV")

