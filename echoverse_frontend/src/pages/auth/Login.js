import React, { useState } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import "./styles/auth.scss";

const Login = () => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const onSubmit = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post("/api/auth/login/", data);
      toast.success("Login successful!");
      navigate("/dashboard"); // Redirect to the dashboard or home page
    } catch (error) {
      toast.error("Login failed. Please check your credentials.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <h2>Log In</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        {/* Username */}
        <input 
          type="text" 
          placeholder="Username" 
          {...register("username", { required: true })} 
        />
        {errors.username && <p className="error-text">Username is required</p>}

        {/* Password */}
        <input 
          type="password" 
          placeholder="Password" 
          {...register("password", { required: true, minLength: 6 })} 
        />
        {errors.password && (
          <p className="error-text">Password must be at least 6 characters</p>
        )}

        {/* Submit Button */}
        <button type="submit" disabled={loading}>
          {loading ? "Logging In..." : "Log In"}
        </button>
      </form>

      {/* Redirect to Register if user doesn't have an account */}
      <p>
        Don't have an account? <a href="/register">Sign Up</a>
      </p>
    </div>
  );
};

export default Login;
