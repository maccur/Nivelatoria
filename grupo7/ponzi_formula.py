import sympy as sp

referidos, balance_por_referido = sp.symbols('referidos balance_por_referido')
balance_total = referidos * balance_por_referido

# Evaluar para un caso específico
evaluacion = balance_total.subs({referidos: 5, balance_por_referido: 100})
print(evaluacion)  # 500