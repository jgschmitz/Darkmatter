# Darkmatter 🚀👽✨

Ever wondered what happens when you mix **MongoDB**, **SETI's cosmic data**, and the power of the **cloud**?  
Welcome to **Darkmatter** — a side project born from curiosity, caffeine, lots of pizza. 🍕

**Version 2.0** - Now with enhanced machine learning pipeline, proper project structure, and improved data visualization!

---

## 🌌 What is this?

Darkmatter is a **comprehensive SETI data processing pipeline** that takes **huge public datasets from SETI**, loads them into **MongoDB**, and provides advanced analytics and machine learning capabilities for signal detection and analysis.

Features include:
- **Real-time data ingestion** from SETI public datasets
- **Advanced signal classification** using TensorFlow and scikit-learn
- **Interactive data visualization** with React and Grafana integration
- **ROC curve analysis** for model performance evaluation
- **Scalable cloud deployment** on Google Cloud Platform

---

## ⚙️ Tech Stack

### Backend & Data Processing
- **Python 3.10+** with pandas, numpy, scikit-learn, TensorFlow
- **MongoDB** – flexible, document-based storage for cosmic data
- **Apache Drill** – sub-second SQL queries across MongoDB collections
- **PyMongo** – Python MongoDB driver with async support

### Frontend & Visualization
- **Node.js 16+** with Express.js REST API
- **React 18** with modern hooks and Tailwind CSS
- **Grafana** – real-time dashboards and cosmic signal visualization
- **Plotly & Matplotlib** – statistical plots and ROC curves

### Cloud & DevOps
- **Google Cloud Platform** – scalable infrastructure
- **Docker** – containerized deployment
- **GitHub Actions** – CI/CD pipeline (coming soon)

---

## 🚀 Quick Start

### Prerequisites
- **Node.js 16+** and **npm 8+**
- **Python 3.8+** with pip
- **MongoDB** (local or Atlas)
- **Git**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jgschmitz/Darkmatter.git
   cd Darkmatter
   ```

2. **Install Node.js dependencies**
   ```bash
   npm install
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB URI and SETI API credentials
   ```

5. **Start the application**
   ```bash
   # Start the backend API server
   npm run dev
   
   # In another terminal, run Python analysis
   python roc.curve.py
   ```

---

## 📊 What Can You Do?

### Data Processing
- **Ingest unlimited SETI datasets** with automatic CSV processing
- **Store and index cosmic signals** in MongoDB with full-text search
- **Run blazing-fast SQL queries** with Apache Drill integration
- **Process signal features** with pandas and numpy

### Machine Learning
- **Train classification models** to detect potential signals vs noise
- **Compare model performance** with comprehensive ROC curve analysis
- **Use TensorFlow/Keras** for deep learning signal recognition
- **Evaluate models** with precision, recall, F1-score, and AUC metrics

### Visualization & Analysis
- **Interactive web interface** for signal comparison and reporting
- **Real-time dashboards** with Grafana integration
- **Statistical visualizations** with matplotlib and seaborn
- **Export analysis results** in multiple formats (CSV, JSON, PNG)

---

## 🛠️ Development

### Project Structure
```
Darkmatter/
├── backendExpress.jsx      # Express.js API server
├── frontendTailwind.jsx    # React frontend component
├── Insert-MongoDB.py       # MongoDB data insertion utilities
├── TensorConnect.py        # TensorFlow model training
├── pandas-insertmtpl.py    # Pandas data processing pipeline  
├── roc.curve.py           # Model evaluation and ROC analysis
├── configure-gce.sh       # Google Cloud setup script
├── package.json           # Node.js dependencies and scripts
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

### Available Scripts

**Node.js/Frontend:**
```bash
npm start          # Start production server
npm run dev        # Start development server with nodemon
npm run lint       # Run ESLint code analysis
npm run format     # Format code with Prettier
```

**Python/ML:**
```bash
python pandas-insertmtpl.py    # Process SETI CSV datasets
python roc.curve.py            # Run ML model evaluation
python TensorConnect.py        # Train TensorFlow models
python Insert-MongoDB.py       # Insert data into MongoDB
```

### Code Quality
- **ESLint** for JavaScript/JSX linting
- **Prettier** for code formatting
- **Black** for Python code formatting
- **MyPy** for Python type checking
- **Pytest** for Python testing

---

## 🌩️ Cloud Deployment

Deploy to Google Cloud Platform using the provided configuration:

```bash
# Configure GCE with MapR connector
chmod +x configure-gce.sh
./configure-gce.sh

# Deploy with Docker (coming soon)
docker build -t darkmatter:latest .
docker run -p 5000:5000 darkmatter:latest
```

---

## 📈 Performance

- **Sub-second queries** on millions of SETI records with Apache Drill
- **Real-time data ingestion** supporting high-velocity cosmic data streams  
- **Scalable architecture** handling terabytes of signal data
- **Optimized ML pipeline** with GPU acceleration for TensorFlow models

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **SETI Institute** for providing public datasets
- **MongoDB** community for excellent documentation  
- **Apache Drill** team for sub-second query performance
- **Google Cloud Platform** for scalable infrastructure
- **The cosmic coffee** that made this possible ☕

---

## 📊 Project Stats

- **3,686+ commits** of cosmic code evolution
- **Multiple languages**: Python, JavaScript, Shell scripting
- **Production-ready**: Deployed on Google Cloud Platform
- **Community-driven**: Open source SETI data analysis

**Ready to explore the universe through data? Let's find those signals! 🛸**
