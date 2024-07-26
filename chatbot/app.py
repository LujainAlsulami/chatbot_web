from flask import Flask, render_template, request
from chatbottask import ask_gemini  

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    question = request.form['user_question']  
    answer = ask_gemini(question)
  else:
    question = None
    answer = None
  return render_template('index.html', question=question, answer=answer)


if __name__ == '__main__':
  app.run(debug=True)
