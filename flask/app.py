#PS C:\Users\gagei\Documents\code\python\flask> python -m venv venv
#PS C:\Users\gagei\Documents\code\python\flask> .\venv\Scripts\activate
# install libraries in global but then go into virtual and run these
#PS C:\Users\gagei\Documents\code\python\flask> SET FLASK_APP=app.py
# PS C:\Users\gagei\Documents\code\python\flask> SET FLASK_ENV=development
# PS C:\Users\gagei\Documents\code\python\flask> flask run

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Database model for storing user data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Create the database tables if they don't exist yet
with app.app_context():
    db.create_all()

# Home route - Display all users
@app.route('/')
def home():
    users = User.query.all()  # Query all users from the database
    return render_template('index.html', users=users)

# Route to handle adding a new user (can be adapted for other forms)
@app.route('/add', methods=['POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        
        # Add a new user to the database
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()  # Commit the changes to the database
        
        return redirect(url_for('home'))  # Redirect to the home page after adding

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
