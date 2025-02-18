import React, { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import AvatarEditor from "react-avatar-editor";
import { toast } from "react-toastify";
import "./styles/profile.scss";

const Profile = ({ user }) => {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [profileData, setProfileData] = useState({});
  const [image, setImage] = useState(null);
  const [imageFile, setImageFile] = useState(null);

  useEffect(() => {
    // Fetch user profile data
    axios.get(`/api/users/${user.id}/profile/`)
      .then(response => setProfileData(response.data))
      .catch(error => toast.error("Failed to load profile"));

  }, [user.id]);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setImageFile(file);
  };

  const onSubmit = async (data) => {
    try {
      let formData = new FormData();
      formData.append("name", data.name);
      formData.append("email", data.email);
      if (imageFile) formData.append("profile_image", imageFile);

      const response = await axios.put(`/api/users/${user.id}/profile/`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      
      toast.success("Profile updated successfully!");
      setProfileData(response.data);
    } catch (error) {
      toast.error("Failed to update profile");
    }
  };

  return (
    <div className="profile-container">
      <h2>Update Your Profile</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="avatar-container">
          <AvatarEditor
            image={image || profileData.profile_image}
            width={150}
            height={150}
            border={50}
            scale={1.2}
          />
          <input type="file" onChange={handleImageChange} />
        </div>

        <input type="text" placeholder="Name" {...register("name", { required: true })} defaultValue={profileData.name} />
        {errors.name && <p className="error-text">Name is required</p>}

        <input type="email" placeholder="Email" {...register("email", { required: true })} defaultValue={profileData.email} />
        {errors.email && <p className="error-text">Valid email is required</p>}

        <button type="submit">Update Profile</button>
      </form>
    </div>
  );
};

export default Profile;
