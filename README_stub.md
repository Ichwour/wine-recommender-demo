# 🧪 Wine Recommender — Interactive Stub Demo 🍷

This repository presents an interactive **stub-based demo** of a wine recommendation system.  
It simulates the behavior of a real recommendation engine without performing actual data processing or model inference.

---

## What it simulates

- A modular project for wine recommendation based on user preferences.
- Menu-driven launch of various components (`parser`, `statistic`, `recommender`, etc.).
- Each module prints **step-by-step messages** emulating its real functionality.
- Intended for demonstration, prototyping, and team discussion.

---

## Project Structure

- `start_stub.py` – central launcher with interactive menu for all components.
- `parser_stub.py` – simulates data preprocessing, cleaning, and wine catalog setup.
- `statistic_stub.py` – simulates analytics on sales data and user behavior.
- `rabbit_stub.py` – simulates popularity modeling with Vowpal Wabbit.
- `cluster_stub.py` – simulates clustering of wines based on features.
- `cat_stub.py` – simulates training a CatBoost classifier for wine categorization.
- `recommender_stub.py` – simulates generating top-10 wine recommendations.

---

## Example Output (recommender stub)

```
    Stub: generating wine recommendations
    Would load CatBoost model for cluster prediction
    Would compute user relevance based on history or input
    Would rank wines using a weighted formula
    Would segment top-10 list into categories:
        - Top 3 by personal match
        - 3 by varietals
        - 3 by fallback clustering
        - 1 wildcard
    Would save recommendation to JSON and optionally visualize
    Stub complete.
```

---

## How to run

From terminal or IDE:

```bash
python start_stub.py
```

Choose a module from the menu to simulate its behavior.

---

## Notes

This stub version contains **no real model, no data, and no training logic**.  
It is designed for UI/UX walkthroughs, interface prototyping, or team onboarding.

To switch to the real implementation, replace `*_stub.py` files with their full counterparts.