# 🏎️ ApexPred
> Deep Learning-based F1 Driver Performance Classification using Telemetry Data

## 📌 Project Overview
This project classifies Formula 1 drivers based on their **driving style and performance**, using **telemetry data** such as throttle, brake, speed, gear, and RPM. The goal is to build a model that can identify whether a driver is **aggressive**, **conservative**, or **balanced**, based on lap-level data.

This project was built for the course **CMPE 471/CMPS 479: Deep Learning** at Qatar University.

---

## 📂 Repository Structure
```
├── data/                   # Raw and preprocessed telemetry data
├── notebooks/              # Jupyter notebooks for EDA, preprocessing, experiments
├── src/
│   ├── model.py            # Model architecture definition
│   ├── train.py            # Training pipeline
│   ├── evaluate.py         # Evaluation and metrics
│   └── utils.py            # Utility functions (e.g., data loaders, metrics)
├── results/
│   ├── confusion\_matrix.png
│   └── training\_curves.png
├── requirements.txt        # Python dependencies
└── README.md               # Project overview

```

---

## 🧠 Model Architecture
- Input: Normalized telemetry vectors per lap
- Model: 
  - Baseline: Logistic Regression / MLP
  - Main: RNN (LSTM/GRU) with optional attention
- Output: Performance Class (Aggressive / Balanced / Conservative)

---

## 🛠️ Setup Instructions
### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/ApexPred.git
cd ApexPred
````

### 2. Create a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 📊 Example Telemetry Features

* `Speed` (km/h)
* `Throttle` (%)
* `Brake` (%)
* `Gear`
* `RPM`
* `DRS`, `nGear`, `Time`, etc.

---

## 🧪 Evaluation Metrics

* Accuracy
* Precision / Recall / F1-Score
* Confusion Matrix
* Training/Validation Loss Curves

---

## 📈 Results Snapshot


---

## 📚 References

* [FastF1 Telemetry Library](https://theoehrly.github.io/Fast-F1/)
* Deep Learning Lectures - CMPE 471/CMPS 479
* PyTorch, scikit-learn

---

## 👤 Author

**Mohamed Elansari**
Qatar University – Spring 2025
Project for CMPE 471

