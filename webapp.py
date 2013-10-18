from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template("index.html")

@app.route('/readinglist.html')
def show_readinglist(): 
    return render_template("readinglist.html")

@app.route('/addbook.html')
def show_addbookpage(): 
    return render_template("addbook.html")

if __name__ == "__main__":
    app.run(debug=True)