import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load data
data = pd.read_csv('bank_note_data.csv')

# 2. Scale features (Drop the target 'Class' column)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data.drop('Class', axis=1))

# 3. Separate inputs (X) and labels (y)
X = scaled_features  # We can pass the numpy array directly to Keras!
y = data['Class'].values

# 4. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5. Build the DNN Classifier using Modern Keras [10, 20, 10 hidden units]
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),                  # 4 input features
    tf.keras.layers.Dense(10, activation='relu'),       # Hidden Layer 1 (10 units)
    tf.keras.layers.Dense(20, activation='relu'),       # Hidden Layer 2 (20 units)
    tf.keras.layers.Dense(10, activation='relu'),       # Hidden Layer 3 (10 units)
    tf.keras.layers.Dense(1, activation='sigmoid')      # Output Layer (Binary classification)
])

# 6. Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 7. Train the model (No complex input_fn needed anymore!)
print("--- Training Modern DNN ---")
model.fit(X_train, y_train, batch_size=20, epochs=30, verbose=1)

# 8. Generate Predictions
print("\n--- Running Predictions ---")
raw_predictions = model.predict(X_test, verbose=0)
# Convert Sigmoid probabilities (0.0 to 1.0) into hard 0 or 1 classes
final_preds = (raw_predictions > 0.5).astype(int).flatten()

# 9. Performance Metrics Report
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_test, final_preds))

print("\n📋 Classification Report:")
print(classification_report(y_test, final_preds))

# 10. Save your freshly trained native model asset
model.save('perceptron_model.keras')
print("🎉 SUCCESS: Model saved as 'perceptron_model.keras'")