# 📄 AI Resume Analyzer

AI Resume Analyzer is an intelligent web application built using **Python**, **Streamlit**, and the **OpenAI API** that helps users analyze and improve their resumes instantly. The application allows users to upload their resume in PDF format and receive AI-powered feedback including ATS compatibility, missing skills, weak areas, and improvement suggestions.

The project combines modern UI design with artificial intelligence to create an interactive and user-friendly experience for job seekers who want to optimize their resumes for recruiters and Applicant Tracking Systems (ATS).

---

# 🚀 Features

* 📂 Upload Resume in PDF format
* 🤖 AI-powered Resume Analysis
* 📊 ATS Friendliness Evaluation
* 🛠 Skill Gap Detection
* 💡 Resume Improvement Suggestions
* 🎯 Weak Area Identification
* ✨ Animated and Modern User Interface
* ⚡ Real-time Analysis using OpenAI API
* 🎈 Interactive UI Effects and Animations

---

# 🖥️ Demo Preview

The application provides:

* Animated gradient background
* Modern glassmorphism UI
* Interactive buttons and animations
* Smooth loading experience
* AI-generated resume feedback

---

# 🛠️ Technologies Used

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Backend Logic             |
| Streamlit             | Web Application Framework |
| OpenAI API            | AI Resume Analysis        |
| PyPDF                 | PDF Text Extraction       |
| HTML/CSS              | UI Customization          |
| Custom CSS Animations | Frontend Enhancement      |

---

# 📂 Project Structure

```bash
AIResumeAnalyser/
│
├── main.py
├── requirements.txt
├── README.md
└── .streamlit/
    └── secrets.toml
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AIResumeAnalyser.git
```

## 2️⃣ Navigate to Project Directory

```bash
cd AIResumeAnalyser
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup OpenAI API Key

Create a `.streamlit` folder inside the project directory.

Inside `.streamlit`, create a file named:

```bash
secrets.toml
```

Add your OpenAI API key:

```toml
OPENAI_API_KEY = "your-api-key"
```

---

# ▶️ Run the Application

```bash
streamlit run main.py
```

The application will automatically open in your browser.

---

# 📄 How It Works

1. User uploads a resume in PDF format
2. PyPDF extracts text from the resume
3. Resume content is sent to OpenAI API
4. AI analyzes the resume
5. The app displays:

   * ATS Score
   * Weak Areas
   * Missing Skills
   * Improvement Suggestions

---

# 🎨 UI/UX Enhancements

The frontend includes:

* Animated gradient backgrounds
* Glassmorphism design
* Hover animations
* Smooth transitions
* Responsive layout
* Interactive feedback animations

---

# 📈 Future Improvements

* Resume Score Visualization
* Job Description Matching
* Downloadable PDF Reports
* Resume Rewriting Feature
* Multiple Resume Templates
* Dark/Light Theme Toggle
* Resume Keyword Optimization
* Authentication System

---

# ⚠️ Security Note

Do NOT expose your OpenAI API key publicly.

Use:

* `.streamlit/secrets.toml`
* Environment Variables
* `.gitignore`

to protect sensitive credentials.

---

# 🤝 Contributing

Contributions are welcome!

Feel free to:

* Fork the repository
* Create a feature branch
* Submit pull requests

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by [Your Name]

If you like this project, give it a ⭐ on GitHub!
