from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def dashboard():

    severity_counts = {"Low": 25, "Medium": 40, "High": 35, "Critical": 24}
    status_counts = {"Open": 8, "In Progress": 5, "Escalated": 3, "Closed": 12}
    alert_trend = {
        "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "counts": [12, 18, 24, 16, 30, 27, 20]
    }

    metrics = {
        "total_alerts": sum(severity_counts.values()),
        "open_cases": status_counts["Open"],
        "critical_alerts": severity_counts["Critical"],
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

    # Threat intelligence metrics summarise known malicious indicators.
    threat_intel = {
        "malicious_ips": 243,
        "malicious_domains": 89,
        "known_hashes": 164,
        "ioc_matches": 27
    }

    return render_template(
        "index.html",
        metrics=metrics,
        recent_events=recent_events,
        threat_intel=threat_intel,
        severity_counts=severity_counts,
        status_counts=status_counts,
        alert_trend=alert_trend
    )


if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG") == "1"
    app.run(debug=debug_mode)
