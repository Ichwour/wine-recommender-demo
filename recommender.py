import json
import joblib
import pandas as pd
from catboost import Pool

def load_model(model_path="model.pkl"):
    return joblib.load(model_path)

def recommend(model, conditions_path="conditions.json", top_n=5):
    with open(conditions_path, encoding="utf-8") as f:
        query = json.load(f)

    query_df = pd.DataFrame([query])
    cat_features = ['producer', 'country', 'varietals', 'region', 'color', 'sugar']
    pool = Pool(query_df, cat_features=cat_features)

    probas = model.predict_proba(pool)[0]

    with open("wine_list.json", encoding="utf-8") as f:
        wine_list = json.load(f)

    ranked = sorted(zip(wine_list, probas), key=lambda x: -x[1])[:top_n]

    return [
        {**wine, "score": round(score, 4)}
        for wine, score in ranked
    ]

if __name__ == "__main__":
    model = load_model()
    results = recommend(model)
    for i, item in enumerate(results, 1):
        print(f"{i}. {item['name']} ({item['score']})")
