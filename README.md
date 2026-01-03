
# ✈️ Agentic AI Travel Planner & Itinerary Generator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=flat&logo=kubernetes&logoColor=white)](https://kubernetes.io/)
[![Elastic Stack](https://img.shields.io/badge/Elastic_Stack-005571?style=flat&logo=elasticsearch&logoColor=white)](https://www.elastic.co/)

<img width="890" height="403" alt="image" src="https://github.com/user-attachments/assets/11e81bac-317e-4fe3-bf1d-c5a95d16e1d9" />


**An Enterprise-Grade, Agentic GenAI Application for Personalized Travel Planning.**

> *Designed for scalability, observability, and autonomous reasoning using LangChain, Groq, and Kubernetes.*

---

## 📑 Contents
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

## 3. 🖼️ User Interface & Dashboard Tabs

The application features a premium, glassmorphism-inspired UI organized into **6 Interactive Tabs**, designed for both user engagement and technical deep-dives.

### 1️⃣ Demo Tab 🎯
**The Core Experience:**
*   **Live AI Travel Planner:** Interactive form to input City and Interests.
*   **Real-Time Generation:** Watches the AI agent reason and build the itinerary live.
*   **Visual Showcase:** Dynamic image grid representing different travel themes.
*   **User Experience:** Includes sidebar tips, request statistics, and auto-logging to the system monitor.

### 2️⃣ About Tab 📖
**Project Context & Positioning:**
*   **Objectives:** Breakdowns of Personalized AI Itineraries, Budget-Aware Planning, and Fast Inference.
*   **Key Highlights:** Focuses on Agentic Workflows, Real-Time Generation, and LLMOps readiness.
*   **Resume-Ready Points:** "Click to view" expander with bullet points tailored for technical interviews.

### 3️⃣ Tech Stack Tab 🛠️
**Deep Dive into Technologies:**
*   **AI/GenAI Layer:** Groq LPU™ & LangChain orchestration.
*   **Frontend:** Streamlit with custom CSS.
*   **Cloud & Infra:** GCP VM, GitHub Actions.
*   **Containerization:** Docker & Kubernetes (Minikube).
*   **Observability:** Full ELK Stack (Filebeat, Logstash, Elasticsearch, Kibana).

### 4️⃣ HLD & LLD Tab 🏗️
**System Design Breakdown:**
*   **High-Level Design (HLD):** Architecture diagrams showing User, AI, App, Infra, and Observability layers.
*   **Low-Level Design (LLD):** Detailed component views including `app.py`, `config.py`, and `planner.py` logic flows.
*   **Comparison Table:** a clear breakdown of HLD vs. LLD for educational purposes.

### 5️⃣ Architecture Tab 📐
**The Production Workflow:**
*   **17-Step Execution Flow:** From User Input to Kubernetes Deployment.
*   **4-Layer Defense:**
    *   🟦 **Development Layer:** Setup, Config, Logic.
    *   🟨 **Containerization Layer:** Docker, K8s Pods.
    *   🟪 **Cloud Layer:** GCP VM, Version Control.
    *   🟩 **Build & Monitor:** Deployment & ELK tracking.

### 6️⃣ System Logs Tab 📊
**Real-Time LLM Observability:**
*   **Live Monitoring:** View system logs with accurate **IST Timezone** timestamps.
*   **Health Status:** Color-coded (Green=Success, Red=Error) indicators.
*   **Metrics:** Real-time counters for Total Requests, Success Rate, and Error Rate.
*   **Audit Trail:** Complete history of every user interaction and AI response.

---

## 4. 🛠️ Technology Stack

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


<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=24,20,12,6&height=3" width="100%">


## 9. Developer & Project Resources 

**Ratnesh Kumar Singh | Data Scientist (AI/ML Engineer)**
> *Specializing in AI/ML ,Agentic & Generative AI, MLOps,LLMOps,AIOps and Scalable System Design.*


### 🔗 Project Resources
*   **Live Demo:** [Streamlit App](https://appudtzei3tyyttd6xjhwur.streamlit.app/)
*   **Documentation:** [GitHub Wiki](https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary/wiki)
*   **Report Issue:** [GitHub Issues](https://github.com/Ratnesh-181998/Agentic-AI-Travel-Planner-Itinerary/issues)

---


## 📜 **License**

![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge&logo=opensourceinitiative&logoColor=white)

This project is licensed under the **MIT License**.
Copyright © 2024 Ratnesh Kumar Singh.

---

# 📞 **CONTACT & NETWORKING** 📞


[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ratneshkumar1998/)
[![GitHub](https://img.shields.io/badge/🐙_GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Ratnesh-181998)
[![Portfolio](https://img.shields.io/badge/🌐_Portfolio-FF6B6B?style=for-the-badge&logo=google-chrome&logoColor=white)](https://share.streamlit.io/user/ratnesh-181998)
[![Email](https://img.shields.io/badge/✉️_Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rattudacsit2021gate@gmail.com)


---

## 📊 **GitHub Stats & Metrics** 📊



![Profile Views](https://komarev.com/ghpvc/?username=Ratnesh-181998&color=blueviolet&style=for-the-badge&label=PROFILE+VIEWS)





<img src="https://github-readme-streak-stats.herokuapp.com/?user=Ratnesh-181998&theme=radical&hide_border=true&background=0D1117&stroke=4ECDC4&ring=F38181&fire=FF6B6B&currStreakLabel=4ECDC4" width="48%" />




<img src="https://github-readme-activity-graph.vercel.app/graph?username=Ratnesh-181998&theme=react-dark&hide_border=true&bg_color=0D1117&color=4ECDC4&line=F38181&point=FF6B6B" width="48%" />

---

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&duration=3000&pause=1000&color=4ECDC4&center=true&vCenter=true&width=600&lines=Ratnesh+Kumar+Singh;Data+Scientist+%7C+AI%2FML+Engineer;4%2B+Years+Building+Production+AI+Systems" alt="Typing SVG" />

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=18&duration=2000&pause=1000&color=F38181&center=true&vCenter=true&width=600&lines=Built+with+passion+for+the+AI+Community+🚀;Innovating+the+Future+of+AI+%26+ML;MLOps+%7C+LLMOps+%7C+AIOps+%7C+GenAI+%7C+AgenticAI+Excellence" alt="Footer Typing SVG" />


<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%">

