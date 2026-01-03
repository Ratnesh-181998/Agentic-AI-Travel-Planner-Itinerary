
![Banner](assets/travel_hill.png)

# ✈️ Agentic AI Travel Planner & Itinerary Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Elastic Stack](https://img.shields.io/badge/Elastic_Stack-005571?style=flat&logo=elasticsearch&logoColor=white)](https://www.elastic.co/)

**An Enterprise-Grade, Agentic GenAI Application for Personalized Travel Planning.**

> *Designed for scalability, observability, and autonomous reasoning using LangChain, Groq, and Kubernetes.*

---

## 📑 Table of Contents
1.  [🚀 Project Overview](#-project-overview)
2.  [✨ Key Features](#-key-features)
3.  [🛠️ Technology Stack](#-technology-stack)
4.  [🏗️ System Architecture](#-system-architecture)
5.  [📂 Project Structure](#-project-structure)
6.  [⚙️ Installation & Local Setup](#-installation--local-setup)
7.  [☁️ Deployment Guide (Cloud & K8s)](#-deployment-guide-cloud--k8s)
8.  [📊 LLMOps & Observability](#-llmops--observability)
9.  [📞 Contact & Author](#-contact--author)

---

## 1. 🚀 Project Overview

The **Agentic AI Travel Planner** is a state-of-the-art Generative AI application that acts as a personal intelligent travel agent. Unlike simple rule-based planners, this system uses **Autonomous AI Agents** empowered by **LangChain** and **Groq's Llama-3-70b** to reason, research, and generate hyper-personalized travel itineraries.

It is engineered as a **Production-Ready System**, featuring a microservices architecture containerized with Docker, orchestrated by Kubernetes, and fully monitored via the ELK Stack (Elasticsearch, Logstash, Kibana).

---

## 2. ✨ Key Features

*   **🤖 Autonomous AI Agents:** Intelligent workflows that understand user preferences (budget, interests, duration) to craft unique plans.
*   **⚡ Ultra-Low Latency:** Powered by **Groq LPU™ Inference Engine**, delivering itineraries in sub-second times.
*   **🎨 Premium Streamlit UI:** A responsive, glassmorphism-styled dashboard with visual showcases and real-time interaction.
*   **🌍 Multi-City Support:** Generates detailed day-by-day plans for any global destination.
*   **📊 Production Observability:** Integrated **ELK Stack** for real-time logging, error tracking, and AI response monitoring.
*   **☁️ Cloud Native:** Designed for deployment on Google Cloud Platform (GCP), AWS, or Streamlit Cloud.

---

## 3. 🛠️ Technology Stack

| Domain | Tech | Role |
| :--- | :--- | :--- |
| **GenAI & LLM** | **LangChain**, **Groq (Llama-3)** | Orchestration Framework & Inference Model |
| **Frontend** | **Streamlit** | Interactive Web UI & Dashboard |
| **Backend Logic** | **Python 3.11** | Core Application Logic |
| **Containerization** | **Docker** | Application & Service Containerization |
| **Orchestration** | **Kubernetes (Minikube)** | Container Management & Scaling |
| **Monitoring** | **ELK Stack** | Centralized Logging & Visualization |
| **Version Control** | **Git & GitHub** | SCM & CI/CD Readiness |

---

## 4. 🏗️ System Architecture

### 🔄 End-to-End Workflow
The system follows a tiered architecture separating the UI, AI Logic, and Infrastructure layers.

![Architecture Workflow](Diagarm/Architeure%20Diagram/AI+travel+planner+Workflow.png)

### 🧱 Component Breakdown
*   **User Layer:** Streamlit Interface for input collection.
*   **AI Layer:** LangChain Agents processing prompts and calling Groq API.
*   **Data Layer:** JSON-structured itinerary generation.
*   **Ops Layer:** Filebeat shipping logs to Logstash/Elasticsearch.

![Components Diagram](Diagarm/Architeure%20Diagram/ELK_Components.png)

---

## 5. 📂 Project Structure

```bash
📦 Agentic-AI-Travel-Planner
 ┣ 📂 assets/                   # UI Assets (Images, Icons)
 ┣ 📂 CODE/                     # Source Code
 ┃ ┣ 📂 src/                    # Core Logic Modules
 ┃ ┃ ┣ 📂 chains/               # LangChain Definitions
 ┃ ┃ ┗ 📂 core/                 # Planner Logic
 ┃ ┣ 📜 app.py                  # Streamlit Entry Point
 ┃ ┣ 📜 streamlit_dashboard.py  # Main Dashboard UI
 ┃ ┣ 📜 Dockerfile              # Container Definition
 ┃ ┣ 📜 requirements.txt        # Python Dependencies
 ┃ ┗ 📜 k8s-deployment.yaml     # Kubernetes Manifests
 ┣ 📂 Diagarm/                  # Architecture Diagrams
 ┣ 📜 README.md                 # Documentation
 ┗ 📜 .gitignore                # Git Configuration
```

---

## 6. ⚙️ Installation & Local Setup

### Prerequisites
*   Python 3.11+
*   Git
*   [Groq API Key](https://groq.com/)

### Step-by-Step Guide
1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary.git
    cd Agentic-AI-Travel-Planner-Itinerary
    ```

2.  **Create Virtual Environment**
    ```bash
    cd CODE
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\Activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key**
    Create a `.env` file in the `CODE` folder:
    ```env
    GROQ_API_KEY=gsk_your_api_key_here
    ```

5.  **Run the Application**
    ```bash
    streamlit run streamlit_dashboard.py
    ```

---

## 7. ☁️ Deployment Guide (Cloud & K8s)

### Option A: Streamlit Cloud (Fastest)
1.  Fork this repository.
2.  Login to [Streamlit Cloud](https://share.streamlit.io/).
3.  Connect GitHub and select repository.
4.  **Important:** Set Main file path to `CODE/streamlit_dashboard.py`.
5.  Add `GROQ_API_KEY` in Streamlit **Secrets**.
6.  Click **Deploy**.

### Option B: Docker Container
The application is fully containerized. View the **[Dockerfile](CODE/Dockerfile)** for details.
```bash
# Build Image
docker build -t travel-planner-ai ./CODE

# Run Container
docker run -p 8501:8501 -e GROQ_API_KEY=your_key travel-planner-ai
```

### Option C: Kubernetes (Enterprise)
Orchestrate the entire stack using our production-ready manifests.

**📂 Infrastructure Files:**
*   **[k8s-deployment.yaml](CODE/k8s-deployment.yaml)**: Main application deployment & service.
*   **[elasticsearch.yaml](CODE/elasticsearch.yaml)**: StatefulSet for log storage.
*   **[logstash.yaml](CODE/logstash.yaml)**: Log processing pipeline config.
*   **[kibana.yaml](CODE/kibana.yaml)**: Dashboard visualization service.
*   **[filebeat.yaml](CODE/filebeat.yaml)**: Log shipper configuration.

**🚀 Deployment Steps:**
1.  Ensure Minikube/K8s cluster is running.
2.  Apply the deployment manifests:
    ```bash
    kubectl apply -f CODE/k8s-deployment.yaml
    kubectl apply -f CODE/elasticsearch.yaml
    kubectl apply -f CODE/logstash.yaml
    kubectl apply -f CODE/kibana.yaml
    ```
3.  Expose the service:
    ```bash
    kubectl port-forward service/travel-planner-service 8501:8501
    ```

---

## 8. 📊 LLMOps & Observability

This project implements a full **LLMOps Pipeline** to ensure AI reliability.
*   **Logging:** Every AI interaction (Prompt, Response, Latency) is logged.
*   **Filebeat:** Ships logs from the application container.
*   **Elasticsearch:** Indexes logs for searchability.
*   **Kibana:** Visualizes metrics (Request count, Success rate, Latency).

![ELK Flow](Diagarm/Architeure%20Diagram/ELK_Flow.jpg)

---

## 9. 📞 Contact & Author

**Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer)**
> *Specializing in Generative AI, LLMOps, and Scalable System Design.*

*   💼 **LinkedIn:** [linkedin.com/in/ratneshkumar1998](https://www.linkedin.com/in/ratneshkumar1998/)
*   🐙 **GitHub:** [github.com/Ratnesh-181998](https://github.com/Ratnesh-181998)
*   📧 **Email:** rattudacsit2021gate@gmail.com

### 🔗 Project Resources
*   **Live Demo:** [Streamlit App](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
*   **Documentation:** [GitHub Wiki](https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary/wiki)
*   **Report Issue:** [GitHub Issues](https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary/issues)

---

## 📝 License

This project is licensed under the **MIT License**.
Copyright © 2024 Ratnesh Kumar Singh.
