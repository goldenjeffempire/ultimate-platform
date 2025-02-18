import React from "react";
import { CardElement, useStripe, useElements } from "@stripe/react-stripe-js";
import axios from "axios";

const CheckoutForm = () => {
  const stripe = useStripe();
  const elements = useElements();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { token } = await stripe.createToken(elements.getElement(CardElement));

    const response = await axios.post("/api/checkout/", { token: token.id });
    if (response.data.success) {
      alert("Payment successful!");
    } else {
      alert("Payment failed.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <CardElement />
      <button type="submit">Pay</button>
    </form>
  );
};

export default CheckoutForm;
