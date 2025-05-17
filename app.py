from flask import Flask, request, redirect, render_template, send_from_directory
import os
import pandas as pd
from ydata_profiling import ProfileReport
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
REPORT_FOLDER = 'reports'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'datafile' not in request.files:
        return "No file part", 400
    file = request.files['datafile']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    # Read file
    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
    except Exception as e:
        return f"Failed to read the file: {e}", 400

    # Generate profile report
    report = ProfileReport(df, title="Data Profiling Report", explorative=True)
    report_path = os.path.join(REPORT_FOLDER, filename + "_report.html")
    report.to_file(report_path)

    return redirect(f"/reports/{os.path.basename(report_path)}")

@app.route('/reports/<path:filename>')
def serve_report(filename):
    return send_from_directory(REPORT_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
