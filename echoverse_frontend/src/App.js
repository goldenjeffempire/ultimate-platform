import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import Dashboard from "./pages/Dashboard";
import StoreBuilder from "./pages/StoreBuilder";
import BlogEditor from "./pages/BlogEditor";
import SellerDashboard from "./pages/SellerDashboard";
import ProductListing from "./pages/ProductListing";
import AdminPanel from "./pages/AdminPanel";
import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";
import NotFound from "./pages/NotFound";
import "./styles/auth.scss";


const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/store-builder" element={<StoreBuilder />} />
        <Route path="/blog-editor" element={<BlogEditor />} />
        <Route path="/seller-dashboard" element={<SellerDashboard />} />
        <Route path="/shop" element={<ProductListing />} />
        <Route path="/admin" element={<AdminPanel />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );
};

export default App;
