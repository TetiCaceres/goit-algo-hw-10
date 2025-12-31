import pulp

model = pulp.LpProblem('Maximize_Production', pulp.LpMaximize)

L = pulp.LpVariable("Limonade", lowBound=0, cat='Integer')
J = pulp.LpVariable("FruitJuice", lowBound= 0, cat='Integer')

model += L + J, "Production"

model += 2*L + J <= 100, "Water_Limit"
model += L <= 50, "Sugar_Limit"
model += L <= 30, "Lemon_Juice_Limit"
model += 2*J <= 40, "Fruit_Puree_Limit"



solver = pulp.COIN_CMD(
    path="/opt/homebrew/bin/cbc",
    msg=False
)
model.solve(solver)



limonade = L.varValue
fruit_juice = J.varValue

print(f"Status: {pulp.LpStatus[model.status]}")
print("Produce Limonade:", limonade)
print("Produce FruitJuice:", fruit_juice)
print("Total Production:", limonade + fruit_juice)
