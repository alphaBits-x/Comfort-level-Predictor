# Comfort-level-Predictor
 fuzzy logic-based system that predicts comfort levels based on temperature and humidity.

This project implements a fuzzy logic system to determine **comfort levels** based on **temperature** and **humidity**. Using the `scikit-fuzzy` library, the system categorizes comfort into *uncomfortable, neutral, and comfortable* using fuzzy membership functions and inference rules.

## 🚀 Features
- Fuzzy logic-based decision-making.
- Membership functions for **Temperature, Humidity, and Comfort Level**.
- Rule-based comfort level classification.
- Visualization of fuzzy sets and results.

## 🔧 How It Works
1. Define fuzzy membership functions:
   - **Temperature:** Low (0-20°C), Medium (15-35°C), High (20-35°C).
   - **Humidity:** Low (0-40%), Medium (30-80%), High (50-80%).
   - **Comfort Level:** Uncomfortable (0-4), Neutral (3-7), Comfortable (6-10).
2. Apply fuzzy rules to classify comfort levels.
3. Compute the comfort level using the given temperature and humidity inputs.
