# Wine Recommender Demo 🍷

This repository demonstrates the core logic of a wine recommendation system using a pre-trained CatBoost model.

## 🔍 What it does

- Loads a saved CatBoost classification model.
- Accepts a query from `conditions.json` representing user preferences.
- Ranks a predefined list of wines (`wine_list.json`) based on model prediction scores.
- Outputs the top recommended wines with confidence scores.

## 📂 Files

- `recommender.py` – logic for loading the model and generating recommendations.
- `model.pkl` – pre-trained CatBoost model (must be placed alongside this script).
- `conditions.json` – input preferences for generating recommendations.
- `wine_list.json` – fixed list of wines available for recommendation.
- `requirements.txt` – Python dependencies.
- `LICENSE` – usage terms and conditions.

## 🚀 Usage

Run the script from terminal or an IDE:

```bash
python recommender.py
