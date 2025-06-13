# Smart Document Chatbot - Beginner Python Project

This is a web-based chatbot application that allows users to upload a PDF or DOCX document and ask natural language questions about its content. It's designed to demonstrate how NLP, Flask, and basic text extraction techniques can work together in a beginner-friendly project.

## Features
- Upload and parse PDF and DOCX files
- Basic intent detection (define, who, when, etc.)
- Simple keyword/entity extraction
- Chat interface with real-time answers from the document
- Dark-themed UI for better eye comfort

## Technologies Used
Python 3.11: Core programming language
Flask: Web server + routing
PyPDF2: PDF text extraction
python-docx: DOCX text extraction
re (regex): Extract keywords/entities
HTML/CSS/JS: Frontend chat UI

## File Structure

document_chatbot_project/
│
├── app.py                  # Flask backend
├── detect_intent.py        # Rule-based intent detector
├── extract_entities.py     # Simple entity extractor
├── templates/
│   └── index.html          # UI with dark blue theme
├── uploads/                # Folder for uploaded documents
└── README.md               # This file

## How It Works
1. User uploads a '.docx' or '.pdf' file through the UI.
2. Flask backend extracts text from the file.
3. User sends a question via the chatbot.
4. Backend detects intent (e.g., "define") and extracts keywords.
5. The app searches the extracted text for sentences with those keywords.
6. Up to 3 matched sentences are returned as the chatbot response.

## Installation & Setup
1. Make sure Python 3.11 is installed
2. Install dependencies: pip install flask werkzeug python-docx PyPDF2
3. Run the app through cmd: python app.py
4. Open browser with the given link (eg: http://127.0.0.1:5000)

## Future Improvements
- Add semantic search (e.g. Sentence-BERT)
- Memory for follow-up questions
- Better intent/entity classifiers
- Chat history export

## Author
Created by Aarian Zenno Mario as a demonstration of beginner-friendly NLP + web development using Python.
