import streamlit as st

def education_page():
    st.markdown("""
    <div class="fade-in-up">
        <h1>🎓 Education</h1>
        <p style="text-align: center; font-size: 1.2rem; color: #6C757D; margin-bottom: 3rem;">
            My Academic Journey & Continuous Learning Path
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Education Timeline
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item">
            <div class="education-card">
                <div class="card-header">
                    <h3 class="card-title">🎓 Master of Science in Marketing</h3>
                    <p class="card-subtitle">The Chinese University of Hong Kong (CUHK)</p>
                    <p class="card-meta">August 2024 – July 2025</p>
                </div>
                <div class="card-content">
                    <p><strong>🏆 GPA:</strong> 3.9/4.0</p>
                    <p><strong>📝 Thesis:</strong> "Applying Machine Learning Techniques to Predict Customer Behavior in E-commerce"</p>
                    <p><strong>📚 Relevant Coursework:</strong></p>
                    <ul style="margin: 1rem 0; padding-left: 2rem; line-height: 1.6;">
                        <li>Advanced Machine Learning</li>
                        <li>Deep Learning & Neural Networks</li>
                        <li>Natural Language Processing</li>
                        <li>Data Visualization & Storytelling</li>
                        <li>Statistical Methods for Data Science</li>
                        <li>Big Data Analytics</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="education-card">
                <div class="card-header">
                    <h3 class="card-title">🎓 Bachelor of Science in Computer Science</h3>
                    <p class="card-subtitle">ABC University</p>
                    <p class="card-meta">September 2016 - May 2020</p>
                </div>
                <div class="card-content">
                    <p><strong>📍 Hong Kong</p>
                    <p><strong>🏆 GPA: – (currently pursuing)</p>
                    <p><strong>📚 Relevant Coursework:</strong></p>
                    <ul style="margin: 1rem 0; padding-left: 2rem; line-height: 1.6;">
                        <li>Consumer Behavior</li>
                        <li>Digital & Social Media Marketing</li>
                        <li>Brand Management</li>
                        <li>Marketing Analytics</li>
                        <li>Strategic Marketing</li>
                        <li>Data-Driven Decision Making</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Certifications Section
    st.markdown("""
    <div class="fade-in-up">
        <h2>🏅 Professional Certifications</h2>
        <p style="text-align: center; font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Industry-recognized certifications that validate my expertise
        </p>
    </div>
    """, unsafe_allow_html=True)

    cert1, cert2, cert3 = st.columns(3)

    with cert1:
        st.markdown("""
        <div class="project-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <h2 style="color: #FF9500; margin: 0;">🏅</h2>
            </div>
            <h3 style="text-align: center;">Toefl</h3>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0;"><strong>Score 103</strong></p>
            
        </div>
        """, unsafe_allow_html=True)

    with cert2:
        st.markdown("""
        <div class="project-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <h2 style="color: #4285F4; margin: 0;">🏅</h2>
            </div>
            <h3 style="text-align: center;">IELTS</h3>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0;"><strong>Score 7.0</strong></p>
            
        </div>
        """, unsafe_allow_html=True)

    with cert3:
        st.markdown("""
        <div class="project-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <h2 style="color: #0078D4; margin: 0;">🏅</h2>
            </div>
            <h3 style="text-align: center;">GRE</h3>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0;"><strong>Score 328</strong></p>
           
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")


    st.markdown("---") 