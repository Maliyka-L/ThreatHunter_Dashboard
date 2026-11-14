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

    # Recent security activity provides analyst visibility into ongoing investigations.
    recent_events = [
        {
            "time": "20:14",
            "event": "Brute Force Alert Detected"
        },
        {
            "time": "20:22",
            "event": "Case Assigned"
        },
        {
            "time": "20:35",
            "event": "IOC Added"
        },
        {
            "time": "20:41",
            "event": "MITRE Technique Tagged"
        },
        {
            "time": "20:58",
            "event": "Case Escalated"
        }
    ]

    return render_template(
        "index.html",
        metrics=metrics,
        recent_events=recent_events
    )


if __name__ == "__main__":
    app.run(debug=True)