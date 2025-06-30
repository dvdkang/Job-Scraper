import React from "react";
import { useLocation } from "react-router-dom"; // To access passed state
import "./Results.css";

export const Results = () => {
  const location = useLocation();
  const { jobRole, location: locationState, jobs } = location.state || []; // Getting jobs from location state

  return (
    <div className="results-container">
      <h2 className="header">
        Results for {jobRole} in {locationState}
      </h2>
      {jobs && jobs.length > 0 ? (
        <div className="results">
          {jobs.map((job, index) => (
            <div key={index} className="job-card">
              <h3 className="job-title">{job.title}</h3>
              <p className="company">
                {job.company} - {job.location}
              </p>
              <p>{job.requirements}</p>
              <a href={job.link} target="_blank" rel="noopener noreferrer">
                View Job
              </a>
            </div>
          ))}
        </div>
      ) : (
        <p>No jobs found for your search.</p>
      )}
    </div>
  );
};
