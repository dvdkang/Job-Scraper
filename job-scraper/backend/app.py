from flask import Flask, request, jsonify
from jobScrape.JobFind import job_scrape  # import your scraping function
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"]) 

@app.route("/api/jobs", methods=["GET"])
def get_jobs():
    role = request.args.get("role", "software engineer")
    location = request.args.get("location", "United States")
    
    print(f"Received request with role={role} and location={location}")
    
    jobs = job_scrape(job_role=role, location=location)
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')