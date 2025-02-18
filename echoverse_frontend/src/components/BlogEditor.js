import React, { useState } from "react";
import styled from "styled-components";

const EditorContainer = styled.div`
  padding: 20px;
  max-width: 800px;
  margin: auto;
`;

const BlogEditor = () => {
  const [content, setContent] = useState("");

  const handleChange = (e) => {
    setContent(e.target.value);
  };

  const generateAIContent = () => {
    setContent("This is AI-generated content...");
  };

  return (
    <EditorContainer>
      <textarea
        value={content}
        onChange={handleChange}
        rows="10"
        style={{ width: "100%", padding: "10px" }}
        placeholder="Write your blog..."
      />
      <button onClick={generateAIContent}>Generate Content</button>
    </EditorContainer>
  );
};

export default BlogEditor;
