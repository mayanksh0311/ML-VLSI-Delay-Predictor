# ⚡ ML-Based Propagation Delay Prediction for VLSI Circuits

### A Machine Learning Agent that bridges the gap between Digital Electronics and AI.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![Domain](https://img.shields.io/badge/Domain-VLSI%20%2F%20Embedded-green)

## 📌 Overview
In traditional VLSI design, determining the speed of a circuit (**Propagation Delay**) requires running computationally expensive **Static Timing Analysis (STA)** tools like Vivado or PrimeTime. This process is slow and hinders rapid prototyping.

This project introduces an **AI-driven approach**:
1.  **Generates** synthetic Verilog hardware designs (Ripple Carry Adders).
2.  **Simulates** the physics of signal propagation to create a dataset.
3.  **Trains** a Machine Learning model to predict delay instantly.
4.  **Deploys** an "Intelligent Agent" that can reverse-engineer design constraints (e.g., *"Find me the largest adder that runs under 5ns"*).

## 🚀 Key Features
* **Automated Dataset Generation:** Python scripts automatically write Verilog RTL code for 64+ circuit variations.
* **Physics-Aware Simulation:** Simulates linear delay scaling and random manufacturing variations (noise).
* **High-Accuracy Prediction:** Achieved **>99% Accuracy ($R^2$)** using Linear Regression on circuit features.
* **Design Optimization Agent:** An interactive CLI tool that recommends optimal hardware architectures based on user-defined timing constraints.


## 📂 Project Structure
```text
├── generate_verilog.py    # Generates raw Verilog (.v) files for 1-bit to 64-bit adders
├── generate_dataset.py    # Simulates synthesis & timing analysis to create training data
├── train_model.py         # Trains the Linear Regression model & saves it (.pkl)
├── circuit_agent.py       # The interactive "AI Consultant" for users
├── circuit_data.csv       # The generated dataset (Features: Bit Width, Gate Count)
├── delay_predictor_model.pkl # The saved ML brain
└── README.md              # Project documentation
```

## 🛠️ Installation
Prerequisites
Ensure you have Python 3.x installed along with the following libraries:
```bash
pip install pandas numpy scikit-learn joblib
```

## 🚀 User Guide
Follow these steps to reproduce the project from scratch:

Step 1: Generate Hardware Designs
Create the Verilog hardware description files for our dataset. This script generates 64 unique Ripple Carry Adder designs.
```bash
python generate_verilog.py
```
Output: Creates a verilog_files directory populated with .v files.

Step 2: Create Training Data
Simulate the timing behavior of these circuits. This script uses a physics-based model (linear scaling + noise) to generate circuit_data.csv.
```bash
python generate_dataset.py
```
Step 3: Train the Model
Train the Machine Learning model. It will output the accuracy score and save the trained model as delay_predictor_model.pkl.
```bash
python train_model.py
```
Expected Output: Accuracy Score (R2): > 0.99
Step 4: Run the AI Agent
Launch the interactive tool to predict delays or optimize designs.
```bash
python circuit_agent.py
```

## 🧠 Theory: Why this works?

This project focuses on the **Ripple Carry Adder (RCA)**.



In an RCA, the carry bit must "ripple" through every full adder stage from the Least Significant Bit (LSB) to the Most Significant Bit (MSB). Because of this structure, the worst-case propagation delay is linearly proportional to the number of bits.

The delay ($T_{delay}$) can be approximated as:

$$T_{delay} \approx N \times T_{carry} + T_{noise}$$

Where:
* $N$ = Bit Width (Input Feature)
* $T_{carry}$ = Delay of a single Full Adder stage
* $T_{noise}$ = Random variations (routing, process variation)

Since the relationship is fundamentally **Linear**, a **Linear Regression** model captures the physics perfectly ($R^2 \approx 0.99$), proving that simple ML models can effectively approximate complex digital hardware behaviors.

## 📊 Results

The model was trained on 64 circuit variations and achieved the following performance metrics:

* **Accuracy ($R^2$ Score):** 0.9953
* **Mean Absolute Error (MAE):** ~0.23 ns

**Agent Demo:**
```text
========================================
🤖 VLSI CIRCUIT AGENT
1. Predict Delay (Forward Analysis)
2. Optimize Hardware (Reverse Design)
3. Exit

> Select: 2
> Enter Max Allowed Delay in ns: 10.0

🔍 Searching for best architecture under 10.0 ns...
>> Recommendation: Use a 50-bit architecture.
   Predicted Delay: 9.9262 ns (matches constraint).
```
🔮 Future Improvements
Real-World Data: Integrate with OpenSTA to parse actual timing reports instead of simulated physics.

Complex Circuits: Expand support for non-linear circuits like Carry Lookahead Adders (CLA) or Wallace Tree Multipliers.

GUI: Deploy the agent as a web app using Streamlit for easier visualization.

👨‍💻 Author
Mayank Sharma
