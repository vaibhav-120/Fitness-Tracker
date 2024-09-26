from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for meal options
meal_options = {
    "breakfast": ["Oatmeal", "Avocado Toast", "Smoothie Bowl"],
    "lunch": ["Quinoa Salad", "Chickpea Wrap", "Vegetable Stir Fry"],
    "dinner": ["Grilled Tofu", "Pasta Primavera", "Sweet Potato Curry"]
}

# Endpoint to generate a meal plan
@app.route('/generate_meal_plan', methods=['GET'])
def generate_meal_plan():
    plan = {
        "breakfast": get_random_meal("breakfast"),
        "lunch": get_random_meal("lunch"),
        "dinner": get_random_meal("dinner")
    }
    return jsonify(plan)

# Helper function to get a random meal from options
def get_random_meal(meal_type):
    import random
    return random.choice(meal_options[meal_type])

if __name__ == '_main_':
    app.run(port=8080)