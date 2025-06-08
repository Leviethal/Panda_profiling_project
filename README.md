# 📊 ML Report Maker – Automated Data Profiling App

Welcome to **ML Report Maker**, a lightweight web application that generates automated data profiling reports from CSV files. Built using `pandas-profiling` and `FastAPI`, this app allows users to upload datasets and instantly view comprehensive exploratory data analysis (EDA) summaries — all through a browser!

## 🌐 Live Demo

🚀 Check out the deployed app here:  
👉 **[https://ml-report-maker.onrender.com/](https://ml-report-maker.onrender.com/)**

---

## 🧰 Tech Stack

- **Backend Framework**: FastAPI
- **Data Profiling**: pandas-profiling
- **Web Server**: Uvicorn
- **Frontend**: HTML, CSS, JS
- **Deployment**: Render

---

## 🛠️ Features

- 📁 Upload CSV files directly from your browser
- 📊 Automatically generate EDA reports using `pandas-profiling`
- 🧼 Analyze null values, distributions, correlations, types, and more
- ⚡ Fast and user-friendly interface with minimal setup

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Panda_profiling_project.git
   cd Panda_profiling_project
2. **Create and activate a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   # Activate on Windows:
   venv\Scripts\activate
   # Or on macOS/Linux:
   source venv/bin/activate
3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the application using Uvicorn**
   ```bash
   uvicorn app:app --reload
5. **Access the app in your browser**

   Navigate to: http://127.0.0.1:8000

## 🌍 Deployed Web App
No need to run locally? Try the live hosted version:
👉 https://ml-report-maker.onrender.com/
Upload your CSV file and view a full profiling report in seconds!
