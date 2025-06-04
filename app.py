from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    sugar = float(request.form['sugar'])
    systolic = int(request.form['systolic'])
    diastolic = int(request.form['diastolic'])

    # Sugar Level Interpretation
    if sugar < 100:
        sugar_status = "Normal"
    elif 100 <= sugar <= 125:
        sugar_status = "Prediabetes"
    else:
        sugar_status = "Diabetes"

    # BP Interpretation
    if systolic < 120 and diastolic < 80:
        bp_status = "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        bp_status = "Elevated"
    elif (130 <= systolic < 140) or (80 <= diastolic < 90):
        bp_status = "High Blood Pressure (Stage 1)"
    elif systolic >= 140 or diastolic >= 90:
        bp_status = "High Blood Pressure (Stage 2)"
    else:
        bp_status = "Consult a doctor"

    return render_template('index.html', sugar_status=sugar_status, bp_status=bp_status)

if __name__ == '__main__':
    app.run(debug=True)
