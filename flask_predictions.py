from flask import Flask, request, jsonify
import boto3
import joblib
import pandas as pd
import io

# === Load model from S3 ===
s3 = boto3.client(
    "s3",
    aws_access_key_id='',
    aws_secret_access_key='',
    region_name='us-east-1'
)

bucket = "taxi-models-group9"
key = "output/RandomForest_200_taxi.joblib"

# Load model from S3
response = s3.get_object(Bucket=bucket, Key=key)
model = joblib.load(io.BytesIO(response["Body"].read()))

# Print the features the model expects
print("✅ Model expects features:")
print(list(model.feature_names_in_))

# === Flask app ===
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Create DataFrame with columns in the same order as training
        input_df = pd.DataFrame([data], columns=model.feature_names_in_)

        # Predict
        prediction = model.predict(input_df)[0]

        return jsonify({
            "predicted_price": round(prediction, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
