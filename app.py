from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])  # 🔥 POST allowed here (Fix for 405)
def predict():
    if 'image' not in request.files:
        return "No file uploaded"

    file = request.files['image']

    if file.filename == '':
        return "No selected file"

    # Save uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Dummy prediction (replace with your ML model)
    prediction = "eosinophil"

    return render_template('result.html',
                           prediction=prediction,
                           img_path=file.filename)

if __name__ == '__main__':
    app.run(debug=True)