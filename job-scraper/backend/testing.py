from flask import Flask, request, jsonify, Response
from jobScrape.JobFind import job_scrape_streaming  # Import your scraping function
from flask_cors import CORS
import time
import json
import asyncio

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])


@app.route("/api/jobs")
# def stream_jobs():
#     role = request.args.get("role", "software engineer")
#     location = request.args.get("location", "United States")

#     def generate():
#         for update in job_scrape_streaming(role, location):
#             yield f"data: {json.dumps(update)}\n\n"

#     return Response(generate(), mimetype="text/event-stream")

def stream_jobs():
    role = request.args.get("role", "software engineer")
    location = request.args.get("location", "United States")

    def generate():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        gen = job_scrape_streaming(role, location)

        try:
            while True:
                update = loop.run_until_complete(gen.__anext__())
                yield f"data: {json.dumps(update)}\n\n"
        except StopAsyncIteration:
            pass
        finally:
            loop.close()

    return Response(generate(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', threaded=True) # Check if threaded affects anything can get rid of it if you need to
