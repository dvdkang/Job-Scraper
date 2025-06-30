import "./App.css";
import { Home, Testing } from "./Home/Testing";
import { Results } from "./Results/Results";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

export const App = () => {
  return (
    <Router>
      <Routes>
        {/* Route for the search bar - this will be the default route */}
        <Route path="/" element={<Testing />} />

        {/* Route for displaying search results */}
        <Route path="/results" element={<Results />} />
      </Routes>
    </Router>
  );
};

export default App;
