import "./Home.css";
import React, { useState } from "react";
import Select from "react-select";
import { useNavigate } from "react-router-dom";

const customStyles = {
  control: (provided) => ({
    ...provided,
    width: "420px",
    borderRadius: "8px",
    boxShadow: "none",
    textAlign: "left",
  }),
  option: (provided, state) => ({
    ...provided,
    color: "black",
    backgroundColor: state.isSelected ? "lightgrey" : "white",
  }),
};

const locations = [
  { value: "United States", label: "United States" },
  { value: "Worldwide", label: "Worldwide" },
  { value: "Austin, TX", label: "Austin, TX" },
  { value: "Los Angeles, CA", label: "Los Angeles, CA" },
  { value: "New York", label: "New York" },
];

export const Home = () => {
  const [jobRole, setJobRole] = useState("");
  const [location, setLocation] = useState("United States");
  const [jobResults, setJobResults] = useState([]);
  const navigate = useNavigate();

  const handleSearch = async () => {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/jobs?role=${jobRole}&location=${location}`
      );
      const jobs = await response.json();
      setJobResults(jobs);

      navigate("/results", {
        state: {
          jobRole,
          location,
          jobs,
        },
      });
    } catch (error) {
      console.error("Error fetching jobs:", error);
    }
  };

  return (
    <div className="container">
      <span className="title">Help me find a job!</span>
      <input
        className="input"
        type="text"
        placeholder="What kind of job are you looking for?"
        value={jobRole}
        onChange={(e) => setJobRole(e.target.value)}
      />
      <Select
        className="select"
        options={locations}
        styles={customStyles}
        placeholder="Select a location"
        onChange={(selected) => setLocation(selected.value)}
      />
      <button className="search-button" onClick={handleSearch}>
        Search
      </button>
    </div>
  );
};
