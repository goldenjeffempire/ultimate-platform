import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    // Fetch user data if authenticated
    const fetchUser = async () => {
      try {
        const token = localStorage.getItem("token");

        // If no token, redirect to login
        if (!token) {
          navigate("/login");
          return;
        }

        const response = await axios.get("http://localhost:8000/api/auth/user/", {
          headers: { Authorization: `Bearer ${token}` },
        });

        setUser(response.data);
      } catch (error) {
        // In case of any error (e.g., token expired), redirect to login
        navigate("/login");
      }
    };

    fetchUser();
  }, [navigate]);

  return (
    <div className="dashboard">
      {user ? (
        <>
          <h1>Welcome, {user.name || user.email}!</h1>
          <p>Explore Echoverse and build your online presence.</p>
        </>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Dashboard;
