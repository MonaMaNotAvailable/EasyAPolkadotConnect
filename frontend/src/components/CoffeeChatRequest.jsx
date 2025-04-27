import React, { useState } from "react";
import styles from "./CoffeeChatRequest.module.css";

const CoffeeChatRequest = ({ timeSlot, onRequest }) => {
  const [bet, setBet] = useState(0);

  const handleSubmit = () => {
    onRequest(timeSlot.id, bet);
  };

  return (
    <div className={styles.card}>
      <h3 className={styles.slotTitle}>Time Slot: {timeSlot.time}</h3>
      <p className={styles.slotDetails}>Available for: {timeSlot.availableFor}</p>
      <div className={styles.betContainer}>
        <input
          type="number"
          value={bet}
          onChange={(e) => setBet(e.target.value)}
          className={styles.betInput}
          placeholder="Enter your bet"
        />
        <button onClick={handleSubmit} className={styles.submitButton}>
          Place Bet
        </button>
      </div>
    </div>
  );
};

export default CoffeeChatRequest;