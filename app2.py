import numpy as np
import tensorflow as tf

# 1. Load your freshly saved banknote model
model = tf.keras.models.load_model('perceptron_model.keras')

# 2. Fabricate a fake banknote reading: [Variance, Skewness, Curtosis, Entropy]
fake_note = np.array([[2.5, -1.2, 3.4, -0.5]], dtype=np.float32)

# 3. Calculate prediction
prob = model.predict(fake_note, verbose=0)[0][0]

print(f"Raw Probability: {prob:.4f}")
print(f"Prediction: {'Counterfeit' if prob >= 0.5 else 'Authentic'}")