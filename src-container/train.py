import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ----- Step 1: Generate large synthetic dataset -----
np.random.seed(42)
n_samples = 20000

data = pd.DataFrame({
    "customer_id": np.arange(n_samples),
    "age": np.random.randint(18, 65, n_samples),
    "income": np.random.randint(30000, 150000, n_samples),
    "loyalty_score": np.random.randint(1, 10, n_samples),
    "region": np.random.choice(["North", "South", "East", "West"], n_samples),
    "visits_per_month": np.random.randint(1, 20, n_samples),
})

# Target: AOV
data["aov"] = (
    data["income"] * 0.001
    + data["loyalty_score"] * 10
    + data["visits_per_month"] * 5
    + np.random.normal(0, 20, n_samples)
)

# ----- Step 2: Preprocessing -----
X = data.drop(columns=["aov", "customer_id"])
y = data["aov"]

categorical = ["region"]
numerical = ["age", "income", "loyalty_score", "visits_per_month"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----- Step 3: Models + Hyperparams -----
models = {
    "LinearRegression": (LinearRegression(), {}),
    "RandomForest": (
        RandomForestRegressor(random_state=42),
        {"model__n_estimators": [50, 100],
         "model__max_depth": [5, 10]}
    ),
    "GradientBoosting": (
        GradientBoostingRegressor(random_state=42),
        {"model__n_estimators": [50, 100],
         "model__learning_rate": [0.05, 0.1]}
    ),
}

results = []
best_model = None
best_score = -np.inf

# ----- Step 4: Grid Search Training -----
for name, (model, params) in models.items():
    pipe = Pipeline([("pre", preprocessor), ("model", model)])
    if params:
        grid = GridSearchCV(pipe, params, cv=3, scoring="r2", n_jobs=-1)
        grid.fit(X_train, y_train)
        candidate = grid.best_estimator_
    else:
        candidate = pipe.fit(X_train, y_train)

    preds = candidate.predict(X_test)
    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    results.append((name, r2, mse))
    if r2 > best_score:
        best_score = r2
        best_model = candidate

# Leaderboard
print("\nLeaderboard (Regression with GridSearch)")
for r in results:
    print(f"{r[0]} --> R2: {r[1]:.4f}, MSE: {r[2]:.2f}")

# ----- Step 5: Save best model -----
with open("regression_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("Best Model Details\n", best_model)
print("Best R2 Score\t", round(best_score, 4))