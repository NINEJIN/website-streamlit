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
                    <h3 class="card-title">🎓 Master of Science in Data Science</h3>
                    <p class="card-subtitle">University of XYZ</p>
                    <p class="card-meta">September 2020 - May 2022</p>
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
                    <p><strong>🏆 GPA:</strong> 3.7/4.0</p>
                    <p><strong>🥇 Achievement:</strong> Graduated with Honors</p>
                    <p><strong>📚 Relevant Coursework:</strong></p>
                    <ul style="margin: 1rem 0; padding-left: 2rem; line-height: 1.6;">
                        <li>Algorithms and Data Structures</li>
                        <li>Database Systems</li>
                        <li>Computer Networks</li>
                        <li>Operating Systems</li>
                        <li>Software Engineering</li>
                        <li>Web Development</li>
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
            <h3 style="text-align: center;">AWS Certified Data Analytics</h3>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0;"><strong>Amazon Web Services</strong></p>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0; font-style: italic;">March 2022</p>
            <p style="text-align: center; line-height: 1.6;">
                Demonstrated expertise in designing, building, securing, and maintaining analytics solutions on AWS platform.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with cert2:
        st.markdown("""
        <div class="project-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <h2 style="color: #4285F4; margin: 0;">🏅</h2>
            </div>
            <h3 style="text-align: center;">TensorFlow Developer Certificate</h3>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0;"><strong>Google</strong></p>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0; font-style: italic;">January 2022</p>
            <p style="text-align: center; line-height: 1.6;">
                Validated ability to develop deep learning models using TensorFlow framework for real-world applications.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with cert3:
        st.markdown("""
        <div class="project-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <h2 style="color: #0078D4; margin: 0;">🏅</h2>
            </div>
            <h3 style="text-align: center;">Azure Data Scientist Associate</h3>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0;"><strong>Microsoft</strong></p>
            <p style="text-align: center; color: #6C757D; margin: 0.5rem 0; font-style: italic;">November 2021</p>
            <p style="text-align: center; line-height: 1.6;">
                Demonstrated expertise in using Azure services to train, evaluate, and deploy machine learning models.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Academic Projects Section
    st.markdown("""
    <div class="experience-card">
        <h2>🔬 Academic Research Projects</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Significant research projects that contributed to my academic and professional development
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Project 1
    with st.expander("🧠 Sentiment Analysis of Product Reviews", expanded=True):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Project Overview:**
            - Developed a deep learning model to analyze customer reviews and predict sentiment
            - Achieved 92% accuracy using BERT and fine-tuning techniques
            - Implemented the model as a web application using Flask
            
            **Technologies Used:**
            """)
            
            skills = ["Python", "BERT", "TensorFlow", "Flask", "NLP", "Web Scraping"]
            skills_html = ""
            for skill in skills:
                skills_html += f'<span class="skill-tag">{skill}</span>'
            st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            **Key Results:**
            - 📊 92% Accuracy
            - 🔍 10,000+ Reviews Analyzed
            - 🚀 Real-time Prediction
            - 📱 Web Application Deployed
            """)

    # Project 2
    with st.expander("🏥 Image Classification for Medical Diagnosis"):
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            **Project Overview:**
            - Created a convolutional neural network to classify medical images
            - Worked with a dataset of X-ray images to detect pneumonia
            - Achieved 88% accuracy and deployed the model on a cloud platform
            
            **Technologies Used:**
            """)
            
            skills = ["Python", "CNN", "Keras", "OpenCV", "AWS", "Medical Imaging"]
            skills_html = ""
            for skill in skills:
                skills_html += f'<span class="skill-tag">{skill}</span>'
            st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)
            
        with col2:
            st.markdown("""
            **Key Results:**
            - 📊 88% Accuracy
            - 🏥 Medical Grade Performance
            - ☁️ Cloud Deployment
            - 🔬 Research Publication
            """)

    st.markdown("---") 