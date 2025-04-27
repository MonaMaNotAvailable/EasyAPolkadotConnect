import React, { useState } from "react";
import ProfileCard from "../components/ProfileCard";
import styles from "../styles/shared.module.css";

const Profile = () => {
  const [user] = useState({
    profileImage: "./dog.png",
    name: "Jane Doe",
    bio: "Web Developer",
    wallet_address: "12345ABCDE",
    interests: ["JavaScript", "React", "Node.js"],
  });

  return (
    <div className={styles.container}>
      <ProfileCard user={user} />
    </div>
  );
};

export default Profile;
