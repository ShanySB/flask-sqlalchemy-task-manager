from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = Task.query.all()
    return render_template("task.html", tasks=tasks)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category_name = request.form.get("category_name")

        # prevent duplicates
        existing_category = Category.query.filter_by(category_name=category_name).first()

        if existing_category:
            return "Category already exists"

        category = Category(category_name=category_name)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for("add_category"))  # stay on same page

    # 👇 THIS is what you're missing
    categories = Category.query.order_by(Category.category_name).all()

    return render_template("add_categories.html", categories=categories)


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)

    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_categories.html", category=category)