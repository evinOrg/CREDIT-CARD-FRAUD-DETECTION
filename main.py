import streamlit as st 
from streamlit_option_menu import option_menu
import home, dataset, model, prediction


st.set_page_config(
    page_title="CREDIT CARD FRAUD DETECTION",
    page_icon="💳"
)
st.title("CREDIT CARD FRAUD DETECTION")

class multiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        selected = option_menu(
            menu_title=None,
            options=['Home', 'Dataset', 'Model', 'Prediction'],
            icons=['🏠', '📊', '🧪', '💳'],
            default_index=0,
            orientation="horizontal"
        )

        for app in self.apps:
            if selected == app['title']:
                app['function']()

# Instantiate the multiApp class and run the application
app = multiApp()

# Add all your apps to the multiApp instance
app.add_app('Home', home.app)
app.add_app('Dataset', dataset.app)
app.add_app('Model', model.app)
app.add_app('Prediction', prediction.app)

# Run the application
app.run()
