import sympy as sp

referidos, balance_por_referido = sp.symbols('referidos balance_por_referido')
referidos_nivel, niveles = sp.symbols('referidos_nivel niveles')
crecimiento_exponencial = 2**niveles
balance_total = referidos_nivel * crecimiento_exponencial * balance_por_referido


# Evaluar para un caso específico
evaluacion = balance_total.subs({referidos: 5, balance_por_referido: 100})
print(evaluacion)  # 500

# Evaluar para un caso específico
print(balance_total.subs({niveles: 3, balance_por_referido: 100}))  # 800
