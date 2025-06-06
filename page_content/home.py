import streamlit as st
from PIL import Image
import os

def home_page():
    # Hero Section
    st.markdown("""
    <div class="fade-in-up">
        <h1>🌟 Sarah Johnson</h1>
        <p style="text-align: center; font-size: 1.4rem; color: #6C757D; margin-bottom: 3rem;">
            Data Scientist | Machine Learning Engineer | Innovation Driver
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Profile Section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        image_path = os.path.join("static", "images", "image.png")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.markdown('<div class="profile-container float">', unsafe_allow_html=True)
            st.image(image, width=250, use_column_width=False)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("📸 Profile image not found")
    
    # Contact Information Card
    st.markdown("""
    <div class="contact-info slide-in-right">
        <h3 style="text-align: center; margin-bottom: 2rem;">📞 Contact Information</h3>
        <div class="contact-item">
            <span class="contact-icon">🎓</span>
            <div>
                <strong>Education</strong><br>
                Master's in Marketing, Chinese University of Hong Kong
            </div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">📍</span>
            <div>
                <strong>Location</strong><br>
                12 Chak Cheung St., Ma Liu Shui, Hong Kong SAR
            </div>
        </div>
        <div class="contact-item">
            <span class="contact-icon">📧</span>
            <div>
                <strong>Email</strong><br>
                <a href="mailto:sarah.johnson@example.com" style="color: #3498DB;">sarah.johnson@example.com</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # About Me Section
    st.markdown("""
    <div class="experience-card fade-in-up">
        <h2>🚀 About Me</h2>
        <p style="font-size: 1.2rem; line-height: 1.8; color: #2C3E50;">
            I am a recent Master's graduate in Data Science from the University of XYZ, eager to apply my knowledge 
            and skills in a professional setting. During my academic journey, I developed a strong foundation in 
            statistical analysis, machine learning, and data visualization.
        </p>
        <p style="font-size: 1.2rem; line-height: 1.8; color: #2C3E50;">
            As part of my master's program, I completed several projects that involved working with real-world datasets 
            and applying various data science techniques. These projects allowed me to gain hands-on experience in data 
            preprocessing, exploratory data analysis, model building, and evaluation.
        </p>
        <p style="font-size: 1.2rem; line-height: 1.8; color: #2C3E50;">
            I am passionate about leveraging data to drive insights and make informed decisions. I am a quick learner, 
            a collaborative team player, and possess strong problem-solving skills. I am excited to contribute my skills 
            and grow as a data science professional in a dynamic and challenging environment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Statistics Section
    st.markdown("""
    <div class="fade-in-up">
        <h2 style="text-align: center; margin: 3rem 0 2rem 0;">📊 Professional Highlights</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">5+</p>
            <p class="stat-label">Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">3</p>
            <p class="stat-label">Internships</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">85%</p>
            <p class="stat-label">Model Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">10+</p>
            <p class="stat-label">Technical Skills</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Skills Section
    st.markdown("""
    <div class="experience-card">
        <h2>💻 Core Skills & Technologies</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Here are the key technologies and skills I've mastered during my journey in data science and software development.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Skill Categories
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>🔧 Programming & Tools</h3>
        </div>
        """, unsafe_allow_html=True)
        
        programming_skills = [
            "Python", "R", "SQL", "JavaScript", "Git", "Docker"
        ]
        
        skills_html = ""
        for skill in programming_skills:
            skills_html += f'<span class="skill-tag">{skill}</span>'
        
        st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>🤖 Machine Learning & AI</h3>
        </div>
        """, unsafe_allow_html=True)
        
        ml_skills = [
            "Scikit-learn", "TensorFlow", "PyTorch", "Deep Learning", "NLP"
        ]
        
        skills_html = ""
        for skill in ml_skills:
            skills_html += f'<span class="skill-tag">{skill}</span>'
        
        st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>📊 Data & Analytics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        data_skills = [
            "Pandas", "NumPy", "Matplotlib", "Seaborn", "Tableau", "Power BI"
        ]
        
        skills_html = ""
        for skill in data_skills:
            skills_html += f'<span class="skill-tag">{skill}</span>'
        
        st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="project-card">
            <h3>☁️ Cloud & Infrastructure</h3>
        </div>
        """, unsafe_allow_html=True)
        
        cloud_skills = [
            "AWS", "Azure", "Google Cloud", "Streamlit", "Flask"
        ]
        
        skills_html = ""
        for skill in cloud_skills:
            skills_html += f'<span class="skill-tag">{skill}</span>'
        
        st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)

    st.markdown("---") 