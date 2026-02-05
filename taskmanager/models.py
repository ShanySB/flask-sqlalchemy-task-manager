from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.column(db.integer, primary_key=True)
    Category_name = db.Column(db.String(25), unique=True, nullable=False)
    task = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__to represent itself in the form of a string
        return self


class Task(db.Model):
    # schema for the Category model
    id = db.column(db.integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Colum(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    Category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__to represent itself in the form of a string
        return "#{0}- Task: | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )