"""Flask application for emotion detection."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector", methods=['POST'])
def emotion_analyzer():
    """Analyzes emotion from text in a POST request."""
    data = request.get_json()
    text_to_analyze = data['text']
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    result_string = (
    f"For the given statement, the system response is "
    f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
    f"'joy': {joy} and 'sadness': {sadness}. "
    f"The dominant emotion is {dominant_emotion}."
)
    return result_string

@app.route("/")
def render_index_page():
    """Renders the index.html page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5002)
