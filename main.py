from flask import Flask , render_template
import pandas as pd 

app=Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/v1/<station>/<date>")
def out(station, date):
    station = str(station).zfill(6)
    df = pd.read_csv("E:\weather api\data\TG_STAID"+station+".txt",skiprows=20,parse_dates=['    DATE'])
    ndate  =f"{date[:4]}-{date[4:6]}-{date[6:]}"
    
    outp=df.loc[df['    DATE'] == ndate]['   TG'].squeeze() /10
    return {"station" : station,
            "date":ndate,
            "temperature":outp}

@app.route("/dct/<word>")
def dit(word):
    df=pd.read_csv("E:\weather api\dict\dictionary.csv")
    
    outp=df.loc[df["word"] == word]['definition'].squeeze()
    return {"word":word,
            "definition":str(outp)}



if __name__=="__main__":
   
   app.run(debug=True)