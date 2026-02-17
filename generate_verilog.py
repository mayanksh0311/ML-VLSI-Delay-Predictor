import os

# 1. Create a folder to store the Verilog files if it doesn't exist
output_folder = "verilog_files"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def generate_adder(bit_width):
    """
    Generates a Verilog file for a Ripple Carry Adder of a specific bit_width.
    """
    filename = f"{output_folder}/adder_{bit_width}bit.v"
    
    # This is the template for the Verilog code
    verilog_code = f"""
module adder_{bit_width}bit (
    input [{bit_width-1}:0] A,
    input [{bit_width-1}:0] B,
    output [{bit_width-1}:0] Sum
);
    // Standard addition logic which synthesis tools will optimize
    assign Sum = A + B;
endmodule
"""
    # Write the code to the file
    with open(filename, "w") as f:
        f.write(verilog_code)
    print(f"Generated: {filename}")

# 2. Generate adders from 1-bit up to 64-bit
for i in range(1, 65):
    generate_adder(i)

print("\nSuccess! Generated 64 Verilog files.")