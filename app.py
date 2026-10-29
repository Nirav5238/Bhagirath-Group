from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'bhagirath_secret_key_veraval'

# Business Configuration Data
GROUP_INFO = {
    "name": "Bhagirath Group",
    "location": "Veraval, Gujarat",
    "phone": "+91 98765 43210",
    "email": "info@bhagirathgroup.com"
}

@app.route('/')
def home():
    return render_template('index.html', title="Home | Bhagirath Group Veraval")

@app.route('/transport')
def transport():
    return render_template('transport.html', title="Roadways & Logistics | Bhagirath Group")

@app.route('/real-estate')
def real_estate():
    return render_template('real_estate.html', title="Real Estate & Arcade | Bhagirath Group")

@app.route('/Service-to-client')
def Service_to_client():
    return render_template('cab.html', title="Service-to-client | Bhagirath Group")

@app.route('/farm-stay')
def farm_stay():
    return render_template('farm.html', title="Bhagirath Farm Stay")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    service = request.form.get('service')
    message = request.form.get('message')
    
    # Process inquiry (Log, store to DB, or send email)
    print(f"New Inquiry from {name} ({email}) for {service}: {message}")
    
    flash("Thank you! Your message has been received. We will contact you shortly.", "success")
    return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True, port=5000)