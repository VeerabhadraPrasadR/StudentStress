import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import datetime

# Load the trained model and mappings
@st.cache_resource
def load_model():
    try:
        model = joblib.load('stress_prediction_models.pkl')
        st.success('Model loaded successfully!')
        return model
    except Exception as e:
        st.error(f'Could not load model: {e}')
        return None

def get_psychological_risks_and_actions(stress_level):
    """Get psychological risks and recommended actions based on stress level"""
    
    guidance = {
        'Fabulous': {
            'status': '🌟 Excellent Mental Health!',
            'risks': [
                '✅ Minimal psychological risk',
                '✅ Strong emotional resilience',
                '✅ Healthy coping mechanisms in place',
                '✅ Good work-life balance'
            ],
            'actions': [
                '🧘 Continue current stress management practices',
                '🏃 Maintain regular physical activity',
                '😴 Keep healthy sleep schedule (7-9 hours)',
                '🤝 Nurture social connections',
                '📚 Consider mentoring others with stress management'
            ]
        },
        'Good': {
            'status': '😊 Good Mental Health with Minor Concerns',
            'risks': [
                '⚠️ Mild anxiety during exams',
                '⚠️ Occasional sleep disruption',
                '⚠️ Risk of perfectionism creating pressure',
                '⚠️ Tendency to compare with peers'
            ],
            'actions': [
                '🧘 Practice 15 minutes daily meditation',
                '📝 Start a stress journal',
                '🏃 Exercise 30 minutes daily',
                '😴 Establish consistent sleep routine',
                '📱 Limit social media before bed',
                '💬 Talk to counselor if overwhelmed'
            ]
        },
        'Bad': {
            'status': '😰 Elevated Stress - Action Needed',
            'risks': [
                '🚨 Risk of anxiety disorders',
                '🚨 Potential depression symptoms',
                '🚨 Academic burnout possible',
                '🚨 Physical health issues (headaches, fatigue)',
                '🚨 Social withdrawal tendencies',
                '🚨 Concentration and memory problems'
            ],
            'actions': [
                '🏥 **SEEK PROFESSIONAL COUNSELING** - Don\'t wait',
                '😴 **Prioritize sleep** - 7-9 hours mandatory',
                '🧘 **Daily stress relief** - Meditation/yoga required',
                '🏃 **Physical activity** - 20+ minutes daily',
                '🤝 **Reach out** - Talk to friends, family, counselors',
                '📵 **Digital detox** - Reduce screen time',
                '📚 **Academic support** - Tutoring, study groups',
                '🏥 **Campus counseling center** - Free services available'
            ]
        },
        'Awful': {
            'status': '🚨 CRITICAL - Immediate Help Required',
            'risks': [
                '🚨 SEVERE: Major depression risk',
                '🚨 SEVERE: Anxiety and panic disorders',
                '🚨 SEVERE: Suicidal ideation possible',
                '🚨 SEVERE: Complete academic failure',
                '🚨 SEVERE: Physical health crisis',
                '🚨 SEVERE: Social isolation',
                '🚨 SEVERE: Substance abuse risk'
            ],
            'actions': [
                '🆘 **EMERGENCY: Call crisis hotline immediately**',
                '📞 **India - AASRA**: 9820466726 (24/7)',
                '📞 **India - Vandrevala**: 9999666555',
                '📞 **India - Sneha**: 044-24640050',
                '🏥 **Visit Emergency Room** if having suicidal thoughts',
                '🤝 **Don\'t be alone** - Stay with trusted person',
                '💊 **Avoid alcohol/drugs**',
                '👨‍⚕️ **See psychiatrist** for medication evaluation',
                '🧠 **Intensive therapy** required immediately',
                '🏥 **Campus health services** - Seek help today'
            ]
        }
    }
    
    return guidance.get(stress_level, guidance['Good'])

