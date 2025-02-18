import React, { useState } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { toast } from "react-toastify";
import "./styles/auth.scss";

const Register = () => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);

  const onSubmit = async (data) => {
    setLoading(true);
    try {
      const response = await axios.post("/api/auth/register/", data);
      toast.success("Registration successful! Please log in.");
      navigate("/login");
    } catch (error) {
      toast.error("Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <input type="text" placeholder="Full Name" {...register("name", { required: true })} />
        {errors.name && <p className="error-text">Name is required</p>}

        <input type="email" placeholder="Email" {...register("email", { required: true })} />
        {errors.email && <p className="error-text">Valid email is required</p>}

        <input type="password" placeholder="Password" {...register("password", { required: true, minLength: 6 })} />
        {errors.password && <p className="error-text">Password must be at least 6 characters</p>}

        <button type="submit" disabled={loading}>{loading ? "Signing Up..." : "Sign Up"}</button>
      </form>
      <p>Already have an account? <a href="/login">Log in</a></p>
    </div>
  );
};

export default Register;
