# GitHub Webhook Event Tracker

This project is a demonstration of how to integrate GitHub Webhooks with a live backend server (using ngrok) to track and display real-time GitHub events such as **Push**, **Pull Request**, and **Merge** operations.

---

## 🚀 Features

- Displays recent GitHub events from your repository.
- Tracks:
  - Push events
  - Pull request creations
  - Pull request merges
- Uses GitHub Webhooks to send real-time data to your backend.
- Clean, readable frontend to view events live.

---

## 🔧 Tech Stack

- **Frontend**: HTML + CSS (simple template to show events)
- **Backend**: PYTHON FLASK
- **Tunnel**: [ngrok](https://ngrok.com/) to expose localhost server to GitHub
- **GitHub Webhooks**: To send events from your repository to your server

---

## 🧪 How It Works (Tested Using GitHub Desktop)

### 1. Push Event
- Create a new branch and commit changes.
- Push the changes to GitHub using GitHub Desktop.
- ✅ Webhook triggers `push` event and logs it on the web app.

### 2. Pull Request Event
- Create a pull request from the feature branch to `main`.
- ✅ Webhook triggers `pull_request` event and logs the PR creation.

### 3. Merge Event
- Merge the pull request using the GitHub UI.
- ✅ Webhook triggers `pull_request` with `action = closed` and logs the merge.

---

## 📡 Webhook Setup

1. Go to your GitHub repo > Settings > Webhooks.
2. Add a new webhook:
   - **Payload URL**: `https://<your-ngrok-subdomain>.ngrok-free.app`
   - **Content type**: `application/json`
   - **Events to trigger**: `Just the push and pull request events`
3. Save the webhook.

---


