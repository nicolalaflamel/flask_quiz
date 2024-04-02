from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def hello():
    quiz = "世界の薬草の種類は全部でおよそ何種類か？"
    return render_template("index.html",quiz=quiz)


@app.route("/answer",methods=["post"])
def answer():
    answer = int(request.form.get("answer"))
    answerKey = ""
    if 50000 <= answer <= 80000:
        answerKey = "正解"
    else:
        answerKey = "不正解"
    return render_template("answer.html",answerKey=answerKey)

if __name__=="__main__":
    app.run(debug=True)