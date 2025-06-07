import streamlit as st
from PIL import Image
import os

def home_page():
    # Hero Section
    st.markdown("""
    <div class="fade-in-up">
        <h1>🌟 Qinyuan Xiao</h1>
        <p style="text-align: center; font-size: 1.4rem; color: #6C757D; margin-bottom: 3rem;">
            Master in Marketing
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Profile Section
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        image_path = os.path.join("static", "images", "iamge.png")
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
                <a href="mailto:qinyuanxiao1115@gmail.com" style="color: #3498DB;">qinyuanxiao1115@gmail.com</a>
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
            I am a recent Marketing graduate from The Chinese University of Hong Kong (CUHK), eager to apply the knowledge and skills I have acquired in a dynamic business environment. 
            Throughout my academic journey, I developed a solid foundation in consumer behavior, brand management, 
            digital marketing, and data-driven decision-making.
        </p>
        <p style="font-size: 1.2rem; line-height: 1.8; color: #2C3E50;">
            During my studies, I worked on several projects that involved market research, campaign planning, and the use of analytics tools to evaluate marketing performance. 
            These hands-on experiences strengthened my ability to translate insights into actionable strategies and sharpened my communication and teamwork skills.
        </p>
        <p style="font-size: 1.2rem; line-height: 1.8; color: #2C3E50;">
            I am passionate about understanding customer needs and creating impactful marketing solutions. 
            I am a fast learner, a collaborative team player, and enjoy solving complex problems. 
            I look forward to contributing to meaningful marketing initiatives and growing as a professional in the industry.
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
            <p class="stat-number">1</p>
            <p class="stat-label">Projects Completed</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">2</p>
            <p class="stat-label">Internships</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">3</p>
            <p class="stat-label">Language</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <p class="stat-number">5</p>
            <p class="stat-label">Technical Skills</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Skills Section
    st.markdown("""
    <div class="experience-card">
        <h2>💻 Core Skills & Technologies</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Skilled in market research, digital marketing, and data-driven strategy development, 
            with hands-on experience in campaign planning and performance analysis. 
            Strong communicator and team player with a keen eye for consumer insights and brand positioning.
        </p>
    </div>
    """, unsafe_allow_html=True)
    

    st.markdown("---") 