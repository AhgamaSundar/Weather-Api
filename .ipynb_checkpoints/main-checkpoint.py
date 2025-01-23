from flask import Flask , render_template

app=Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def out(station,date):
    return {"station":station,
            "date":date,
            "temp":23}
@app.route("/api/v1/<word>/")
def wrd(word):
    return str({"word":word.upper()})


if __name__=="__main__":
    app.run(debug=True)