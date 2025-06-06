import streamlit as st

def load_css():
    """Load custom CSS styles"""
    st.markdown("""
    <style>
    /* Global Variables */
    :root {
        --primary-color: #2C3E50;
        --secondary-color: #3498DB;
        --accent-color: #E74C3C;
        --success-color: #27AE60;
        --background-color: #F8F9FA;
        --card-background: #FFFFFF;
        --text-muted: #6C757D;
        --border-color: #DEE2E6;
        --shadow-light: 0 2px 4px rgba(0,0,0,0.1);
        --shadow-medium: 0 4px 6px rgba(0,0,0,0.1);
        --shadow-heavy: 0 8px 25px rgba(0,0,0,0.15);
        --border-radius: 12px;
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, var(--primary-color), #34495E);
        color: white;
        border-radius: 0 15px 15px 0;
    }
    
    .sidebar-header {
        text-align: center;
        padding: 1rem 0;
        border-bottom: 2px solid rgba(255,255,255,0.2);
        margin-bottom: 1rem;
    }
    
    .sidebar-header h1 {
        color: white !important;
        font-size: 1.8rem;
        margin: 0;
    }
    
    .sidebar-header p {
        color: #BDC3C7;
        font-size: 0.9rem;
        margin: 0.5rem 0 0 0;
        font-style: italic;
    }
    
    .sidebar-footer {
        margin-top: 2rem;
        padding: 1rem;
        background: rgba(0,0,0,0.1);
        border-radius: 10px;
    }
    
    .sidebar-footer h3 {
        color: white !important;
        font-size: 1rem;
        margin: 0 0 0.5rem 0;
    }
    
    .sidebar-footer a {
        color: #85C1E9;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .sidebar-footer a:hover {
        color: white;
    }

    /* Main Container */
    .main .block-container {
        padding: 2rem 3rem 5rem 3rem;
        max-width: 1200px;
    }

    /* Typography */
    h1 {
        color: var(--primary-color);
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    h2 {
        color: var(--primary-color);
        font-size: 2.2rem;
        font-weight: 600;
        margin: 2.5rem 0 1.5rem 0;
        border-bottom: 3px solid var(--secondary-color);
        padding-bottom: 0.5rem;
    }

    h3 {
        color: var(--primary-color);
        font-size: 1.6rem;
        font-weight: 600;
        margin: 2rem 0 1rem 0;
    }

    /* Card Styles */
    .experience-card, .education-card, .project-card, .contact-info, .resume-section {
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: var(--shadow-light);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .experience-card::before, .education-card::before, .project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    }

    .experience-card:hover, .education-card:hover, .project-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-heavy);
        border-color: var(--secondary-color);
    }

    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, var(--secondary-color), var(--primary-color));
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 25px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem;
        box-shadow: var(--shadow-light);
        transition: all 0.3s ease;
    }

    .skill-tag:hover {
        transform: scale(1.1) translateY(-2px);
        box-shadow: var(--shadow-medium);
    }

    /* Profile Section */
    .profile-container {
        text-align: center;
        margin: 3rem 0;
        padding: 2rem;
        background: var(--card-background);
        border-radius: var(--border-radius);
        box-shadow: var(--shadow-light);
    }

    /* Contact Items */
    .contact-item {
        display: flex;
        align-items: center;
        margin: 1rem 0;
        padding: 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        background: var(--background-color);
    }

    .contact-item:hover {
        background: var(--secondary-color);
        color: white;
        transform: translateX(10px);
        box-shadow: var(--shadow-medium);
    }

    .contact-icon {
        margin-right: 1.5rem;
        font-size: 1.5rem;
        width: 40px;
        text-align: center;
    }

    /* Button Styles */
    .stButton > button {
        background: linear-gradient(135deg, var(--secondary-color), var(--primary-color)) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 1rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
        margin: 0.3rem 0 !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-medium) !important;
    }

    .stDownloadButton > button {
        background: linear-gradient(135deg, var(--success-color), #2ECC71) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: var(--shadow-light) !important;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: var(--shadow-heavy) !important;
    }

    /* Statistics Cards */
    .stat-card {
        background: var(--card-background);
        border-radius: var(--border-radius);
        padding: 2rem 1.5rem;
        text-align: center;
        box-shadow: var(--shadow-light);
        border: 1px solid var(--border-color);
        transition: all 0.3s ease;
        position: relative;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
    }

    .stat-card:hover {
        transform: translateY(-8px);
        box-shadow: var(--shadow-heavy);
    }

    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }

    .stat-label {
        color: var(--text-muted);
        font-size: 1rem;
        margin: 1rem 0 0 0;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
    }

    /* Timeline */
    .timeline {
        position: relative;
        margin: 3rem 0;
    }

    .timeline::before {
        content: '';
        position: absolute;
        left: 30px;
        top: 0;
        bottom: 0;
        width: 3px;
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        border-radius: 2px;
    }

    .timeline-item {
        position: relative;
        margin: 3rem 0;
        padding-left: 4rem;
    }

    .timeline-item::before {
        content: '';
        position: absolute;
        left: 18px;
        top: 8px;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        background: var(--secondary-color);
        border: 4px solid var(--card-background);
        box-shadow: var(--shadow-medium);
    }

    /* Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 8px !important;
        border: 2px solid var(--border-color) !important;
        transition: all 0.3s ease !important;
        padding: 0.8rem !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: var(--secondary-color) !important;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2) !important;
    }

    /* Footer */
    .footer {
        background: linear-gradient(135deg, var(--primary-color), #34495E);
        color: white;
        text-align: center;
        padding: 3rem 0;
        margin-top: 4rem;
        border-radius: var(--border-radius) var(--border-radius) 0 0;
        box-shadow: 0 -5px 15px rgba(0,0,0,0.1);
    }

    .footer a {
        color: #85C1E9;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .footer a:hover {
        color: white;
        text-decoration: underline;
    }

    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(40px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .fade-in-up {
        animation: fadeInUp 0.8s ease-out;
    }

    @keyframes slideInRight {
        from {
            opacity: 0;
            transform: translateX(40px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    .slide-in-right {
        animation: slideInRight 0.8s ease-out;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    .float {
        animation: float 3s ease-in-out infinite;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
        .main .block-container {
            padding: 1rem;
        }
        
        h1 {
            font-size: 2.2rem;
        }
        
        h2 {
            font-size: 1.8rem;
        }
        
        .timeline-item {
            padding-left: 2.5rem;
        }
        
        .timeline::before {
            left: 20px;
        }
        
        .timeline-item::before {
            left: 8px;
        }
    }

    /* Success Messages */
    .stSuccess {
        background: linear-gradient(135deg, var(--success-color), #2ECC71) !important;
        color: white !important;
        border-radius: var(--border-radius) !important;
        border: none !important;
    }

    /* Expander Styling */
    .streamlit-expanderHeader {
        background: var(--card-background) !important;
        border-radius: var(--border-radius) !important;
        border: 2px solid var(--border-color) !important;
        box-shadow: var(--shadow-light) !important;
        transition: all 0.3s ease !important;
    }

    .streamlit-expanderHeader:hover {
        box-shadow: var(--shadow-medium) !important;
        border-color: var(--secondary-color) !important;
    }
    </style>
    """, unsafe_allow_html=True) 