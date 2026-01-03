
# ✈️ Agentic AI Travel Planner & Itinerary Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Elastic Stack](https://img.shields.io/badge/Elastic_Stack-005571?style=flat&logo=elasticsearch&logoColor=white)](https://www.elastic.co/)

**An Enterprise-Grade, Agentic GenAI Application for Personalized Travel Planning.**

Built with **LangChain**, **Groq Llama-3**, and **Streamlit**, this application leverages autonomous AI agents to research, plan, and generate detailed travel itineraries. It features a production-ready architecture with **Docker**, **Kubernetes (K8s)** orchestration, and full observability using the **ELK Stack** (Elasticsearch, Logstash, Kibana).

---

## 🌟 Key Features

-   **🤖 Agentic AI Workflows**: Autonomous agents that research destinations and curate personalized plans.
-   **⚡ Ultra-Fast Generation**: Powered by **Groq's Llama-3-70b** for sub-second inference.
-   **🎨 Premium UI/UX**: A stunning, responsive Streamlit dashboard with glassmorphism design.
-   **🏭 Production Architecture**: Containerized with Docker and orchestrated via Kubernetes.
-   **📊 Full Observability**: Integrated ELK Stack for real-time logging, monitoring, and analytics.
-   **☁️ Cloud Native**: Designed for deployment on GCP, AWS, or Streamlit Cloud.

---

## 🛠️ Tech Stack

| Domain | Technology |
| :--- | :--- |
| **GenAI Framework** | [LangChain](https://www.langchain.com/) |
| **LLM Provider** | [Groq](https://groq.com/) (Llama-3-70b-Versatile) |
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **Containerization** | [Docker](https://www.docker.com/) |
| **Orchestration** | [Kubernetes](https://kubernetes.io/) (Minikube/EKS/GKE) |
| **Monitoring** | [ELK Stack](https://www.elastic.co/elastic-stack) (Elasticsearch, Logstash, Kibana) |
| **Language** | Python 3.11+ |

---

## 📸 UI & Features

### 1. 🎯 Interactive Demo Tab
The heart of the application. Users can generate itineraries via:
*   **Quick Start:** One-click generation for popular cities (Paris, Tokyo, etc.).
*   **Custom Form:** Detailed inputs for City, Interests, Dates, and Travelers.
*   **Visual Showcase:** a 5-column grid of realistic travel imagery.

### 2. 📊 System Logs & Monitoring
A transparency layer displaying real-time system logs.
*   **ELK Integration Code:** Visualizes how logs are processed.
*   **Live Metrics:** Success rates, total requests, and latency.
*   **Architecture Diagrams:** View the underlying infrastructure.

*(See Architecture Section below for diagrams)*

---

## 🏗️ Architecture & Workflows

This system is designed with **Microservices** principles in mind.

### 1. 🔄 Data Flow
The user request travels from the Streamlit Frontend -> LangChain Agent -> Groq LLM -> Response. Logs are shipped asynchronously to the ELK Stack.

![ELK Stack Data Flow](Diagarm/Architeure%20Diagram/ELK_Flow.jpg)

### 2. 🧱 System Components
A breakdown of the internal components, including the interaction between the User Interface, AI Agents, and the Knowledge Base.

![ELK Components](Diagarm/Architeure%20Diagram/ELK_Components.png)

### 3. 🚀 Deployment Architecture
How the application is deployed in a Kubernetes cluster with separate pods for the App, Elasticsearch, Logstash, and Kibana.

![Deployment Architecture](Diagarm/Architeure%20Diagram/ELK_Deployment.jpg)

---

## 🚀 Installation & Local Run

### Prerequisites
*   Python 3.11+
*   Git
*   Docker (optional, for container run)

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary.git
cd Agentic-AI-Travel-Planner-Itinerary
```

### Step 2: Install Dependencies
```bash
cd CODE
pip install -r requirements.txt
```

### Step 3: Setup Environment Variables
Create a `.env` file in the `CODE` directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 4: Run the Application
```bash
streamlit run streamlit_dashboard.py
```
*Access the app at `http://localhost:8501`*

---

## 🌐 Deployment Logic

### ☁️ Streamlit Cloud
1.  Fork this repo.
2.  Login to Streamlit Cloud.
3.  Connect GitHub and select the repo.
4.  Set `Main file path` to `CODE/streamlit_dashboard.py`.
5.  Add `GROQ_API_KEY` in Streamlit "Secrets".
6.  **Deploy!** 🚀

### 🐳 Docker & Kubernetes
For enterprise deployment:
1.  **Build Image:** `docker build -t ai-travel-planner ./CODE`
2.  **Run Container:** `docker run -p 8501:8501 ai-travel-planner`
3.  **Kubernetes:** Apply the manifests in `k8s-deployment.yaml`.
    ```bash
    kubectl apply -f CODE/k8s-deployment.yaml
    ```

---

## 🤝 Contributing & Large Files

This repository uses **Git LFS** (Large File Storage) for high-resolution diagram and asset management.
To clone with full assets:
```bash
git lfs install
git clone https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary.git
git lfs pull
```

---

## 📞 Contact

**Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer 4+ Yrs Experience)**

*   💼 **LinkedIn:** [https://www.linkedin.com/in/ratneshkumar1998/](https://www.linkedin.com/in/ratneshkumar1998/)
*   🐙 **GitHub:** [https://github.com/Ratnesh-181998](https://github.com/Ratnesh-181998)
*   📧 **Email:** rattudacsit2021gate@gmail.com

### Project Links
*   🌐 **Live Demo:** [Streamlit App](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
*   📖 **Documentation:** [GitHub Wiki](https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary/wiki)
*   🐛 **Issue Tracker:** [GitHub Issues](https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary/issues)

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

Copyright © 2024 Ratnesh Kumar Singh. All Rights Reserved.
