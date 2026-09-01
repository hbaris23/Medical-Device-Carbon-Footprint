# 🏥 Medical Device Energy & Carbon Footprint Analysis System

A Python and Streamlit-based analytical dashboard for evaluating the energy consumption, electricity cost, and carbon footprint of medical devices.

The system analyzes medical device usage data, calculates annual energy consumption and CO₂e emissions, and provides interactive energy-saving scenarios.

---

## 📌 Project Overview

Medical devices operate continuously or for extended periods in healthcare environments. Their energy consumption can contribute significantly to operational costs and environmental impact.

This project provides a simple analytical tool to:

- Calculate daily and annual energy consumption
- Estimate annual CO₂e emissions
- Estimate electricity costs
- Compare medical devices
- Identify high-energy-consuming devices
- Generate device-specific energy-saving recommendations
- Simulate different energy-saving scenarios
- Estimate potential financial and environmental savings

---

## 🚀 Features

### ⚡ Energy Analysis
- Daily energy consumption
- Annual energy consumption
- Device-based energy comparison
- Identification of the highest energy-consuming device

### 🌱 Carbon Footprint Analysis
- Daily CO₂e estimation
- Annual CO₂e estimation
- Device-based carbon footprint comparison

### 💰 Cost Analysis
- User-defined electricity price
- Daily electricity cost
- Monthly electricity cost
- Annual electricity cost
- Device-based annual cost analysis

### 📉 Energy Saving Simulation
Users can select an energy-saving rate between 0% and 50%.

The system calculates:

- Energy savings
- CO₂e reduction
- Financial savings
- Remaining annual energy consumption
- Remaining annual carbon footprint
- Remaining annual cost

### 🤖 Smart Device Analysis
The application provides device-specific recommendations based on energy consumption and standby time.

---

## 🛠️ Technologies

- Python
- Streamlit
- Pandas
- Matplotlib
- CSV

---

## 📂 Project Structure

```text
Medical-Device-Carbon-Footprint/
│
├── data/
│   └── devices.csv
│
├── outputs/
│   ├── energy_analysis.png
│   └── carbon_analysis.png
│
├── src/
│   ├── analysis.py
│   ├── dashboard.py
│   ├── main.py
│   ├── recommendations.py
│   ├── savings.py
│   └── total_savings.py
│
├── .gitignore
├── README.md
└── requirements.txt