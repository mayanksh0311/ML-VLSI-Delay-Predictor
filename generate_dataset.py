import pandas as pd
import numpy as np
import random

# We will create a dataset with 3 columns:
# 1. Bit_Width (Feature)
# 2. Gate_Count (Feature - roughly 5 gates per bit for a full adder)
# 3. Delay_ns (Target - The value we want to predict)

data = []

print("Simulating synthesis tool run...")

for bit_width in range(1, 65):
    # --- PHYSICS SIMULATION ---
    # A Full Adder typically has ~5 gates.
    gate_count = bit_width * 5 
    
    # In a Ripple Carry Adder, delay is roughly linear: T_total = T_carry * N
    # We assume a standard gate delay of ~0.1ns.
    # We add 'random.uniform' to simulate real-world routing/wire variations.
    base_delay = (bit_width * 0.2) 
    noise = random.uniform(-0.5, 0.5) # Random noise
    
    total_delay = base_delay + noise
    
    # Ensure delay is never negative
    if total_delay < 0.1: total_delay = 0.1
    
    # Append to our list
    data.append([bit_width, gate_count, round(total_delay, 3)])

# Save to CSV
df = pd.DataFrame(data, columns=["Bit_Width", "Gate_Count", "Delay_ns"])
df.to_csv("circuit_data.csv", index=False)

print("Success! Created 'circuit_data.csv' with 64 samples.")
print(df.head()) # Show first 5 rows