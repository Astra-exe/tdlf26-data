def sinergia(ph, pr, pj):
    """((Ph - Pr + PJ) / (11 * PJ)) * 100

    100 = todos los puntos a favor (10 por partido) y ninguno en contra.
    Con 3 partidos la constante es 33, con 2 partidos es 22.
    """
    return (ph - pr + pj) / (11 * pj) * 100