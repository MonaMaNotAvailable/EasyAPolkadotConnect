import React from 'react';
import styles from '../styles/home.module.css';

const Home = () => {
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
        <button className={styles.ctaButton}>
          Start Browsing →
        </button>
      </div>
    </main>
  );
};

export default Home;