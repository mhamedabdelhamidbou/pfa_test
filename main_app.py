import os
import streamlit as st
from streamlit_navigation_bar import st_navbar
from princing import pricing
from market import market_scenarios
from VOLATILITY import volatility_calculator
from doc import documentation_page
st.set_page_config(initial_sidebar_state="collapsed", layout="wide")

# Mise à jour de la liste des pages sans "Community"
pages = ["pricing", "market scenarios", "volatility", "documentation", "About"]

parent_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(parent_dir, "cubes.svg")
urls = {"About": "http://www.ensa-agadir.ac.ma/"}
styles = {
    "nav": {
        "background-color": "royalblue",
        "justify-content": "left",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "padding": "14px",
    },
    "active": {
        "background-color": "white",
        "color": "var(--text-color)",
        "font-weight": "normal",
        "padding": "14px",
    }
}
options = {
    "show_menu": False,
    "show_sidebar": False,
}

# Affichage de la barre de navigation et récupération de la page sélectionnée
page_selected = st_navbar(
    pages,
    logo_path=logo_path,
    urls=urls,
    styles=styles,
    options=options,
)

# Dictionnaire associant les pages aux fonctions correspondantes (sans la page "Community")
functions = {
    "pricing": pricing,
    "market scenarios": market_scenarios,
    "volatility": volatility_calculator,  # Remarquez l'absence de parenthèses
    "documentation": documentation_page,
}

# Affichage de la page sélectionnée uniquement
if page_selected in functions:
    functions[page_selected]()
elif page_selected == "About":
    st.write("Page 'About me' est un lien externe.")
