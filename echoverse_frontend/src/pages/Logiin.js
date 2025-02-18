import React, { useState } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import jwtDecode from "jwt-decode";
import "./styles/auth.scss";

const Login = ({ setUser }) => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const onSubmit = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post("/api/auth/login/", data);
      const { access } = response.data;
      localStorage.setItem("token", access);
      setUser(jwtDecode(access)); // Store user data
      toast.success("Login successful!");
      navigate("/dashboard");
    } catch (error) {
      toast.error("Invalid email or password");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input type="email" placeholder="Email" {...register("email", { required: true })} />
        {errors.email && <p className="error-text">Email is required</p>}

        <input type="password" placeholder="Password" {...register("password", { required: true })} />
        {errors.password && <p className="error-text">Password is required</p>}

        <button type="submit" disabled={loading}>{loading ? "Logging in..." : "Login"}</button>
      </form>
      <p>Don't have an account? <a href="/register">Sign up</a></p>
    </div>
  );
};

export default Login;
