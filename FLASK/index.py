from flask import Flask, render_template, url_for, request
from scripts.portfolio import Portfolio

app =  Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/calculate", methods=["post"])
def calculate():
    print(request.form)
    asset_list = request.form.getlist('asset')
    investment = request.form['totalInvestment']
    portfolio = [i for i in asset_list if i]
    result = Portfolio.get_recommended_allocation(portfolio,investment)
    return render_template("simple.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)