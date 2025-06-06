import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(
    page_title="Sarah Johnson | Data Scientist Portfolio", 
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🌟"
)

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func, icon):
        self.apps.append({"title": title, "function": func, "icon": icon})

    def run(self):
        # Load custom CSS
        load_css()

        # Enhanced sidebar with beautiful navigation
        st.sidebar.markdown("""
        <div class="sidebar-header">
            <h1>🌟 Sarah Johnson</h1>
            <p>Data Scientist & ML Engineer</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.sidebar.markdown("---")
        
        # Beautiful navigation menu
        st.sidebar.markdown("""
        <div class="nav-title">
            <h2>📋 Navigation</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Create navigation with icons
        selected_app = None
        for app in self.apps:
            if st.sidebar.button(
                f"{app['icon']} {app['title']}", 
                key=app['title'],
                use_container_width=True
            ):
                selected_app = app
        
        # If no app is selected via button, use radio as fallback (hidden)
        if selected_app is None:
            app_index = st.sidebar.radio(
                "Navigation", 
                range(len(self.apps)), 
                format_func=lambda i: f"{self.apps[i]['icon']} {self.apps[i]['title']}",
                key="nav_radio",
                label_visibility="collapsed"
            )
            selected_app = self.apps[app_index]
        
        st.sidebar.markdown("---")
        
        # Sidebar footer
        st.sidebar.markdown("""
        <div class="sidebar-footer">
            <h3>🔗 Quick Links</h3>
            <p><a href="mailto:sarah.johnson@example.com">📧 Email</a></p>
            <p><a href="https://linkedin.com/in/sarahjohnson" target="_blank">💼 LinkedIn</a></p>
            <p><a href="https://github.com/sarahjohnson" target="_blank">💻 GitHub</a></p>
        </div>
        """, unsafe_allow_html=True)

        # Execute selected page
        selected_app["function"]()
        
        # Display footer at the bottom of each page
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app with icons
app.add_app("Home", home_page, "🏠")
app.add_app("Education", education_page, "🎓")
app.add_app("Experience", experience_page, "💼")
app.add_app("Resume", resume_page, "📄")
app.add_app("Contact", contact_page, "📞")

# Run the app
app.run()
