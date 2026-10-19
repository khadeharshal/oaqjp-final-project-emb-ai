# Final project


# Emotion Detection Web Application

## Project Overview
This project uses Natural Language Processing (NLP) and IBM Watson NLP to detect emotions expressed in text. It identifies five emotions: anger, disgust, fear, joy, and sadness, and determines the dominant emotion.

## Features
- Detects emotions from user-provided text.
- Returns scores for five emotions.
- Identifies the dominant emotion.
- Provides a Flask web application and API endpoint.
- Includes unit tests for emotion detection.

## Project Structure
- `emotion_detection.py` — Emotion detection implementation.
- `EmotionDetection/__init__.py` — Python package initialization.
- `server.py` — Flask web application.
- `test_emotion_detection.py` — Unit tests.
- `README.md` — Project documentation.

## Technologies Used
- Python
- Flask
- IBM Watson NLP
- HTML
- Unittest

## How to Run
1. Install the required dependencies.
2. Start the Flask application using:

   ```bash
   python3 server.py
   ```

3. Open the application in your browser at `http://localhost:5000`.

## Example
**Input:** `I am very happy today!`

The application analyzes the text and returns emotion scores along with the dominant emotion.

## Author
Harshal Khade

## Repository
[GitHub Repository](https://github.com/khadeharshal/oaqjp-final-project-emb-ai)
