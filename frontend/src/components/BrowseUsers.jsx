import React from "react";
import styles from "./BrowseUsers.module.css";

const BrowseUsers = ({ users, renderExtra }) => {
  if (!users || users.length === 0) {
    return <p className={styles.noUsers}>No users available to display.</p>;
  }

  return (
    <div className={styles.container}>
      <div className={styles.userList}>
        {users.map((user) => (
          <div key={user.wallet_address} className={styles.userCard}>
            <img
              src={user.profileImage}
              className={styles.profileImage}
            />
            <h2 className={styles.userName}>{user.name}</h2>
            <p className={styles.userBio}>{user.bio}</p>
            <p className={styles.userInterests}>
              Interests: {user.interests.join(", ")}
            </p>
            {renderExtra && renderExtra(user)}
            <button className={styles.connectButton}>Connect</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default BrowseUsers;
