import streamlit as st
from datetime import datetime

def display_footer():
    """Display a beautiful footer across all pages"""
    current_year = datetime.now().year
    
    footer = f"""
    <div class="footer">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 2rem;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <h4 style="margin: 0; color: white;">Qinyuan Xiao</h4>
                    <p style="margin: 0.5rem 0 0 0; color: #BDC3C7;">Master in Marketing</p>
                </div>
                <div style="text-align: right;">
                    <p style="margin: 0; color: #BDC3C7;">
                        © {current_year} Qinyuan Xiao | 
                        <a href="mailto:qinyuanxiao1115@gmail.com" style="color: #3498DB; text-decoration: none;">
                            📧 Contact Me
                        </a>
                    </p>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; color: #95A5A6;">
                        Last Updated: {datetime.now().strftime("%B %Y")}
                    </p>
                </div>
            </div>
        </div>
    </div>
    
    <style>
    .footer {{
        margin-top: 30px;
        padding-top: 10px;
        border-top: 1px solid #dee2e6;
        text-align: center;
        font-size: 0.8rem;
        color: #6c757d;
    }}
    .footer a:hover {{
        text-decoration: underline;
    }}
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True) 