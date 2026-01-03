# 🎯 AI Travel Planner - Professional Dashboard

## 🚀 Quick Start

### Running the Dashboard

```bash
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the comprehensive dashboard
streamlit run streamlit_dashboard.py --server.port 8502
```

**Access URLs:**
- **Local:** http://localhost:8502
- **Network:** http://192.168.1.3:8502

### Running the Original App

```bash
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the original simple app
streamlit run app.py
```

**Access URLs:**
- **Local:** http://localhost:8501
- **Network:** http://192.168.1.3:8501

---

## 📊 Dashboard Features

### 🎨 Premium Design Elements
- ✅ **Gradient Color Schemes** - Professional purple/blue gradients
- ✅ **Google Fonts** - Inter font family for modern typography
- ✅ **Glassmorphism Effects** - Modern card designs with shadows
- ✅ **Smooth Animations** - Hover effects and transitions
- ✅ **Responsive Layout** - Works on all screen sizes

### 📑 Six Comprehensive Tabs

#### 1️⃣ **Demo Tab** - Live AI Travel Planner
- Interactive form for city and interests input
- Real-time itinerary generation using Groq LLM
- Tips and statistics sidebar
- Success/error handling with logging

#### 2️⃣ **About Tab** - Project Overview
- Complete project description
- Key objectives and highlights
- End-to-end flow diagram
- Resume-ready positioning statement

#### 3️⃣ **Tech Stack Tab** - Technology Details
- AI/GenAI Layer (Groq, LangChain)
- Frontend Layer (Streamlit)
- Cloud & Infrastructure (GCP, GitHub)
- Containerization (Docker, Kubernetes, kubectl)
- ELK Stack (Filebeat, Logstash, Elasticsearch, Kibana)
- Complete tech stack summary

#### 4️⃣ **HLD & LLD Tab** - Architecture Design
- High-Level Design (HLD) diagram
- Low-Level Design (LLD) components
- Visual architecture diagrams
- Detailed component breakdown
- Key features list

#### 5️⃣ **Architecture Tab** - System Design
- Complete workflow diagram
- Development layer (Steps 1-5)
- Containerization & Deployment layer (Steps 6-11)
- Version control & cloud setup (Steps 12-14)
- Build, deploy & monitor (Steps 15-17)
- Architecture diagrams from folder

#### 6️⃣ **System Logs Tab** - Activity Monitor
- Real-time IST timezone display
- Activity logs with timestamps
- Success/error tracking
- Statistics dashboard
- System information
- Clear logs functionality

### 🎯 Special Features

#### Top-Right Header Box
```
Ratnesh Kumar Singh
Data Scientist (AI/ML Engineer)
4+ Years Experience
```
- Fixed position in top-right corner
- Gradient background with shadow
- Professional styling

#### Sidebar
- Project overview card
- Key features list
- Quick links section
- Gradient background

#### IST Timezone Logging
- All logs captured in IST (UTC+5:30)
- Format: `YYYY-MM-DD HH:MM:SS IST`
- Real-time timestamp display

---

## 📁 Project Structure

```
CODE/
├── app.py                      # Original simple app
├── streamlit_dashboard.py      # New comprehensive dashboard
├── .env                        # Environment variables (GROQ_API_KEY)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── k8s-deployment.yaml         # Kubernetes deployment
├── src/
│   ├── chains/
│   │   └── itinerary_chain.py  # LangChain itinerary generation
│   ├── config/
│   │   └── config.py           # Configuration settings
│   ├── core/
│   │   └── planner.py          # Travel planner core logic
│   └── utils/
│       ├── custom_exception.py # Exception handling
│       └── logger.py           # Logging utilities
└── venv/                       # Virtual environment
```

---

## 🎨 Design Philosophy

### Color Palette
- **Primary Gradient:** `#667eea` → `#764ba2` (Purple/Blue)
- **Success Gradient:** `#11998e` → `#38ef7d` (Teal/Green)
- **Error Color:** `#e74c3c` (Red)
- **Background:** `#f8f9fa` → `#e9ecef` (Light Gray)

### Typography
- **Font Family:** Inter (Google Fonts)
- **Weights:** 300 (Light), 400 (Regular), 600 (Semi-Bold), 700 (Bold)

### UI Components
- **Cards:** White background, rounded corners, subtle shadows
- **Tabs:** Gradient active state, hover effects
- **Buttons:** Gradient background, hover animations
- **Logs:** Monospace font, color-coded status

---

## 📊 Content Sources

All content is dynamically loaded from:

### Text Files (Project Doc folder)
- `About.txt` - Project description and tech stack details
- `tch Stack.txt` - HLD/LLD and technology information
- `Architecture.txt` - Architecture steps and flow

### Diagrams (Diagarm folder)
- `About Diagram/` - Project overview diagrams
- `Architeure Diagram/` - Architecture workflow diagrams
- `HLD & LLD Daigram/` - Design diagrams
- `Tech Stack Diagram/` - Technology stack visuals

### Root Files
- `AI+travel+planner+Workflow.png` - Main workflow diagram
- `FULL DOCUMENTATION.md` - Complete setup documentation

---

## 🔧 Technical Details

### Dependencies
```
langchain
langchain_core
langchain_groq
langchain_community
python-dotenv
streamlit
pytz  # For IST timezone
```

### Environment Variables
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### Python Version
- **Required:** Python 3.11.2
- **Virtual Environment:** venv

---

## 🎯 Key Differences: Original vs Dashboard

| Feature | Original App | Dashboard App |
|---------|-------------|---------------|
| **File** | `app.py` | `streamlit_dashboard.py` |
| **Port** | 8501 | 8502 |
| **Tabs** | None | 6 comprehensive tabs |
| **Design** | Basic | Premium with gradients |
| **Logging** | None | IST timezone logs |
| **Documentation** | None | Complete project docs |
| **Diagrams** | None | All architecture diagrams |
| **Header** | Simple title | Professional header box |
| **Sidebar** | None | Project overview |

---

## 📝 Usage Tips

### For Demo Tab
1. Enter a city name (e.g., "Paris", "Tokyo", "Mumbai")
2. Add interests separated by commas (e.g., "museums, food, history")
3. Click "Generate Itinerary"
4. View AI-generated travel plan
5. Check logs in System Logs tab

### For Presentations
- Use **Architecture Tab** for technical discussions
- Use **Tech Stack Tab** for technology overview
- Use **Demo Tab** for live demonstrations
- Use **System Logs Tab** for monitoring

### For Recruiters/Interviews
- Show **About Tab** for project overview
- Demonstrate **Demo Tab** for functionality
- Explain **HLD & LLD Tab** for design thinking
- Highlight **Tech Stack Tab** for technical skills

---

## 🚀 Deployment Notes

### Local Development
- Both apps can run simultaneously on different ports
- Original app: Port 8501
- Dashboard app: Port 8502

### Production Deployment
- Use `streamlit_dashboard.py` for production
- Configure environment variables
- Set up proper logging infrastructure
- Enable HTTPS for security

---

## 📞 Support & Contact

**Developer:** Ratnesh Kumar Singh  
**Role:** Data Scientist (AI/ML Engineer)  
**Experience:** 4+ Years  

**Project Type:** Agentic GenAI Application with LLMOps  
**Tech Stack:** LangChain, Groq, Streamlit, Docker, Kubernetes, ELK Stack  

---

## 📄 License

This project demonstrates production-grade GenAI application development with full DevOps and LLMOps integration.

---

**Last Updated:** 2026-01-03  
**Version:** 1.0.0  
**Status:** ✅ Production Ready
