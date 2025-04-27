import React from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate for navigation
import styles from '../styles/home.module.css';

const Home = () => {
  const navigate = useNavigate(); // Initialize the useNavigate hook

  const handleNavigate = () => {
    navigate('/browse'); // Navigate to the Browse tab
  };

  return (
    <main className={styles.hero}>
      <div className={styles.heroContent}>
        <h1 className={styles.title}>
          <span className={styles.titleBrand}>EasyA Polkadot</span>
          <span className={styles.titleDivider}>|</span>
          <span className={styles.titleApp}>CoffeeChat</span>
        </h1>
        <p className={styles.subtitle}>
          Find mentors, network, and grow your career over a virtual coffee ☕
        </p>
        <button className={styles.ctaButton} onClick={handleNavigate}>
          Start Browsing →
        </button>
      </div>
    </main>
  );
};

export default Home;