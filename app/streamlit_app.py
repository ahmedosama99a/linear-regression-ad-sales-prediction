import streamlit as st
import numpy as np
import joblib

# تحميل النموذج المدرب
model = joblib.load(r"linear_model.pkl")  # تأكد من وجود هذا الملف في نفس المجلد

# اختيار اللغة
lang = st.selectbox("🔤 اختر اللغة / Select Language", ["العربية", "English"])

# واجهة عربية
if lang == "العربية":
    st.set_page_config(page_title="توقع المبيعات", layout="centered")
    st.title("📊 توقع المبيعات بناءً على ميزانية الإعلانات")
    st.write("💰 أدخل ميزانية الإعلان لكل قناة (بالدولار):")

    tv = st.number_input("📺 ميزانية التلفزيون", min_value=0.0, value=100.0)
    radio = st.number_input("📻 ميزانية الراديو", min_value=0.0, value=20.0)
    newspaper = st.number_input("📰 ميزانية الصحف", min_value=0.0, value=10.0)

    if st.button("🔍 احسب التوقع"):
        input_data = np.array([[tv, radio, newspaper]])
        prediction = model.predict(input_data)[0]
        st.success(f"🔮 التوقع: {prediction:.2f} دولار 💵 في المبيعات")

# واجهة إنجليزية
else:
    st.set_page_config(page_title="Sales Prediction", layout="centered")
    st.title("📊 Predict Sales Based on Ad Budget")
    st.write("💰 Enter your advertising budget for each channel (in USD):")

    tv = st.number_input("📺 TV Ad Budget", min_value=0.0, value=100.0)
    radio = st.number_input("📻 Radio Ad Budget", min_value=0.0, value=20.0)
    newspaper = st.number_input("📰 Newspaper Ad Budget", min_value=0.0, value=10.0)

    if st.button("🔍 Predict"):
        input_data = np.array([[tv, radio, newspaper]])
        prediction = model.predict(input_data)[0]
        st.success(f"🔮 Prediction: ${prediction:.2f} in sales 💵")