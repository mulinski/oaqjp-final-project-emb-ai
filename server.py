''' Executing this function initiates the application of emotion detection 
    to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emo_analyzer():
    ''' This code receives the text from the HTML interface and runs emotion 
        detection over it using emotion_detector() function. The output 
        returned shows the scores for each emotion and the dominant emotion.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return ("For the given statement, the system response is 'anger': "
            f"{response['anger']}, 'disgust': {response['disgust']}, 'fear': "
            f"{response['fear']}, 'joy': {response['joy']} and 'sadness': "
            f"{response['sadness']}. The dominant emotion is <b>"
            f"{response['dominant_emotion']}</b>.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
