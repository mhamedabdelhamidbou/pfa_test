import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def simulate_gbm(S0, mu, sigma, T, steps, simulations):
    dt = T / steps
    S = np.zeros((steps + 1, simulations))
    S[0] = S0

    for t in range(1, steps + 1):
        Z = np.random.standard_normal(simulations)
        S[t] = S[t - 1] * np.exp((mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)

    return S


def price_autocall(S, barriers, coupon, protection_level):
    final_prices = S[-1]
    early_redemption = np.any(S > barriers, axis=0)
    payoff = np.where(early_redemption, coupon,
                      np.where(final_prices > protection_level, final_prices, protection_level))
    return np.mean(payoff)


def black_scholes_price(S0, K, T, r, sigma):
    from scipy.stats import norm
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def pricing():
    st.title("Pricing d'un Autocall")

    S0 = st.number_input("Prix initial du sous-jacent", value=100.0)
    mu = st.number_input("Taux de rendement attendu", value=0.05)
    sigma = st.number_input("Volatilité annuelle", value=0.2)
    T = st.number_input("Maturité (années)", value=1.0)
    steps = st.number_input("Nombre de pas de temps", value=252, step=1)
    simulations = st.number_input("Nombre de simulations Monte Carlo", value=10000, step=1000)
    barrier = st.number_input("Barrière de remboursement anticipé", value=110.0)
    coupon = st.number_input("Coupon payé en cas de remboursement", value=5.0)
    protection_level = st.number_input("Niveau de protection", value=80.0)

    method = st.selectbox("Méthode de pricing", ["Monte Carlo", "Black-Scholes"])

    if st.button("Simuler et Pricer"):
        price = None
        if method == "Monte Carlo":
            S = simulate_gbm(S0, mu, sigma, T, int(steps), int(simulations))
            price = price_autocall(S, barrier, coupon, protection_level)
            st.write(f"Prix estimé de l'Autocall via Monte Carlo : {price:.2f}")

            fig = go.Figure()
            for i in range(min(100, S.shape[1])):
                fig.add_trace(go.Scatter(y=S[:, i], mode='lines', opacity=0.3, name=f'Simulation {i + 1}'))

            fig.add_hline(y=barrier, line=dict(color='red', dash='dash'), annotation_text='Barrière',
                          annotation_position='top left')
            fig.add_hline(y=protection_level, line=dict(color='green', dash='dash'), annotation_text='Protection',
                          annotation_position='bottom left')

            fig.update_layout(title="Simulations de prix sous GBM", xaxis_title="Temps", yaxis_title="Prix",
                              showlegend=False)
            st.plotly_chart(fig)

        elif method == "Black-Scholes":
            price = black_scholes_price(S0, protection_level, T, mu, sigma)
            st.write(f"Prix estimé de l'Autocall via Black-Scholes : {price:.2f}")


if __name__ == "__main__":
    pricing()