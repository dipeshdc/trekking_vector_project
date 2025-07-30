# 🏔️ Trekking Vector Project

A full-stack project that leverages vector search and LLMs to deliver intelligent trek recommendations and summaries. Built with FastAPI, React, Ollama, and Qdrant.

---

## 📦 Features

- 🔍 Semantic search of trek data
- 🧠 LLM-powered trek summary generation
- ⚡ FastAPI backend with Ollama integration
- 🌐 React frontend with clean UI
- 🗄️ Vector storage using Qdrant
- 🐳 Dockerized for easy deployment

---

## 🖥️ Run Locally

This method is best suited for high-performance devices with fast internet.

### Steps:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd trekking_vector_project
   ```

2. Start the project using Docker:
   ```bash
   docker compose up
   ```

---

## ☁️ Deploy on AWS EC2

Recommended for mid-tier setups or remote hosting.

### EC2 Configuration:

- **Instance type**: `t3.medium` or `t2.medium`
- **Storage**: 30 GB (fits under AWS Free Tier)
- **OS**: Ubuntu Server (20.04 or later)

### Deployment Steps:

1. Launch an EC2 instance with the above configuration.
2. Open port 3000 and 8000
2. SSH into the instance.
3. Clone the repository:
   ```bash
   git clone <repository-url>
   cd trekking_vector_project
   ```
4. Update the IP references:
   - Replace `localhost` with your **EC2 public IP** in:
     - `backend/apiForTaking.py`
     - `frontend/src/App.jsx`
5. Run the app:
   ```bash
   docker compose up
   ```

---

## ⚙️ Tech Stack

| Layer     | Technology               |
|-----------|--------------------------|
| Frontend  | React                    |
| Backend   | FastAPI                  |
| LLM       | Ollama (e.g., DeepSeek, LLaMA3) |
| Vector DB | Qdrant                   |
| Runtime   | Docker + Docker Compose  |
| Cloud     | AWS EC2 (optional)       |

---

## 📁 Project Structure

```
trekking_vector_project/
├── backend/
│   └── apiForTaking.py
├── frontend/
│   └── src/App.jsx
├── docker-compose.yml
└── README.md
```

---

## 🔧 Environment Notes

- Make sure ports like `11434` (Ollama) and `3000` (React) are open in your EC2 security group.
- You can optionally use a `.env` file to centralize configurations (e.g., backend URLs, model names).

---


## 📬 Contact

For bugs, suggestions, or contributions, feel free to open an [Issue](https://github.com/your-repo/issues) or [Pull Request](https://github.com/your-repo/pulls).
