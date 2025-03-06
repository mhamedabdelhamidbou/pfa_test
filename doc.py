import streamlit as st

def documentation_page():
    st.title("Documentation sur les Autocall")
    st.markdown("""
    ## Introduction
    Les produits **autocall** sont des instruments financiers structurés qui offrent un rendement conditionnel basé sur l'évolution d'un sous-jacent, généralement un indice boursier. Leur particularité réside dans le fait que le remboursement peut être anticipé si certaines conditions de marché sont atteintes, comme un niveau d'indice fixé à l'avance. En d'autres termes, si le sous-jacent atteint un seuil spécifique pendant la durée de vie du produit, le remboursement s'effectue avant la date de maturité, avec un gain prédéterminé. 

    Ces produits sont souvent utilisés par les investisseurs pour générer des rendements dans des conditions de marché fluctuantes. Cette documentation présente une analyse détaillée de la **valorisation** (pricing) et de la **couverture** (hedging) des autocalls, en utilisant des méthodes avancées telles que la simulation Monte Carlo et la modélisation stochastique basée sur le **mouvement brownien géométrique** (GBM).

    ## Contexte et Objectifs
    Ce travail fait partie du **Projet de Fin d'Année (PFA)** du 2ème cycle en **Finance et Ingénierie Décisionnelle** à l’**ENSA Agadir**. Le projet porte sur l’analyse des produits structurés, avec une focalisation sur les **autocalls** indexés sur les indices boursiers. 

    Le thème du projet est :  
    **"Analyse des produits structurés : Pricing et couverture des autocalls indexés sur les indices boursiers au sein de Oracle Capital"**.  
    Le travail est réalisé en collaboration avec **Oracle Capital**, une entreprise de gestion d'actifs et de solutions d'investissement qui fournit une expertise dans l'optimisation des produits financiers pour ses clients.

    ### Objectifs du Projet :
    - Développer une méthodologie robuste pour le **pricing** des autocalls.
    - Concevoir des stratégies de **couverture (hedging)** pour réduire le risque lié aux produits structurés.
    - Tester des scénarios de marché en simulant l'évolution des indices boursiers sur des périodes spécifiques.

    ## Méthodologie
    Le projet repose sur plusieurs axes méthodologiques complémentaires pour analyser le comportement des autocalls dans différents contextes de marché.

    - **Modélisation Mathématique :**  
      Nous utilisons des modèles stochastiques, notamment le **mouvement brownien géométrique (GBM)**, pour simuler l'évolution du sous-jacent, en prenant en compte les facteurs tels que le taux d'intérêt sans risque et la volatilité implicite.
    
    - **Simulation Monte Carlo :**  
      La simulation Monte Carlo est utilisée pour estimer la valeur des produits autocall en générant plusieurs trajectoires du sous-jacent et en calculant le paiement du produit dans chaque scénario simulé. Cette méthode permet de mieux appréhender l'incertitude des rendements futurs et d'estimer le risque associé aux autocalls.

    - **Analyse de Sensibilité :**  
      Nous effectuons une analyse de sensibilité pour comprendre comment les variations des paramètres (volatilité, taux sans risque, coupons) influencent la valorisation des autocalls. Cela permet de déterminer les leviers sur lesquels il est possible d'agir pour optimiser les rendements.

    - **Stratégies de Couverture (Hedging) :**  
      Des stratégies de couverture sont développées pour minimiser les risques de marché. Celles-ci incluent des techniques comme les **options**, les **futures** et les **swaps**, permettant de réduire l'impact des fluctuations de l'indice boursier sur le portefeuille.

    ## Résultats et Perspectives
    Les résultats obtenus à partir des simulations et des modèles de pricing nous permettent de mieux comprendre les dynamiques des autocalls dans divers scénarios de marché. Ces résultats ouvrent également des pistes d’optimisation pour améliorer les stratégies de couverture et de valorisation, en prenant en compte les évolutions des indices boursiers et des variables macroéconomiques.

    Les perspectives incluent l'intégration de techniques de **deep learning** et d'**IA** pour améliorer encore la précision des modèles de pricing, ainsi que l'étude d'autres produits dérivés structurés similaires, comme les **reverse convertibles** ou les **bonus certificates**.

    ## Équipe et Encadrement
    Ce travail a été réalisé par :
    - **BOU Mhamed Abdelhamid**
    - **BENLAMINE Mouad**  
      *(Élèves ingénieurs en 2ème année à l'ENSA Agadir)*

    Sous l'encadrement de :
    - **Monsieur Al Asri** *(Encadrant académique à l'ENSA Agadir)*
    - **Monsieur Anass Nadim** *(Encadrant entreprise chez Oracle Capital)*

    ## À propos de l'ENSA Agadir
    L’**ENSA Agadir** (École Nationale Supérieure d’Applications) est une institution d'enseignement supérieur renommée qui forme des ingénieurs dans divers domaines, dont l'ingénierie décisionnelle, la finance et les systèmes d'information. L'école offre une formation rigoureuse, axée sur l'innovation et la pratique, avec une forte composante de projets appliqués en collaboration avec des entreprises partenaires.

    ## À propos de Oracle Capital
    **Oracle Capital** est une société de gestion d'actifs et de conseil financier qui se spécialise dans les produits financiers structurés, l'optimisation de portefeuilles et la gestion des risques. Elle propose des solutions sur mesure pour les investisseurs institutionnels et privés, en se basant sur des modèles financiers avancés pour maximiser les rendements tout en contrôlant le risque. Leur expertise en matière d’autocalls et de produits dérivés en fait un partenaire idéal pour ce projet.

    ## Conclusion
    Ce projet représente une contribution significative dans l’analyse des produits structurés, en combinant rigueur théorique et application pratique. Les techniques de pricing et de couverture développées dans ce cadre offrent un outil précieux pour Oracle Capital et pour l’ensemble des acteurs du marché financier, en vue d'optimiser les stratégies d'investissement et de gestion du risque.

    """, unsafe_allow_html=True)

if __name__ == "__main__":
    documentation_page()
