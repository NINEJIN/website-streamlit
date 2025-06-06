import streamlit as st

def contact_page():
    st.markdown("""
    <div class="fade-in-up">
        <h1>📞 Contact Me</h1>
        <p style="text-align: center; font-size: 1.2rem; color: #6C757D; margin-bottom: 3rem;">
            Let's Connect & Collaborate
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact Methods
    st.markdown("""
    <div class="contact-info">
        <h2>🌐 Get in Touch</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            I'm always excited to discuss new opportunities, collaborations, or just chat about data science and technology. 
            Feel free to reach out through any of the following channels:
        </p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
            <div class="contact-item">
                <span class="contact-icon">📧</span>
                <div>
                    <strong>Email</strong><br>
                    <a href="mailto:sarah.johnson@example.com" style="color: #3498DB;">sarah.johnson@example.com</a><br>
                    <span style="color: #6C757D; font-size: 0.9rem;">Best for professional inquiries</span>
                </div>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">📱</span>
                <div>
                    <strong>Phone</strong><br>
                    <a href="tel:+11234567890" style="color: #3498DB;">+1 (123) 456-7890</a><br>
                    <span style="color: #6C757D; font-size: 0.9rem;">Available Mon-Fri, 9 AM - 5 PM ET</span>
                </div>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">💼</span>
                <div>
                    <strong>LinkedIn</strong><br>
                    <a href="https://linkedin.com/in/sarahjohnson" target="_blank" style="color: #3498DB;">linkedin.com/in/sarahjohnson</a><br>
                    <span style="color: #6C757D; font-size: 0.9rem;">Professional networking & updates</span>
                </div>
            </div>
            
            <div class="contact-item">
                <span class="contact-icon">💻</span>
                <div>
                    <strong>GitHub</strong><br>
                    <a href="https://github.com/sarahjohnson" target="_blank" style="color: #3498DB;">github.com/sarahjohnson</a><br>
                    <span style="color: #6C757D; font-size: 0.9rem;">Code repositories & projects</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Contact Form
    st.markdown("""
    <div class="experience-card">
        <h2>💌 Send Me a Message</h2>
        <p style="font-size: 1.1rem; color: #6C757D; margin-bottom: 2rem;">
            Have a question or want to discuss a potential collaboration? Fill out the form below and I'll get back to you as soon as possible.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        # Form Header
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3498DB, #2C3E50); color: white; padding: 1rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="margin: 0; color: white;">📝 Contact Form</h3>
            <p style="margin: 0.5rem 0 0 0; color: #BDC3C7;">All fields are required</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("👤 Full Name", placeholder="Enter your full name")
            email = st.text_input("📧 Email Address", placeholder="your.email@example.com")
            
        with col2:
            subject = st.text_input("📋 Subject", placeholder="What's this about?")
            phone = st.text_input("📱 Phone Number (Optional)", placeholder="+1 (123) 456-7890")
        
        # Message Type
        message_type = st.selectbox(
            "📂 Message Type",
            ["General Inquiry", "Job Opportunity", "Collaboration", "Technical Question", "Other"]
        )
        
        # Message
        message = st.text_area(
            "💬 Message", 
            height=150,
            placeholder="Please provide details about your inquiry, project, or question. The more information you provide, the better I can assist you."
        )
        
        # Urgency Level
        urgency = st.radio(
            "⚡ Urgency Level",
            ["Low (1-2 weeks)", "Medium (3-5 days)", "High (24-48 hours)", "Urgent (same day)"],
            horizontal=True
        )
        
        # Submit Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            submitted = st.form_submit_button(
                "🚀 Send Message",
                use_container_width=True
            )
        
        if submitted:
            if name and email and subject and message:
                # Success Message
                st.markdown("""
                <div style="background: linear-gradient(135deg, #27AE60, #2ECC71); color: white; padding: 2rem; border-radius: 15px; text-align: center; margin: 2rem 0;">
                    <h3 style="margin: 0; color: white;">✅ Message Sent Successfully!</h3>
                    <p style="margin: 1rem 0 0 0; color: #D5DBDB; font-size: 1.1rem;">
                        Thank you for reaching out! I'll review your message and get back to you within the timeframe you specified.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                # Display summary
                st.markdown(f"""
                <div class="project-card">
                    <h4>📋 Message Summary</h4>
                    <p><strong>From:</strong> {name} ({email})</p>
                    <p><strong>Subject:</strong> {subject}</p>
                    <p><strong>Type:</strong> {message_type}</p>
                    <p><strong>Urgency:</strong> {urgency}</p>
                    <p><strong>Message Preview:</strong> {message[:100]}...</p>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.error("⚠️ Please fill in all required fields (Name, Email, Subject, and Message)")

    st.markdown("---")

    # Office Hours & Availability
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="project-card">
            <h3>🕒 Availability & Response Times</h3>
            <div class="contact-item">
                <span class="contact-icon">⏰</span>
                <div>
                    <strong>Office Hours</strong><br>
                    <span style="color: #6C757D;">Monday - Friday: 9 AM - 5 PM (ET)</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📧</span>
                <div>
                    <strong>Email Response</strong><br>
                    <span style="color: #6C757D;">Within 24-48 hours</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📱</span>
                <div>
                    <strong>Phone Calls</strong><br>
                    <span style="color: #6C757D;">By appointment only</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">💼</span>
                <div>
                    <strong>Virtual Meetings</strong><br>
                    <span style="color: #6C757D;">Zoom, Google Meet, or Teams</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="project-card">
            <h3>💡 What I'm Looking For</h3>
            <div class="contact-item">
                <span class="contact-icon">🚀</span>
                <div>
                    <strong>Career Opportunities</strong><br>
                    <span style="color: #6C757D;">Data Science, ML Engineer, AI roles</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🤝</span>
                <div>
                    <strong>Collaborations</strong><br>
                    <span style="color: #6C757D;">Research projects, open source</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🎓</span>
                <div>
                    <strong>Mentoring</strong><br>
                    <span style="color: #6C757D;">Students, career changers</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">💼</span>
                <div>
                    <strong>Consulting</strong><br>
                    <span style="color: #6C757D;">Data strategy, ML implementation</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Location & Timezone
    st.markdown("""
    <div class="contact-info">
        <h2>🌍 Location & Timezone</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin: 1rem 0;">
            <div class="contact-item">
                <span class="contact-icon">📍</span>
                <div>
                    <strong>Current Location</strong><br>
                    <span style="color: #6C757D;">Hong Kong SAR</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🕒</span>
                <div>
                    <strong>Timezone</strong><br>
                    <span style="color: #6C757D;">GMT+8 (Hong Kong Time)</span>
                </div>
            </div>
            <div class="contact-item">
                <span class="contact-icon">✈️</span>
                <div>
                    <strong>Travel</strong><br>
                    <span style="color: #6C757D;">Open to relocation & remote work</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
