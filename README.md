# ☕ EasyAPolkadotCoffeeChat

A Web3-powered platform for genuine, meaningful networking

## 🚀 Use Case

**EasyAPolkadotCoffeeChat** is a decentralized networking platform designed to facilitate authentic peer-to-peer coffee chats. Built on Polkadot, it uses a unique betting system for time slots, ensuring more respectful and serious interactions without the friction of traditional centralized platforms.

## 🎯 Mission

Humans meeting humans — for mentorship, learning, career growth, collaboration, or simply expanding horizons.  

## ✨ Features

| Feature                  | Description |
|:-------------------------|:------------|
| **Profile Registration** | Create a wallet-based profile including name, short bio, and interests. |
| **Browse Users**          | Discover others interested in coffee chats based on shared interests. |
| **Post Time Slot**        | Users can post available time slots for coffee chats and set a maximum bet for each slot.
| **Place a Bet**           | Users can place a bet on a time slot to increase their chances of winning the chat. The highest bet wins the time slot. (first come first serve). |
| **Bet Refund**            | Users who place lower bets than the highest bidder will receive a refund. |
| **Funds Allocation**      | The person who posted the time slot decides how the funds are allocated (e.g., refund to winner, use for coffee, etc.) |
| **Secure Interaction**    | All interactions are peer-to-peer; no unnecessary data stored. |

## 💸 Monetization Model

A **small platform transaction fee** is applied to each coffee chat interaction to sustain the service.  

## 🔮 Future Work

- **Event RSVP System**:  
  Allow users to RSVP for virtual or in-person gatherings by paying a refundable fee (only refunded if attending).
- **Subscription Programs**:  
  Avoid paying any fees by subscribing per week, per month, per quarter, per year.
- **Recruiter Outreach**:  
  Enable recruiters to post roles and invite candidates for coffee chats.
- **Reputation System**:  
  Build trust through endorsements and chat feedback.

# 🚀 Project Setup Guide

## 📋 Requirements

### 🦀 Install Rust on macOS
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sudo sh
# source the changes
source "$HOME/.cargo/env"
# Verify installation
rustc --version  
```

### 🔧 Setting Up the Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Expected output for server startup
  ```
  INFO:     Will watch for changes in these directories: ['/Users/xxx/Desktop/EasyAPolkadotConnect/backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [35292] using StatReload
INFO:     Started server process [35294]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:60198 - "GET / HTTP/1.1" 200 OK
  ```

## 🔍 Troubleshooting

If you encounter permission issues during installation:
- For Rust: Make sure to run the installer with sudo
- For Python packages: Fix pip cache permissions with `sudo chown -R username:staff ~/Library/Caches/pip`