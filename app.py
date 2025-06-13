from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader
from docx import Document
from detect_intent import detect_intent
from extract_entities import extract_entities

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

parsed_text = ""

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    global parsed_text
    if 'document' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['document']
    if file.filename == '':
        return jsonify({"message": "No file selected"}), 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    try:
        if filename.lower().endswith(".pdf"):
            parsed_text = parse_pdf(file_path)
        elif filename.lower().endswith(".docx"):
            parsed_text = parse_docx(file_path)
        else:
            return jsonify({"message": "Unsupported file type"}), 400
        parsed_text = clean_text(parsed_text)
    except Exception as e:
        return jsonify({"message": f"Failed to parse file: {str(e)}"}), 500
    return jsonify({"message": f"File '{filename}' uploaded and parsed successfully.", "content": parsed_text[:1000] + '... (truncated)'});

@app.route("/chat", methods=["POST"])
def chat():
    global parsed_text
    user_input = request.json.get("message")
    if not user_input or not parsed_text.strip():
        return jsonify({"reply": "No message or no uploaded file."})
    intent = detect_intent(user_input)
    entities = extract_entities(user_input)
    sentences = parsed_text.split('.')
    matches = [s.strip() for s in sentences if any(ent.lower() in s.lower() for ent in entities)]
    response = "<br><br>".join(matches[:3]) if matches else "I'm not sure how to answer that."
    return jsonify({"reply": f"<strong>Intent:</strong> {intent}<br><strong>Entities:</strong> {', '.join(entities)}<br><br>{response}"})

def parse_pdf(filepath):
    reader = PdfReader(filepath)
    text = " ".join(page.extract_text() or "" for page in reader.pages)
    return text

def parse_docx(filepath):
    doc = Document(filepath)
    return " ".join(para.text for para in doc.paragraphs if para.text.strip())

def clean_text(text):
    return ' '.join(text.replace('\n', ' ').split())

if __name__ == "__main__":
    app.run(debug=True)