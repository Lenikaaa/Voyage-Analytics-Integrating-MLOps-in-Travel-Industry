from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load(
    "model/flight_prediction/xgb_regressor.pkl"
)

feature_columns = joblib.load(
    "model/flight_prediction/feature_columns.pkl"
)


@app.route("/")
def home():
    return "Flight Price Prediction API Running"


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    df = pd.DataFrame([data])

    df = pd.get_dummies(df)

    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    prediction = model.predict(df)[0]

    return jsonify({
        "predicted_price": float(prediction)
    })


if __name__ == "__main__":
    app.run(debug=True)