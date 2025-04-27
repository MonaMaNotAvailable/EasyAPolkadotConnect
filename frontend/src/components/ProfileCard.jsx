import React from "react";
import styles from "./ProfileCard.module.css";

const ProfileCard = ({ user }) => {
  return (
    <div className={styles.card}>
      <img
        src={user.profileImage}
        alt={`${user.name}'s profile`}
        className={styles.profileImage}
      />
      <h2 className={styles.name}>{user.name}</h2>
      <p className={styles.bio}>{user.bio}</p>
      <div className={styles.interests}>
        <h3 className={styles.interestsTitle}>Interests:</h3>
        <div className={styles.interestsContainer}>
          {user.interests && user.interests.map((interest, index) => (
            <span key={index} className={styles.interestTag}>{interest}</span>
          ))}
        </div>
      </div>
      <p className={styles.walletAddress}>Wallet Address: {user.wallet_address}</p>
    </div>
  );
};

export default ProfileCard;