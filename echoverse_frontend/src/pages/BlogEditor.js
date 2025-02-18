import React, { useState, useEffect } from "react";
import ReactQuill from "react-quill";
import "react-quill/dist/quill.snow.css";
import axios from "axios";
import "./styles/blogeditor.scss";

const BlogEditor = () => {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [aiSuggestion, setAiSuggestion] = useState("");

  useEffect(() => {
    document.title = "Echoverse | AI-Powered Blog Editor";
  }, []);

  const handleSave = async () => {
    try {
      await axios.post("/api/blogs/", { title, content });
      alert("Blog saved successfully!");
    } catch (error) {
      console.error("Error saving blog:", error);
    }
  };

  const handleGenerateAIContent = async () => {
    try {
      const response = await axios.post("/api/ai/generate-content/", {
        title,
      });
      setAiSuggestion(response.data.suggestion);
    } catch (error) {
      console.error("Error generating AI content:", error);
    }
  };

  return (
    <div className="blog-editor">
      <h2>Write Your Blog</h2>
      <input
        type="text"
        placeholder="Enter title..."
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <ReactQuill value={content} onChange={setContent} />
      <button className="ai-btn" onClick={handleGenerateAIContent}>
        Generate AI Suggestion
      </button>
      {aiSuggestion && <p className="ai-suggestion">{aiSuggestion}</p>}
      <button className="save-btn" onClick={handleSave}>
        Save Blog
      </button>
    </div>
  );
};

export default BlogEditor;
