import React from "react";
import CoffeeChatRequest from "../components/CoffeeChatRequest";
import BrowseUsers from "../components/BrowseUsers";
import styles from "../styles/shared.module.css";

const Browse = () => {
  const users = [
    {
      wallet_address: "0x123",
      profileImage:"/panda.png",
      name: "Alice",
      bio: "Enthusiast in AI and Blockchain.",
      interests: ["AI", "Blockchain"],
      timeSlot: { id: 101, time: "9:00 AM", availableFor: "Mentorship" },
    },
    {
      wallet_address: "0x456",
      profileImage:"/cat.png",
      name: "Bob",
      bio: "Frontend developer and UX designer.",
      interests: ["Frontend", "UX Design"],

      timeSlot: { id: 102, time: "11:00 AM", availableFor: "Networking" },
    },
  ];

  const handleRequest = (timeSlotId, bet) => {
    console.log(`Requesting time slot ${timeSlotId} with bet of ${bet}`);
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>Available Mentors</h1>
      <BrowseUsers
        users={users}
        renderExtra={(user) => (
          <CoffeeChatRequest
            timeSlot={user.timeSlot}
            onRequest={handleRequest}
          />
        )}
      />
    </div>
  );
};

export default Browse;