from flask import Flask, render_template, request, flash
import logging
from plagiarism import detect_plagiarism

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    text = request.form.get('text')
    if not text:
        flash('Please enter some text to check for plagiarism.')
        return render_template('index.html')
    
    try:
        result = detect_plagiarism(text)
        return render_template('result.html', result=result)
    except Exception as e:
        logging.error(f"Error during plagiarism detection: {e}")
        flash('An error occurred while processing your request.')
        return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('error.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
