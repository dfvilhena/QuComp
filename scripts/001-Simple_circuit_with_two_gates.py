import numpy as np
from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Using Aer's qasm simulator
# Aer is "high performance simulator framework" for Qiskit
# qasm is a "Noisy quantum circuit simulator backend"
simulator = Aer.get_backend('qasm_simulator')

# Create a quantum circuit object
# This one has 2 qubit and 2 bits
circuit = QuantumCircuit(2, 2)

# Add a Hadamard gate to qubit 0
circuit.h(0);

# Add a CNOT gate with qubit 0 being the control and 1 the operated on
circuit.cx(0, 1);

# Map measurements to classical bits
circuit.measure([0,1], [0,1]);

# Show the circuit in the output
print(circuit)

# Create the circuit figure using Matplotlib
circuit.draw(output='mpl', filename='test.png')

# Using latex
##circuit.draw(output='latex_source', filename='test.tex')

# Create a job to simulate the circuit with 1000 iterations
# execute() is a function, documentation at https://qiskit.org/documentation/_modules/qiskit/execute.html
job = execute(circuit, simulator, shots=1000);

# Get results from job
result = job.result();

# Get the counts for each result
# With both input qubits being |0>, only |00> and |11> outputs are possible
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# A nice figure
plot_histogram(counts)

# Show everything generated with matplotlib - the circuit and the histogram
plt.show();