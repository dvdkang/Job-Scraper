import React, { useState, useEffect } from "react";
import Select from "react-select";
import { useNavigate } from "react-router-dom";
import "./Testing.css";

// Custom styles for the Select component
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
  { value: "Dallas, TX", label: "Dallas, TX" },
  { value: "Los Angeles, CA", label: "Los Angeles, CA" },
  { value: "Irvine, CA", label: "Irvine, CA" },
  { value: "San Jose, CA", label: "San Jose, CA" },
  { value: "Mountain View, CA", label: "Mountain View, CA" },
  { value: "San Diego, CA", label: "San Diego, CA" },
  { value: "San Francisco, CA", label: "San Francisco, CA" },
  { value: "New York, NY", label: "New York, NY" },
  { value: "Seattle, WA", label: "Seattle, WA" },
  { value: "Bellevue, WA", label: "Bellevue, WA" },
  { value: "Boston, MA", label: "Boston, MA" },
  { value: "Chicago, IL", label: "Chicago, IL" },
  { value: "Phoenix, AZ", label: "Phoenix, AZ" },
  { value: "Atlanta, GA", label: "Atlanta, GA" },
  { value: "Seoul, South Korea", label: "Seoul, South Korea" },
  { value: "Tokyo, Japan", label: "Tokyo, Japan" },
];

export const Testing = () => {
  const [jobRole, setJobRole] = useState("");
  const [location, setLocation] = useState("United States");
  const [jobResults, setJobResults] = useState([]);
  const [progress, setProgress] = useState(0); // State for tracking progress
  const navigate = useNavigate();

  const handleSearch = () => {
    const eventSource = new EventSource(
      `http://127.0.0.1:5000/api/jobs?role=${encodeURIComponent(
        jobRole
      )}&location=${encodeURIComponent(location)}`
    );

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.progress !== undefined) {
        setProgress(data.progress);
      }

      if (data.done) {
        setJobResults(data.jobs);
        navigate("/results", {
          state: { jobRole, location, jobs: data.jobs },
        });
        eventSource.close();
      }
    };

    eventSource.onerror = (error) => {
      console.error("Error with SSE:", error);
      eventSource.close();
    };
  };

  return (
    <div className="container">
      <span className="title">Help me find a job!</span>
      <h3 className="sub-title">Job Scraping LinkedIn Job Posting</h3>
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

      {/* Progress bar */}
      <div className="progress-bar-container">
        <div className="progress-bar" style={{ width: `${progress}%` }}>
          <div className="progress-text">{Math.floor(progress)}%</div>
        </div>
      </div>
    </div>
  );
};

// import React, { useState, useEffect } from "react";
// import { useNavigate } from "react-router-dom";
// import Select from "react-select";

// export const Home = () => {
//   const [jobRole, setJobRole] = useState("");
//   const [location, setLocation] = useState("United States");
//   const [progress, setProgress] = useState(0);
//   const [jobResults, setJobResults] = useState([]);
//   const navigate = useNavigate();

//   const handleSearch = () => {
//     const eventSource = new EventSource(
//       `http://127.0.0.1:5000/api/progress?role=${jobRole}&location=${location}`
//     );

//     eventSource.onmessage = (e) => {
//       const data = JSON.parse(e.data);

//       if (data.progress !== undefined) {
//         setProgress(data.progress);
//       }

//       if (data.done) {
//         setJobResults(data.jobs);
//         navigate("/results", {
//           state: { jobRole, location, jobs: data.jobs },
//         });
//         eventSource.close();
//       }
//     };

//     eventSource.onerror = () => {
//       console.error("SSE connection error");
//       eventSource.close();
//     };
//   };

//   return (
//     <div>
//       <input
//         type="text"
//         placeholder="Enter job role"
//         value={jobRole}
//         onChange={(e) => setJobRole(e.target.value)}
//       />
//       <Select
//         options={[{ value: "United States", label: "United States" }]} // Add more as needed
//         onChange={(opt) => setLocation(opt.value)}
//       />
//       <button onClick={handleSearch}>Search</button>

//       {progress > 0 && (
//         <div>
//           <p>Scraping Progress: {progress}%</p>
//           <progress value={progress} max="100" />
//         </div>
//       )}
//     </div>
//   );
// };
