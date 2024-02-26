import joblib
import pandas as pd
def predict(data):
    clf = joblib.load("RFC_model.sav")
    prediction = clf.predict_proba(data)
    df_prob = pd.DataFrame(prediction)
    return df_prob[1]*100
