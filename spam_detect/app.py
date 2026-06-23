import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Spam Detection Dashboard",
    page_icon="📧",
    layout="wide"
)

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_message(message):

    if not message.strip():
        return None

    transformed = vectorizer.transform([message])

    prediction = model.predict(transformed)[0]

    probability = model.predict_proba(transformed).max()

    return prediction, probability


def batch_predict(uploaded_file):

    df = pd.read_csv(uploaded_file)

    predictions = []

    for msg in df["text"]:
        transformed = vectorizer.transform([str(msg)])
        pred = model.predict(transformed)[0]
        predictions.append(pred)

    df["prediction"] = predictions

    return df


st.title("Spam Detection Dashboard")

tab1, tab2, tab3 = st.tabs(
    [
        "Single Prediction",
        "Bulk Detection",
        "Dataset Preview"
    ]
)

with tab1:

    st.subheader("Message Analysis")

    message = st.text_area(
        "Enter Message",
        height=200
    )

    if st.button("Analyze Message"):

        result = predict_message(message)

        if result is None:
            st.warning("Please enter a message")

        else:

            prediction, probability = result

            if prediction == "spam":
                st.error("SPAM DETECTED")
            else:
                st.success("HAM MESSAGE")

            st.metric(
                "Confidence",
                f"{probability*100:.2f}%"
            )

with tab2:

    st.subheader("Bulk CSV Detection")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        if st.button("Detect Spam"):

            result_df = batch_predict(uploaded_file)

            st.dataframe(
                result_df,
                use_container_width=True
            )

            csv = result_df.to_csv(index=False)

            st.download_button(
                "Download Results",
                csv,
                "predictions.csv",
                "text/csv"
            )

with tab3:

    st.subheader("Dataset Preview")

    df = pd.read_csv("spam.csv")

    st.dataframe(
        df.head(100),
        use_container_width=True
    )

    st.write("Total Records:", len(df))
    st.write("Spam Messages:", len(df[df["label"] == "spam"]))
    st.write("Ham Messages:", len(df[df["label"] == "ham"]))