import React, { useState } from "react";
import styled from "styled-components";

const BuilderContainer = styled.div`
  display: flex;
  height: 100vh;
  background-color: #e0dde4;
`;

const Sidebar = styled.div`
  width: 250px;
  background-color: #42455f;
  color: white;
  padding: 20px;
`;

const Workspace = styled.div`
  flex: 1;
  padding: 20px;
  border-left: 2px solid #998a90;
  min-height: 500px;
`;

const DragAndDropBuilder = () => {
  const [elements, setElements] = useState([]);

  const handleDrop = (e) => {
    const newElement = { id: Date.now(), type: e.dataTransfer.getData("text") };
    setElements([...elements, newElement]);
  };

  return (
    <BuilderContainer>
      <Sidebar>
        <h3>Elements</h3>
        <div
          draggable
          onDragStart={(e) => e.dataTransfer.setData("text", "text")}
          style={{ cursor: "grab", padding: "10px", border: "1px solid #cec0b6", marginBottom: "10px" }}
        >
          Text
        </div>
        <div
          draggable
          onDragStart={(e) => e.dataTransfer.setData("text", "image")}
          style={{ cursor: "grab", padding: "10px", border: "1px solid #cec0b6", marginBottom: "10px" }}
        >
          Image
        </div>
      </Sidebar>

      <Workspace onDrop={handleDrop} onDragOver={(e) => e.preventDefault()}>
        {elements.map((el) => (
          <div key={el.id} style={{ padding: "10px", marginBottom: "10px", border: "1px solid #998a90" }}>
            {el.type === "text" && <p>Sample Text Element</p>}
            {el.type === "image" && <img src="placeholder.jpg" alt="Placeholder" width="100" />}
          </div>
        ))}
      </Workspace>
    </BuilderContainer>
  );
};

export default DragAndDropBuilder;
