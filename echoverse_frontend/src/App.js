import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState, useEffect } from "react";
import jwtDecode from "jwt-decode";

// Authentication Pages
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";

// Main Pages
import HomePage from "./pages/HomePage";
import Dashboard from "./pages/Dashboard";
import StoreBuilder from "./pages/StoreBuilder";
import BlogEditor from "./pages/BlogEditor";
import SellerDashboard from "./pages/SellerDashboard";
import ProductListing from "./pages/ProductListing";
import AdminPanel from "./pages/AdminPanel";
import NotFound from "./pages/NotFound";

const App = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token) {
      try {
        const decoded = jwtDecode(token);
        if (decoded.exp * 1000 < Date.now()) {
          // Token is expired, remove from localStorage and set user to null
          localStorage.removeItem("token");
          setUser(null);
        } else {
          // Token is valid, set the user from the decoded token
          setUser(decoded);
        }
      } catch (error) {
        console.error("Error decoding token:", error);
        localStorage.removeItem("token");
        setUser(null);
      }
    }
  }, []);

  return (
    <Router>
      <Routes>
        {/* Authentication Routes */}
        <Route path="/login" element={<Login setUser={setUser} />} />
        <Route path="/register" element={<Register />} />

        {/* Main Application Routes */}
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<Dashboard user={user} />} />
        <Route path="/dashboard" element={<PrivateRoute user={user}><Dashboard user={user} /></PrivateRoute>} />
        <Route path="/store-builder" element={<StoreBuilder />} />
        <Route path="/blog-editor" element={<BlogEditor />} />
        <Route path="/seller-dashboard" element={<SellerDashboard />} />
        <Route path="/shop" element={<ProductListing />} />
        <Route path="/admin" element={<AdminPanel />} />

        {/* Catch-all route for 404 */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
};

export default App;
