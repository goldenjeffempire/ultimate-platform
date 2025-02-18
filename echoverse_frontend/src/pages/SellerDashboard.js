import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles/sellerdashboard.scss";

const SellerDashboard = () => {
  const [products, setProducts] = useState([]);
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    fetchProducts();
    fetchOrders();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await axios.get("/api/seller/products/");
      setProducts(response.data);
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  const fetchOrders = async () => {
    try {
      const response = await axios.get("/api/seller/orders/");
      setOrders(response.data);
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  return (
    <div className="seller-dashboard">
      <h2>Seller Dashboard</h2>

      <div className="dashboard-section">
        <h3>Your Products</h3>
        <ul>
          {products.map((product) => (
            <li key={product.id}>{product.name} - ${product.price}</li>
          ))}
        </ul>
      </div>

      <div className="dashboard-section">
        <h3>Recent Orders</h3>
        <ul>
          {orders.map((order) => (
            <li key={order.id}>
              {order.product_name} - {order.status}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default SellerDashboard;
