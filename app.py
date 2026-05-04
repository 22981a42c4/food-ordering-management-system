from flask import Flask, render_template, request

app = Flask(__name__)
menu = {
    "Pizza": {"price": 150, "photo": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg"},
    "Burger": {"price": 80, "photo": "https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80"},
    "Sandwich": {"price": 60, "photo": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80"},
    "Coffee": {"price": 40, "photo": "https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&w=800&q=80"},
    "Tea": {"price": 20, "photo": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80"},
    "Dum biryani": {"price": 250, "photo": "https://static.vecteezy.com/system/resources/thumbnails/039/320/570/small_2x/ai-generated-a-plate-of-indian-chicken-biryani-with-rice-and-chutney-chicken-biryani-concept-photo.jpeg"},
    "Fry piece biryani": {"price": 300, "photo": "https://i.ytimg.com/vi/ySPhGVskTnc/maxresdefault.jpg"},
    "Paneer biryani": {"price": 250, "photo": "https://www.indianhealthyrecipes.com/wp-content/uploads/2023/02/paneer-biryani-recipe.jpg"},
    "Special biryani": {"price": 350, "photo": "https://static.vecteezy.com/system/resources/previews/048/067/086/non_2x/biryani-dish-special-biryani-with-meat-and-rice-isolated-illustration-on-a-transparent-background-png.png"},
    "Chicken Fried Rice": {"price": 150, "photo": "https://tse2.mm.bing.net/th/id/OIP.IphM07zFgViDxBrDIiNufwHaE8?rs=1&pid=ImgDetMain&o=7&rm=3"},
    "Veg Fried Rice": {"price": 100, "photo": "https://recipesofhome.com/wp-content/uploads/2020/06/veg-fried-rice-recipe.jpg"}
}






@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        order = {}
        total = 0
        for item, details in menu.items():
            qty = request.form.get(item)
            if qty and qty.isdigit() and int(qty) > 0:
                qty = int(qty)
                order[item] = {"qty": qty, "subtotal": qty * details["price"]}
                total += qty * details["price"]

        # ✅ This is where you add it
        return render_template("bill.html", order=order, total_amount=total, menu=menu)

    # For GET requests, show the menu
    return render_template("index.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
