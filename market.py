import streamlit as st
import numpy as np
import plotly.graph_objects as go


# Fonction de simulation de Monte Carlo pour le pricing de l'autocall
def simulate_autocall(S0, r, sigma, T, observations, strike_level, coupon, n_simulations):
    dt = T / observations  # pas de temps par observation
    payoff = np.zeros(n_simulations)

    # Simulation pour chaque scénario
    for i in range(n_simulations):
        S = S0  # prix initial
        for t in range(1, observations + 1):
            # Simulation du prix du sous-jacent avec le modèle GBM
            Z = np.random.normal(0, 1)
            S = S * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

            # Activation de l'autocall si le niveau est atteint
            if S >= strike_level:
                payoff[i] = coupon * S  # remboursement avec coupon
                break
        if payoff[i] == 0:
            payoff[i] = 0  # Aucun remboursement si le niveau n'est jamais atteint

    # Actualisation des payoffs
    discounted_payoff = np.mean(payoff) * np.exp(-r * T)
    return discounted_payoff


# Fonction de la page Scénarios de Marché avec Plotly
def market_scenarios():
    st.title("Scénarios de Marché")
    st.write("""
        Testez l'impact des différents scénarios économiques sur la valorisation de l'autocall.
        Choisissez parmi les scénarios suivants : Hausse, Baisse, Volatilité faible ou Volatilité élevée.
    """)

    # Paramètres de base
    S0 = st.number_input("Prix initial du sous-jacent (S0)", value=100)
    strike_level = st.number_input("Niveau d'activation de l'autocall (%)", value=110) / 100 * S0
    coupon = st.number_input("Coupon annuel (%)", value=5) / 100
    T = st.slider("Durée de l'autocall (années)", 1, 10, 5)
    observations = st.slider("Nombre d'observations par an", 1, 12, 2)
    r = st.number_input("Taux sans risque (%)", value=2) / 100
    sigma = st.number_input("Volatilité (%)", value=20) / 100
    n_simulations = st.number_input("Nombre de simulations Monte Carlo", value=1000)

    # Choix du scénario
    scenario = st.selectbox("Choisissez un scénario de marché",
                            ['Hausse', 'Baisse', 'Volatilité faible', 'Volatilité élevée'])

    # Ajustement des paramètres selon le scénario
    if scenario == 'Hausse':
        S0 *= 1.10
        st.write("Le marché est en forte hausse, le prix initial augmente de 10%.")
    elif scenario == 'Baisse':
        S0 *= 0.90
        st.write("Le marché est en baisse, le prix initial baisse de 10%.")
    elif scenario == 'Volatilité faible':
        sigma = 0.10
        st.write("La volatilité est faible, réduite à 10%.")
    elif scenario == 'Volatilité élevée':
        sigma = 0.30
        st.write("La volatilité est élevée, augmentée à 30%.")

    # Calcul du prix de l'autocall via simulation Monte Carlo
    autocall_price = simulate_autocall(S0, r, sigma, T, observations, strike_level, coupon, n_simulations)
    st.write(f"Le prix estimé de l'autocall sous le scénario '{scenario}' est de : {autocall_price:.2f} EUR")

    # Simulation d'une trajectoire de l'actif sous-jacent pour visualisation
    t = np.linspace(0, T, 100)
    # Attention : np.sqrt(t) est utilisé, il faut gérer t=0 pour éviter une division par zéro
    sqrt_t = np.sqrt(t)
    sqrt_t[0] = 0
    prices = S0 * np.exp((r - 0.5 * sigma ** 2) * t + sigma * sqrt_t * np.random.randn(100))

    # Création du graphique interactif avec Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t, y=prices, mode='lines', name='Simulation du prix sous-jacent'))
    fig.add_trace(go.Scatter(x=[0, T], y=[strike_level, strike_level],
                             mode='lines', name="Niveau d'activation",
                             line=dict(dash='dash', color='red')))
    fig.update_layout(title=f"Évolution du prix de l'autocall sous le scénario : {scenario}",
                      xaxis_title="Temps (années)",
                      yaxis_title="Prix du sous-jacent")

    st.plotly_chart(fig)


if __name__ == "__main__":
    market_scenarios()
