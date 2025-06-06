import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("""
    <div class="fade-in-up">
        <h1>💼 Professional Experience</h1>
        <p style="text-align: center; font-size: 1.2rem; color: #6C757D; margin-bottom: 3rem;">
            My Professional Journey & Career Highlights
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Experience Timeline
    st.markdown("""
    <div class="timeline">
        <div class="timeline-item">
            <div class="experience-card">
                <div class="card-header">
                    <h3 class="card-title">🚀 Data Science Intern</h3>
                    <p class="card-subtitle">TechCorp Inc.</p>
                    <p class="card-meta">June 2021 - August 2021</p>
                </div>
                <div class="card-content">
                    <ul style="line-height: 1.8; padding-left: 1.5rem;">
                        <li>📊 Analyzed customer data to identify patterns and trends using Python and SQL</li>
                        <li>🤖 Developed a machine learning model to predict customer churn with 85% accuracy</li>
                        <li>📈 Created interactive dashboards using Tableau to visualize key performance indicators</li>
                        <li>🎯 Presented findings and recommendations to senior management</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="experience-card">
                <div class="card-header">
                    <h3 class="card-title">🔬 Research Assistant</h3>
                    <p class="card-subtitle">University of XYZ, Department of Computer Science</p>
                    <p class="card-meta">January 2021 - May 2021</p>
                </div>
                <div class="card-content">
                    <ul style="line-height: 1.8; padding-left: 1.5rem;">
                        <li>🧠 Assisted professor with research on natural language processing techniques</li>
                        <li>⚡ Implemented and evaluated various machine learning algorithms for text classification</li>
                        <li>📝 Co-authored a paper that was accepted at a regional computer science conference</li>
                        <li>👥 Mentored undergraduate students on research methodologies and programming</li>
                    </ul>
                </div>
            </div>
        </div>
        
        <div class="timeline-item">
            <div class="experience-card">
                <div class="card-header">
                    <h3 class="card-title">💻 Software Development Intern</h3>
                    <p class="card-subtitle">InnovateTech Solutions</p>
                    <p class="card-meta">May 2020 - August 2020</p>
                </div>
                <div class="card-content">
                    <ul style="line-height: 1.8; padding-left: 1.5rem;">
                        <li>🌐 Developed and maintained web applications using Django and React</li>
                        <li>🤝 Collaborated with a team of developers using Agile methodologies</li>
                        <li>⚙️ Implemented new features based on user feedback and requirements</li>
                        <li>🔍 Participated in code reviews and testing procedures</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Projects Section
    st.markdown("""
    <div class="experience-card">
        <h2>🎯 Featured Projects</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Highlight projects that demonstrate my technical skills and problem-solving abilities
        </p>
    </div>
    """, unsafe_allow_html=True)

    projects = [
        {
            "title": "🔍 Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns.",
            "impact": "📈 Increased conversion rate by 23%"
        },
        {
            "title": "⚙️ Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%.",
            "impact": "💰 Saved $50K annually"
        },
        {
            "title": "🤖 NLP for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores.",
            "impact": "⚡ 35% faster response time"
        }
    ]

    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**🎯 Description:** {project['description']}")
                st.markdown(f"**📊 Outcome:** {project['outcome']}")
                
                st.markdown("**🛠️ Technologies Used:**")
                skills_html = ""
                for skill in project['skills']:
                    skills_html += f'<span class="skill-tag">{skill}</span>'
                st.markdown(f'<div style="margin: 1rem 0;">{skills_html}</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="stat-card" style="margin: 0;">
                    <h4 style="color: #27AE60; margin: 0;">Impact</h4>
                    <p style="font-size: 1.1rem; margin: 0.5rem 0; font-weight: 600;">
                        {project['impact']}
                    </p>
                </div>
                """, unsafe_allow_html=True)

    # Interactive Demo
    with st.expander("📊 Interactive Data Visualization Demo", expanded=False):
        st.markdown("""
        <div class="project-card">
            <h4>🎮 Live Demo</h4>
            <p><strong>Description:</strong> An interactive demonstration of various data visualization techniques 
            showcasing my skills in creating dynamic, user-friendly data presentations.</p>
        </div>
        """, unsafe_allow_html=True)
        display_interactive_chart()

    st.markdown("---")

    # Skills Section
    st.markdown("""
    <div class="experience-card">
        <h2>🛠️ Professional Skills Matrix</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Comprehensive overview of my technical and soft skills developed through professional experience
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>💻 Technical Expertise</h3>
            <div style="margin: 1.5rem 0;">
                <p><strong>Programming Languages:</strong></p>
                <p style="margin: 0.5rem 0; color: #6C757D;">Python, R, SQL, JavaScript</p>
                
                <p><strong>Machine Learning:</strong></p>
                <p style="margin: 0.5rem 0; color: #6C757D;">scikit-learn, TensorFlow, PyTorch</p>
                
                <p><strong>Data Processing:</strong></p>
                <p style="margin: 0.5rem 0; color: #6C757D;">Pandas, NumPy, PySpark</p>
                
                <p><strong>Visualization:</strong></p>
                <p style="margin: 0.5rem 0; color: #6C757D;">Matplotlib, Seaborn, Tableau, PowerBI</p>
                
                <p><strong>Cloud Platforms:</strong></p>
                <p style="margin: 0.5rem 0; color: #6C757D;">AWS, Azure, Google Cloud</p>
                
                <p><strong>Web Development:</strong></p>
                <p style="margin: 0.5rem 0; color: #6C757D;">Django, Flask, React</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>🎯 Soft Skills</h3>
            <div style="margin: 1.5rem 0;">
                <div class="contact-item">
                    <span class="contact-icon">💬</span>
                    <div>
                        <strong>Communication</strong><br>
                        <span style="color: #6C757D;">Excellent written and verbal communication</span>
                    </div>
                </div>
                
                <div class="contact-item">
                    <span class="contact-icon">🤝</span>
                    <div>
                        <strong>Teamwork</strong><br>
                        <span style="color: #6C757D;">Collaborative team player with Agile experience</span>
                    </div>
                </div>
                
                <div class="contact-item">
                    <span class="contact-icon">🧩</span>
                    <div>
                        <strong>Problem-solving</strong><br>
                        <span style="color: #6C757D;">Strong analytical and critical thinking abilities</span>
                    </div>
                </div>
                
                <div class="contact-item">
                    <span class="contact-icon">⏰</span>
                    <div>
                        <strong>Time Management</strong><br>
                        <span style="color: #6C757D;">Efficient at prioritizing tasks and meeting deadlines</span>
                    </div>
                </div>
                
                <div class="contact-item">
                    <span class="contact-icon">👑</span>
                    <div>
                        <strong>Leadership</strong><br>
                        <span style="color: #6C757D;">Experience leading teams and mentoring colleagues</span>
                    </div>
                </div>
                
                <div class="contact-item">
                    <span class="contact-icon">🔄</span>
                    <div>
                        <strong>Adaptability</strong><br>
                        <span style="color: #6C757D;">Quick learner who thrives in dynamic environments</span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---") 