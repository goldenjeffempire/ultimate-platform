import React, { useState } from "react";
import { useDrag, useDrop } from "react-dnd";
import "./styles/storebuilder.scss";

const ElementTypes = {
  TEXT: "text",
  IMAGE: "image",
  BUTTON: "button",
};

const DraggableElement = ({ type, children }) => {
  const [{ isDragging }, drag] = useDrag(() => ({
    type,
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(),
    }),
  }));

  return (
    <div ref={drag} className={`draggable ${isDragging ? "dragging" : ""}`}>
      {children}
    </div>
  );
};

const DropArea = ({ onDrop }) => {
  const [{ isOver }, drop] = useDrop(() => ({
    accept: [ElementTypes.TEXT, ElementTypes.IMAGE, ElementTypes.BUTTON],
    drop: (item) => onDrop(item.type),
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  }));

  return (
    <div ref={drop} className={`drop-area ${isOver ? "hovered" : ""}`}>
      Drop components here
    </div>
  );
};

const StoreBuilder = () => {
  const [elements, setElements] = useState([]);

  const handleDrop = (type) => {
    setElements([...elements, type]);
  };

  return (
    <div className="store-builder">
      <aside className="sidebar">
        <h3>Drag Components</h3>
        <DraggableElement type={ElementTypes.TEXT}>📝 Text Block</DraggableElement>
        <DraggableElement type={ElementTypes.IMAGE}>🖼️ Image</DraggableElement>
        <DraggableElement type={ElementTypes.BUTTON}>🔘 Button</DraggableElement>
      </aside>

      <main className="canvas">
        <DropArea onDrop={handleDrop} />
        {elements.map((el, index) => (
          <div key={index} className="element">{el}</div>
        ))}
      </main>
    </div>
  );
};

export default StoreBuilder;
