import React, { useEffect, useState } from "react";
import axios from "axios";
import "./styles/recommendations.scss";

const Recommendations = ({ userId }) => {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    // Example AI-powered recommendations API
    axios.get(`/api/recommendations/${userId}/`)
      .then(response => setRecommendations(response.data))
      .catch(error => console.log("Error fetching recommendations"));
  }, [userId]);

  return (
    <div className="recommendations-container">
      <h3>AI-Powered Recommendations</h3>
      <ul>
        {recommendations.length > 0 ? recommendations.map((rec, index) => (
          <li key={index}>
            <p>{rec.title}</p>
            <span>{rec.description}</span>
          </li>
        )) : <p>No recommendations available</p>}
      </ul>
    </div>
  );
};

export default Recommendations;
