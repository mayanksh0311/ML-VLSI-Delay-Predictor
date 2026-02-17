import joblib
import numpy as np
import pandas as pd
import math

# 1. Load the "Brain" (The trained model)
try:
    model = joblib.load('delay_predictor_model.pkl')
    print("✅ Agent loaded successfully. Ready to assist with VLSI timing.")
except FileNotFoundError:
    print("❌ Error: Model file not found. Did you run Step 3?")
    exit()

def predict_delay(bit_width):
    """
    Agent predicts delay for a given bit width.
    """
    # We know Gate Count is approx 5x Bit Width (Domain Knowledge)
    gate_count = bit_width * 5
    
    # Create a DataFrame for prediction (must match training format)
    features = pd.DataFrame([[bit_width, gate_count]], columns=['Bit_Width', 'Gate_Count'])
    
    # Ask the model
    predicted_delay = model.predict(features)[0]
    return predicted_delay

def optimize_design(max_delay_ns):
    """
    Agent 'reasons' backwards to find the best hardware for a constraint.
    """
    print(f"\n🔍 Searching for the best architecture under {max_delay_ns} ns...")
    
    best_bits = 0
    best_delay = 0
    
    # Iterate through possible designs (1-bit to 128-bit)
    for bits in range(1, 129):
        d = predict_delay(bits)
        if d < max_delay_ns:
            best_bits = bits
            best_delay = d
        else:
            # If delay exceeds limit, stop searching (physically impossible)
            break
            
    return best_bits, best_delay

# --- THE INTERACTIVE LOOP ---
while True:
    print("\n" + "="*40)
    print("🤖 VLSI CIRCUIT AGENT")
    print("1. Predict Delay (Forward Analysis)")
    print("2. Optimize Hardware (Reverse Design)")
    print("3. Exit")
    choice = input("Select an option (1/2/3): ")

    if choice == '1':
        try:
            bits = int(input("Enter Bit Width (e.g., 32): "))
            delay = predict_delay(bits)
            print(f"\n>> Result: A {bits}-bit Ripple Carry Adder will have a delay of approx {delay:.4f} ns.")
        except ValueError:
            print("Please enter a valid integer.")

    elif choice == '2':
        try:
            target = float(input("Enter Max Allowed Delay in ns (e.g., 5.0): "))
            bits, delay = optimize_design(target)
            if bits > 0:
                print(f"\n>> Recommendation: Use a {bits}-bit architecture.")
                print(f"   Predicted Delay: {delay:.4f} ns (matches constraint).")
            else:
                print("\n>> Impossible: Even a 1-bit adder is too slow for that constraint!")
        except ValueError:
            print("Please enter a valid number.")

    elif choice == '3':
        print("Agent shutting down.")
        break