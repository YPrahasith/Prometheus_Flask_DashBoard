from flask import Flask, request, render_template
import requests, json, csv

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def index():
    lst =[]
    f = open('csv_file', 'w')
    writer = csv.writer(f)
    if request.method == "POST":
        p_name = request.form.get("fname")
        q_name = request.form.get("lname")
        query = q_name
        api_link = 'http://localhost:9090/api/v1/query?query='+query
        data = requests.get(api_link).text
        a = json.loads(data)
        b = []
        b = a["data"]["result"]
        print(data)
        for x in b :
            lst.append(x["value"])
            writer.writerow(x["value"])
        f.close()
    return render_template("index.html",x=lst)
