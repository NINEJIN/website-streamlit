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
                file_name="resume.pdf",
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
            <h1 style="margin: 0; color: #2C3E50;">Qinyuan Xiao</h1>
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
                    <a href="mailto:qinyuanxiao1115@gmail.com">qinyuanxiao1115@gmail.com</a>
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
                    <a href="https://www.linkedin.com/in/qinyuan-xiao-b550142b0/" target="_blank">linkedin.com/in/qinyuan-xiao-b550142b0/</a>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">💻</span>
                <div>
                    <strong>GitHub</strong><br>
                    <a href="https://github.com/NINEJIN" target="_blank">github.com/NINEJIN</a>
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
           Marketing graduate student at The Chinese University of Hong Kong with a solid foundation in business administration and international exposure through studies at UC Berkeley. 
           Experienced in marketing strategy, social media operations, and industry research through internships at leading firms such as CICC and Yuehai Group. 
           Strong analytical and communication skills, with a passion for combining data insights and creative thinking to drive brand growth and community engagement.
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
            "title": "Marketing Intern",
            "company": "Guangdong Yuehai Industrial Park Investment Holdings Co., Ltd.",
            "period": "March 2023 – May 2023",
            "responsibilities": [
                "📊 Conducted market research and competitor analysis to support strategic marketing plans",
                "📈 Assisted in brand development and improved internal marketing management systems",
                "📱 Managed official social media content and handled external communications",
                "📂 Analyzed member data to support customer engagement initiatives"
            ]
        },
        {
            "title": "Investment Banking Intern",
            "company": "China International Capital Corporation Limited (CICC)",
            "period": "July 2021 – August 2021",
            "responsibilities": [
                "📉 Conducted industry research in the online ride-hailing and energy technology sectors for IPO valuation",
                "📑 Drafted capital operation proposals and internal financial documents",
                "🔍 Evaluated investment opportunities and supported project due diligence",
                "🤝 Collaborated with team members across departments to prepare client presentations"
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
                <h3 class="card-title">Master of Science in Marketing</h3>
                <p class="card-subtitle">The Chinese University of Hong Kong (CUHK)</p>
                <p class="card-meta">August 2024 – July 2025</p>
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
    """, unsafe_allow_html=True)


    # Certifications
    st.markdown("""
    <div class="resume-section">
        <h2>🏅 Certifications</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
            <div class="project-card">
                <h4>🏅 Toefl</h4>
                <p style="color: #6C757D; margin: 0.5rem 0;">Score 103</p>
            </div>
            <div class="project-card">
                <h4>🏅 IELTS</h4>
                <p style="color: #6C757D; margin: 0.5rem 0;">Score 7.0</p>
            </div>
            <div class="project-card">
                <h4>🏅 GRE</h4>
                <p style="color: #6C757D; margin: 0.5rem 0;">Score 328</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Key Projects

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
                    <strong>Travel</strong><br>
                    <span style="color: #6C757D;">Travel</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📝</span>
                <div>
                    <strong>Skiing</strong><br>
                    <span style="color: #6C757D;">Skiing</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🏃</span>
                <div>
                    <strong>Fitness & Outdoor Activities</strong><br>
                    <span style="color: #6C757D;">Communication</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---") 