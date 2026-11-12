from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():

    metrics = {
        "total_alerts": 124,
        "open_cases": 18,
        "critical_alerts": 4,
        "threat_hits": 11
    }

    severity_data = {
        "Low": 25,
        "Medium": 40,
        "High": 35,
        "Critical": 24
    }

    return render_template(
        "index.html",
        metrics=metrics,
        severity_data=severity_data
    )


if __name__ == "__main__":
    app.run(debug=True)