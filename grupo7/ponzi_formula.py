import sympy as sp

balance_por_referido = sp.symbols('balance_por_referido')
referidos_nivel, niveles = sp.symbols('referidos_nivel niveles')
crecimiento_exponencial = 2**niveles
balance_total = referidos_nivel * crecimiento_exponencial * balance_por_referido


print(balance_total.subs({niveles: 3, balance_por_referido: 100}))  # 800
