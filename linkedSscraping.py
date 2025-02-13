import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    URL = "https://www.linkedin.com/jobs/search/?keywords=Software%20Developer%20Intern"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)

    job_listings = []
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        job_elements = soup.find_all("a", href=True)

        keywords = ["software", "intern"]

        for job in job_elements:
            title = job.text.strip().lower()
            link = job["href"]

            if all(keyword in title for keyword in keywords):
                job_listings.append({"title": job.text.strip(), "link": link})
    else:
        job_listings.append({"title": "Failed to retrieve jobs", "link": ""})

    html_template = """
    <html>
        <head>
            <title>Job Listings - Software Developer Intern</title>
        </head>
        <body>
            <h1>Job Listings - Software Developer Intern </h1>
            {% if job_listings %}
                <ul>
                {% for job in job_listings %}
                    <li><a href="{{ job.link }}" target="_blank">{{ job.title }}</a></li>
                {% endfor %}
                </ul>
            {% else %}
                <p>No job listings found.</p>
            {% endif %}
        </body>
    </html>
    """

    return render_template_string(html_template, job_listings=job_listings)

if __name__ == "__main__":
    app.run(debug=True)
