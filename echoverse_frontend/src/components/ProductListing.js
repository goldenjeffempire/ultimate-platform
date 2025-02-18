import React, { useEffect, useState } from "react";
import styled from "styled-components";

const ProductGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
`;

const ProductCard = styled.div`
  padding: 15px;
  background: #cec0b6;
  border-radius: 10px;
`;

const ProductListing = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    setProducts([
      { id: 1, name: "Product A", price: "$30" },
      { id: 2, name: "Product B", price: "$50" },
    ]);
  }, []);

  return (
    <ProductGrid>
      {products.map((product) => (
        <ProductCard key={product.id}>
          <h3>{product.name}</h3>
          <p>{product.price}</p>
        </ProductCard>
      ))}
    </ProductGrid>
  );
};

export default ProductListing;
