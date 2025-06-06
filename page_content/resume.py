import streamlit as st
import base64
import os

def resume_page():
    st.markdown("""
    <div class="fade-in-up">
        <h1>📄 Resume</h1>
        <p style="text-align: center; font-size: 1.2rem; color: #6C757D; margin-bottom: 3rem;">
            Professional Profile & Career Summary
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Download Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pdf_file_path = os.path.join("static", "docs", "resume.pdf")
        if os.path.exists(pdf_file_path):
            with open(pdf_file_path, "rb") as pdf_file:
                PDFbyte = pdf_file.read()
            
            st.markdown("""
            <div class="resume-section" style="text-align: center; margin-bottom: 2rem;">
                <h3>📥 Download Resume</h3>
                <p style="color: #6C757D; margin-bottom: 1.5rem;">
                    Get a PDF copy of my complete resume
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            st.download_button(
                label="📥 Download Resume PDF",
                data=PDFbyte,
                file_name="Sarah_Johnson_Resume.pdf",
                mime='application/octet-stream',
                use_container_width=True
            )
        else:
            st.warning("📋 Resume PDF file not found")

    st.markdown("---")

    # Header Section
    st.markdown("""
    <div class="resume-section">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="margin: 0; color: #2C3E50;">Sarah Johnson</h1>
            <p style="font-size: 1.3rem; color: #3498DB; margin: 0.5rem 0;">Data Scientist & Machine Learning Engineer</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Contact Information
    st.markdown("""
    <div class="contact-info">
        <h2>📞 Contact Information</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div class="contact-item">
                <span class="contact-icon">📧</span>
                <div>
                    <strong>Email</strong><br>
                    <a href="mailto:sarah.johnson@example.com">sarah.johnson@example.com</a>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📱</span>
                <div>
                    <strong>Phone</strong><br>
                    (123) 456-7890
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">💼</span>
                <div>
                    <strong>LinkedIn</strong><br>
                    <a href="https://linkedin.com/in/sarahjohnson" target="_blank">linkedin.com/in/sarahjohnson</a>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">💻</span>
                <div>
                    <strong>GitHub</strong><br>
                    <a href="https://github.com/sarahjohnson" target="_blank">github.com/sarahjohnson</a>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📍</span>
                <div>
                    <strong>Location</strong><br>
                    Hong Kong SAR
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Professional Summary
    st.markdown("""
    <div class="resume-section">
        <h2>🎯 Professional Summary</h2>
        <p style="font-size: 1.1rem; line-height: 1.8; color: #2C3E50;">
            Highly skilled data scientist with over 3 years of experience in developing scalable machine learning solutions. 
            Proven ability to analyze complex datasets, build predictive models, and translate business requirements into 
            technical solutions. Seeking a challenging role to utilize my expertise in data science, machine learning, 
            and statistical analysis to drive business insights and innovation.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Work Experience
    st.markdown("""
    <div class="resume-section">
        <h2>💼 Work Experience</h2>
    </div>
    """, unsafe_allow_html=True)

    # Experience Timeline
    experiences = [
        {
            "title": "Data Science Intern",
            "company": "TechCorp Inc.",
            "period": "June 2021 – August 2021",
            "responsibilities": [
                "Developed and maintained machine learning models using Python and TensorFlow",
                "Improved model performance by 30% through feature engineering and hyperparameter tuning",
                "Led data analysis projects, conducting statistical analysis and presenting insights to stakeholders",
                "Collaborated with cross-functional teams to define project requirements and deliverables"
            ]
        },
        {
            "title": "Research Assistant",
            "company": "University of XYZ, Department of Computer Science",
            "period": "January 2021 – May 2021",
            "responsibilities": [
                "Assisted in natural language processing research projects and algorithm development",
                "Participated in agile research sprints and contributed to project planning and task estimation",
                "Implemented machine learning algorithms and conducted model evaluation and validation",
                "Co-authored research papers and presented findings at academic conferences"
            ]
        }
    ]

    for exp in experiences:
        st.markdown(f"""
        <div class="experience-card">
            <div class="card-header">
                <h3 class="card-title">{exp['title']}</h3>
                <p class="card-subtitle">{exp['company']}</p>
                <p class="card-meta">{exp['period']}</p>
            </div>
            <div class="card-content">
                <ul style="line-height: 1.8; padding-left: 1.5rem; margin: 1rem 0;">
        """, unsafe_allow_html=True)
        
        for responsibility in exp['responsibilities']:
            st.markdown(f"<li>{responsibility}</li>", unsafe_allow_html=True)
        
        st.markdown("</ul></div></div>", unsafe_allow_html=True)

    # Education
    st.markdown("""
    <div class="resume-section">
        <h2>🎓 Education</h2>
        <div class="education-card">
            <div class="card-header">
                <h3 class="card-title">Master of Science in Data Science</h3>
                <p class="card-subtitle">University of XYZ</p>
                <p class="card-meta">Graduated: May 2022</p>
            </div>
            <div class="card-content">
                <p><strong>GPA:</strong> 3.9/4.0</p>
                <p><strong>Thesis:</strong> "Applying Machine Learning Techniques to Predict Customer Behavior in E-commerce"</p>
            </div>
        </div>
        
        <div class="education-card">
            <div class="card-header">
                <h3 class="card-title">Bachelor of Science in Computer Science</h3>
                <p class="card-subtitle">ABC University</p>
                <p class="card-meta">Graduated: May 2020</p>
            </div>
            <div class="card-content">
                <p><strong>GPA:</strong> 3.7/4.0</p>
                <p><strong>Achievement:</strong> Graduated with Honors</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Skills
    st.markdown("""
    <div class="resume-section">
        <h2>🛠️ Technical Skills</h2>
    </div>
    """, unsafe_allow_html=True)

    skill_categories = [
        {
            "category": "Programming Languages",
            "skills": ["Python", "R", "SQL", "JavaScript", "Java"]
        },
        {
            "category": "Machine Learning & AI",
            "skills": ["scikit-learn", "TensorFlow", "PyTorch", "Keras", "XGBoost"]
        },
        {
            "category": "Data Processing & Analysis",
            "skills": ["Pandas", "NumPy", "PySpark", "Dask", "Apache Airflow"]
        },
        {
            "category": "Visualization & BI",
            "skills": ["Matplotlib", "Seaborn", "Plotly", "Tableau", "Power BI"]
        },
        {
            "category": "Cloud & Infrastructure",
            "skills": ["AWS", "Azure", "Google Cloud", "Docker", "Kubernetes"]
        },
        {
            "category": "Web Technologies",
            "skills": ["Django", "Flask", "React", "Node.js", "Streamlit"]
        }
    ]

    col1, col2 = st.columns(2)
    
    for i, skill_cat in enumerate(skill_categories):
        col = col1 if i % 2 == 0 else col2
        
        with col:
            st.markdown(f"""
            <div class="project-card">
                <h4>{skill_cat['category']}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            skills_html = ""
            for skill in skill_cat['skills']:
                skills_html += f'<span class="skill-tag">{skill}</span>'
            
            st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)

    # Certifications
    st.markdown("""
    <div class="resume-section">
        <h2>🏅 Certifications</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
            <div class="project-card">
                <h4>🏅 AWS Certified Data Analytics - Specialty</h4>
                <p style="color: #6C757D; margin: 0.5rem 0;">Amazon Web Services • March 2022</p>
            </div>
            <div class="project-card">
                <h4>🏅 TensorFlow Developer Certificate</h4>
                <p style="color: #6C757D; margin: 0.5rem 0;">Google • January 2022</p>
            </div>
            <div class="project-card">
                <h4>🏅 Azure Data Scientist Associate</h4>
                <p style="color: #6C757D; margin: 0.5rem 0;">Microsoft • November 2021</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Projects
    st.markdown("""
    <div class="resume-section">
        <h2>🎯 Key Projects</h2>
        
        <div class="project-card">
            <h4>🔍 Customer Segmentation Analysis</h4>
            <p>Developed a comprehensive customer segmentation solution using K-means clustering and RFM analysis, 
            resulting in 23% increase in targeted marketing campaign effectiveness.</p>
            <p><strong>Technologies:</strong> Python, scikit-learn, Pandas, Matplotlib, Tableau</p>
        </div>
        
        <div class="project-card">
            <h4>🤖 Predictive Maintenance System</h4>
            <p>Built an IoT-based predictive maintenance system using time series analysis and deep learning, 
            reducing equipment downtime by 23% and maintenance costs by 15%.</p>
            <p><strong>Technologies:</strong> Python, TensorFlow, Time Series Analysis, IoT, AWS</p>
        </div>
        
        <div class="project-card">
            <h4>🧠 NLP Customer Support Automation</h4>
            <p>Created an intelligent text classification system for automatic customer support ticket categorization, 
            improving response time by 35% and customer satisfaction scores.</p>
            <p><strong>Technologies:</strong> Python, NLTK, spaCy, BERT, Flask</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Additional Information
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="resume-section">
            <h2>🌍 Languages</h2>
            <div class="contact-item">
                <span class="contact-icon">🇺🇸</span>
                <div>
                    <strong>English</strong><br>
                    <span style="color: #6C757D;">Native Proficiency</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🇨🇳</span>
                <div>
                    <strong>Mandarin</strong><br>
                    <span style="color: #6C757D;">Professional Working Proficiency</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="resume-section">
            <h2>🎯 Interests</h2>
            <div class="contact-item">
                <span class="contact-icon">💻</span>
                <div>
                    <strong>Open Source Contributions</strong><br>
                    <span style="color: #6C757D;">Active contributor to ML libraries</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📝</span>
                <div>
                    <strong>Technical Writing</strong><br>
                    <span style="color: #6C757D;">Blogging about AI/ML trends</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🏃</span>
                <div>
                    <strong>Fitness & Outdoor Activities</strong><br>
                    <span style="color: #6C757D;">Running, hiking, photography</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---") 