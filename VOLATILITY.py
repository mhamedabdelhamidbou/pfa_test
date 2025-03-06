import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def calculate_volatility(prices):
    """
    Calcule la volatilité annualisée à partir d'une série de prix.
    La volatilité est obtenue en calculant l'écart-type des log returns,
    puis en l'annualisant (en supposant 252 jours de bourse par an).
    """
    # Calcul des log returns
    log_returns = np.log(prices / prices.shift(1))
    # Écart-type des log returns quotidiens
    daily_vol = log_returns.std()
    # Annualisation (en supposant 252 jours de bourse)
    annual_vol = daily_vol * np.sqrt(252)
    return annual_vol, log_returns

def volatility_calculator():
    st.title("Calcul de la Volatilité")
    st.write("Cette page vous permet de calculer la volatilité annualisée d'un actif à partir de ses prix historiques.")

    st.write("Vous pouvez soit importer un fichier CSV contenant une colonne 'Price', soit saisir manuellement une série de prix séparés par des virgules.")

    # Option d'importation de fichier CSV
    uploaded_file = st.file_uploader("Importer un fichier CSV", type=["csv"])

    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file)
            if "Price" not in data.columns:
                st.error("Le fichier CSV doit contenir une colonne 'Price'.")
                return
            prices = data["Price"]
            st.write("Aperçu des données importées :")
            st.dataframe(data.head())
        except Exception as e:
            st.error("Erreur lors de la lecture du fichier CSV : " + str(e))
            return
    else:
        # Saisie manuelle des prix
        st.write("Saisie manuelle des prix (séparés par des virgules)")
        price_input = st.text_input("Entrez les prix historiques", "100,102,101,103,104")
        try:
            prices = pd.Series([float(x.strip()) for x in price_input.split(",")])
        except:
            st.error("Erreur dans la saisie des prix. Veuillez vérifier le format.")
            return

    if len(prices) < 2:
        st.error("Il faut au moins deux valeurs de prix pour calculer la volatilité.")
        return

    # Calcul de la volatilité
    annual_vol, log_returns = calculate_volatility(prices)
    st.write(f"La volatilité annualisée calculée est : **{annual_vol:.2%}**")

    # Visualisation de la série de prix
    fig_prices = go.Figure()
    fig_prices.add_trace(go.Scatter(
        x=np.arange(len(prices)),
        y=prices,
        mode='lines+markers',
        name='Prix'
    ))
    fig_prices.update_layout(
        title="Évolution des Prix",
        xaxis_title="Période",
        yaxis_title="Prix"
    )
    st.plotly_chart(fig_prices)

    # Visualisation des log returns
    # On ignore la première valeur NaN générée par le calcul du log return
    fig_returns = go.Figure()
    fig_returns.add_trace(go.Scatter(
        x=np.arange(1, len(prices)),
        y=log_returns.dropna(),
        mode='lines+markers',
        name='Log Returns'
    ))
    fig_returns.update_layout(
        title="Log Returns",
        xaxis_title="Période",
        yaxis_title="Log Return"
    )
    st.plotly_chart(fig_returns)

if __name__ == "__main__":
    volatility_calculator()
