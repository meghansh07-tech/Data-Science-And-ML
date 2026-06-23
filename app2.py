import os

# 1. CRUCIAL ENVIRONMENT FLAGS (Must be at the very top before importing TensorFlow)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Prevents annoying backend warnings from cluttering the screen

import streamlit as st
import numpy as np
import tensorflow as tf

# 2. Streamlit Page UI Configuration
st.set_page_config(page_title="Perceptron Classifier", page_icon="🧠", layout="centered")
st.title("🧠 Neural Network Perceptron Gateway")
st.write(
    "This interactive dashboard loads your trained single-neuron TensorFlow model to classify data points in real time!")


# 3. Securely Load the Pre-Trained Native Keras Model
@st.cache_resource  # Keeps the model cached in memory so it doesn't reload on every slider change
def load_perceptron():
    # Make sure this filename matches exactly what tensor.py saved!
    return tf.keras.models.load_model('perceptron_model.keras')


try:
    model = load_perceptron()
    st.sidebar.success("✅ TensorFlow Model Loaded Successfully!")
except Exception as e:
    st.sidebar.error("❌ Missing Model File!")
    st.sidebar.write("Please run your `python tensor.py` script first to generate the `perceptron_model.keras` asset.")

# 4. User Interface Sliders (Inputs representing the 2 features)
st.write("### 🎛️ Adjust Input Features:")
feature_1 = st.slider("Feature 1 (e.g., Structural Thickness)", 0.0, 5.0, 2.5, step=0.1)
feature_2 = st.slider("Feature 2 (e.g., Applied Mechanical Stress)", 0.0, 5.0, 2.5, step=0.1)

# 5. Inference Activation Button
if st.button("Run Neural Network Inference", type="primary"):

    # Format the user inputs into a 2D NumPy array matrix expected by TensorFlow: [[feat1, feat2]]
    input_data = np.array([[feature_1, feature_2]], dtype=np.float32)

    # Execute the forward pass through the perceptron's weights
    raw_prediction = model.predict(input_data, verbose=0)
    probability = float(raw_prediction[0][0])

    # Apply the decision boundary threshold (0.5) to determine the binary class
    binary_class = 1 if probability >= 0.5 else 0

    # 6. Display the Dynamic Output Results
    st.write("---")
    st.subheader("📊 Network Prediction Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Raw Sigmoid Output (Probability)", value=f"{probability:.4f}")
    with col2:
        if binary_class == 1:
            st.error("🎯 Result: **Class 1** (High Risk / Triggered)")
        else:
            st.success("🎯 Result: **Class 0** (Safe / Nominal)")

    # Quick text explanation for clarity
    st.caption(
        f"Reasoning: The sigmoid activation function squashed the mathematical node output to a probability of {probability * 100:.1f}%. "
        f"Since this is {'above' if binary_class == 1 else 'below'} the 50% activation threshold, the Perceptron fires a **Class {binary_class}** signal.")