def predict_stress_level(mark10th, mark12th, collegemark, carrer_willing, smtime, financial):
    """Simple rule-based prediction"""
    
    academic_avg = (mark10th + mark12th + collegemark) / 3
    risk_score = 0
    
    # Academic factors
    if academic_avg < 50:
        risk_score += 3
    elif academic_avg < 70:
        risk_score += 1
    
    # Career factors
    if carrer_willing < 30:
        risk_score += 2
    elif carrer_willing < 60:
        risk_score += 1
    
    # Social media
    if smtime > 8:
        risk_score += 2
    elif smtime > 5:
        risk_score += 1
    
    # Financial
    if financial == 'Awful':
        risk_score += 2
    elif financial == 'Bad':
        risk_score += 1
    
    # Map to stress level
    if risk_score >= 6:
        return 'Awful', [0.1, 0.1, 0.2, 0.6]
    elif risk_score >= 4:
        return 'Bad', [0.1, 0.2, 0.6, 0.1]
    elif risk_score >= 2:
        return 'Good', [0.2, 0.6, 0.1, 0.1]
    else:
        return 'Fabulous', [0.6, 0.3, 0.1, 0.0]

# App title
st.title('Student Stress Level Predictor')
st.markdown('### AI-Powered Mental Health Assessment')

# Load model
model_data = load_model()

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader('Academic Information')
    mark10th = st.slider('10th Grade Marks (%)', 30, 100, 75)
    mark12th = st.slider('12th Grade Marks (%)', 30, 100, 75)
    collegemark = st.slider('College Marks (%)', 30, 100, 75)
    
    st.subheader('Personal Information')
    gender = st.selectbox('Gender', ['Male', 'Female'])
    height = st.slider('Height (cm)', 140, 200, 170)
    weight = st.slider('Weight (kg)', 30, 120, 65)

with col2:
    st.subheader('Lifestyle & Career')
    studytime = st.slider('Study Time (hours/day)', 0, 12, 6)
    smtime = st.slider('Social Media Time (hours/day)', 0, 24, 3)
    travel = st.slider('Travel Time (minutes)', 0, 180, 30)
    
    st.subheader('Expectations & Status')
    salexpect = st.number_input('Salary Expectation (₹)', 10000, 2000000, 50000)
    carrer_willing = st.slider('Career Willingness (%)', 0, 100, 50)
    financial = st.selectbox('Financial Status', ['Awful', 'Bad', 'Good', 'Fabulous'])

# Predict button
if st.button('Predict Stress Level', type='primary'):
    # Make prediction
    predicted_level, probabilities = predict_stress_level(
        mark10th, mark12th, collegemark, carrer_willing, smtime, financial
    )
    
    # Display results
    st.success('✅ Prediction Completed!')
    
    # Show metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric('🎯 Predicted Stress Level', predicted_level)
    with col2:
        confidence = max(probabilities) * 100
        st.metric('🎚️ Confidence', f'{confidence:.1f}%')
    
    # Show profile summary
    academic_avg = (mark10th + mark12th + collegemark) / 3
    st.info(f'📊 **Profile**: Academic: {academic_avg:.1f}% | Career: {carrer_willing}% | Social Media: {smtime}h/day | Financial: {financial}')
    
    # Show probability chart
    st.subheader('📊 Stress Level Probabilities')
    prob_df = pd.DataFrame({
        'Stress Level': ['Fabulous', 'Good', 'Bad', 'Awful'],
        'Probability': probabilities
    })
    st.bar_chart(prob_df.set_index('Stress Level'))
    
    # Get and display guidance
    guidance = get_psychological_risks_and_actions(predicted_level)
    
    # Display status with appropriate color
    if predicted_level == 'Fabulous':
        st.success(guidance['status'])
    elif predicted_level == 'Good':
        st.info(guidance['status'])
    elif predicted_level == 'Bad':
        st.warning(guidance['status'])
    else:
        st.error(guidance['status'])
    
    # Display risks and actions
    st.markdown('---')
    st.header('🎯 Psychological Assessment & Recommendations')
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('⚠️ Identified Risks')
        for risk in guidance['risks']:
            st.markdown(f'• {risk}')
    
    with col2:
        st.subheader('💡 Recommended Actions')
        for action in guidance['actions']:
            st.markdown(f'• {action}')
    
    # Crisis disclaimer for critical cases
    if predicted_level == 'Awful':
        st.markdown('---')
        st.error('🚨 **CRISIS DISCLAIMER**: This is an automated assessment. If you are having thoughts of self-harm or suicide, please seek immediate professional help or call emergency services. Your life matters and help is available 24/7.')

st.markdown('---')
st.caption('Stress Level Prediction App v1.0')
