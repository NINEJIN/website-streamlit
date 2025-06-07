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
                    <h3 class="card-title">🚀 Marketing Intern</h3>
                    <p class="card-subtitle">Guangdong Yuehai Industrial Park Investment Holdings Co., Ltd.</p>
                    <p class="card-meta">March 2023 – May 2023</p>
                </div>
                <div class="card-content">
                    <ul style="line-height: 1.8; padding-left: 1.5rem;">
                        <li>📊 Conducted market research and competitor analysis to support strategic marketing plans</li>
                        <li>📈 Assisted in brand development and improved internal marketing management systems</li>
                        <li>📱 Managed official social media content and handled external communications</li>
                        <li>📂 Analyzed member data to support customer engagement initiatives</li>
                    </ul>
                </div>
            </div>
        </div>
         <div class="timeline">
        <div class="timeline-item">
            <div class="experience-card">
                <div class="card-header">
                    <h3 class="card-title">🚀 Investment Banking Intern</h3>
                    <p class="card-subtitle">China International Capital Corporation Limited (CICC)</p>
                    <p class="card-meta">July 2021 – August 2021</p>
                </div>
                <div class="card-content">
                    <ul style="line-height: 1.8; padding-left: 1.5rem;">
                        <li>📉 Conducted industry research in the online ride-hailing and energy technology sectors for IPO valuation</li>
                        <li>📑 Drafted capital operation proposals and internal financial documents</li>
                        <li>🔍 Evaluated investment opportunities and supported project due diligence</li>
                        <li>🤝 Collaborated with team members across departments to prepare client presentations</li>
                    </ul>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("---")



    st.markdown("---")