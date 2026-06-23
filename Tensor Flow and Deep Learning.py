import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Create a dummy dataset (e.g., inputs and expected binary outputs)
X_train = np.array([[1.0, 2.0], [2.0, 3.0], [3.0, 1.0], [4.0, 5.0]], dtype=np.float32)
y_train = np.array([[0], [0], [1], [1]], dtype=np.float32)

# 2. Build the Perceptron Model
model = Sequential([
    # 'Dense' creates fully connected weights.
    # 'units=1' means a single neuron (Perceptron).
    # 'sigmoid' is the activation function mapping outputs between 0 and 1.
    Dense(units=1, activation='sigmoid', input_shape=(2,))
])

# 3. Compile the model to set up the mathematical engine
# Binary crossentropy measures prediction error (loss).
# The optimizer uses 'Backpropagation' to update weights based on that error.
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

print("--- Training the Perceptron (Backpropagation in action) ---")
# 4. Train the model
model.fit(X_train, y_train, epochs=10, verbose=1)

print("\n--- Evaluating Model Performance ---")
# 5. Evaluation step
loss, accuracy = model.evaluate(X_train, y_train, verbose=0)
print(f"Final Model Accuracy: {accuracy * 100:.2f}%")