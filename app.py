from flask import Flask, jsonify, redirect, render_template, request, flash, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'qwertyuiop1234567890'


users = {}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return render_template('home.html', username=username)
        else:
            flash('Invalid username or password')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error='Username already exists')
        else:
            users[username] = password
            flash('Registration successful')
            return redirect(url_for('login'))  # Redirect to login page after successful registration
    else:
        return render_template('register.html')

# Route for the dashboard page
@app.route('/home')
def dashboard():
        return render_template('home.html')


@app.route("/api/nft_data")
def nft_data():
    # Generate fake data for the NFT
    sales_data = [random.randint(1, 10) for _ in range(7)]
    views_data = [random.randint(10, 100) for _ in range(7)]
    prefix = "ERC"
    suffix = str(random.randint(1, 999))
    peak = f"{prefix}{suffix}"

    # Calculate total sales and views for the NFT
    total_sales = sum(sales_data)
    total_views = sum(views_data)

    # Return the data as JSON
    return jsonify({
        "sales": sales_data,
        "views": views_data,
        "peak" : peak,
        "total_sales": total_sales,
        "total_views": total_views,
    })

if __name__ == "__main__":
    app.run(debug=True)
