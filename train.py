import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("data.csv", header=None)
data.columns = ["interval"]

# Feature engineering
data["pause"] = data["interval"].apply(lambda x: 1 if x > 1 else 0)

X = data[["interval", "pause"]]
y = (data["interval"] < 0.5).astype(int)  # fake label (fast = focused)

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
