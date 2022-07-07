import pandas as pd

STATES = []
print(len(STATES))
data = pd.read_csv("50_states.csv")
for state in data.state:
    STATES.append(state)
print(STATES)
print(len(STATES))