import os, sqlite3

from flask import Flask, redirect, render_template, request, url_for
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get(".env"),
)

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        student_name = request.form["name"]
        student_email = request.form["email"]
        reference_style = request.form["style"]
        reference_content = request.form["references"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.6,
            messages=[
                {"role": "system","content": "You will receive submissions of a reference list provided by Canadian university students. Your job is to provide feedback to the user about ways that they could improve their references based on the reference style they input. In your response, say which reference style the student is trying to use. The following common errors should be highlighted: - Incorrect punctuation - Incorrect use of italics, italics should only be used for titles - Missing links, all online journal articles should have DOIs, and all websites should have URLs"},
                {"role": "user", "content": f"{reference_style}\n{reference_content}"}
            ]
        )
        msg = response.choices[0].message.content
        conn = get_db_connection()
        conn.execute("INSERT INTO student (StudentName, StudentEmail) VALUES (?, ?)",
                     (student_name, student_email))
        conn.execute("INSERT INTO prompts (Style, Reference, Msg) VALUES (?, ?, ?)",
                     (reference_style, reference_content, msg))
        conn.commit()
        conn.close()
        return redirect(url_for("index", result=response.choices[0].message.content))

    result = request.args.get("result")
    return render_template("index.html", result=result)