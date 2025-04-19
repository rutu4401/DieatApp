import pandas as pd

data = {
    "Diet_Type": ["Veg", "Veg", "Veg", "Non-Veg", "Non-Veg", "Non-Veg"],
    "Calories": [1500, 1800, 2000, 1500, 1800, 2000],
    "Protein": [50, 60, 70, 60, 70, 80],
    "Calcium": [500, 600, 700, 550, 650, 750],
    "Breakfast": [
        "Oats with Almonds & Fruits",
        "Sprouts with Brown Bread",
        "Paneer Paratha with Yogurt",
        "Boiled Eggs with Whole Wheat Toast",
        "Grilled Chicken Sandwich",
        "Omelette with Brown Bread"
    ],
    "Lunch": [
        "Dal, Rice, Veggies, Curd",
        "Chickpea Salad & Whole Wheat Roti",
        "Rajma, Brown Rice, Buttermilk",
        "Grilled Chicken with Quinoa",
        "Fish Curry with Brown Rice",
        "Chicken Breast with Steamed Veggies"
    ],
    "Dinner": [
        "Vegetable Soup & Salad",
        "Tofu Stir Fry with Quinoa",
        "Khichdi with Yogurt",
        "Grilled Salmon with Veggies",
        "Chicken Soup & Brown Rice",
        "Boiled Eggs & Avocado Salad"
    ]
}

df = pd.DataFrame(data)
df.to_csv("diet_plans.csv", index=False)
print("Dataset saved as diet_plans.csv")
