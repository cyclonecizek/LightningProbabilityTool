import joblib
import pandas as pd
def predict(data):
    clf = joblib.load("RFC_model.sav")
    clf_limited = joblib.load("RFC_model_limited_depth.sav")
    prediction = clf.predict_proba(data)
    prediction_limited = clf_limited.predict_proba(data)
    df_prob = pd.DataFrame(prediction)
    df_prob_limited = pd.DataFrame(prediction_limited)
    return df_prob[1]*100


def predict_limited(data):
    clf_limited = joblib.load("RFC_model_limited_depth.sav")
    prediction_limited = clf_limited.predict_proba(data)
    df_prob_limited = pd.DataFrame(prediction_limited)
    return df_prob_limited[1]*100
