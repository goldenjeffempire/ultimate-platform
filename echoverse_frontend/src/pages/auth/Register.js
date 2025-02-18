import React, { useState } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate } from "react-router-dom";
import "./styles/auth.scss";

const Register = () => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

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
        {/* Full Name */}
        <input 
          type="text" 
          placeholder="Full Name" 
          {...register("fullName", { required: true })} 
        />
        {errors.fullName && <p className="error-text">Full Name is required</p>}

        {/* Username */}
        <input 
          type="text" 
          placeholder="Username" 
          {...register("username", { required: true })} 
        />
        {errors.username && <p className="error-text">Username is required</p>}

        {/* Email */}
        <input 
          type="email" 
          placeholder="Email" 
          {...register("email", { required: true })} 
        />
        {errors.email && <p className="error-text">Valid email is required</p>}

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
          {loading ? "Signing Up..." : "Sign Up"}
        </button>
      </form>

      {/* Redirect to Login if user already has an account */}
      <p>
        Already have an account? <a href="/login">Log in</a>
      </p>
    </div>
  );
};

export default Register;
