import streamlit as st
from streamlit_lottie import st_lottie
import json

def app():
    path = "Animation - 1714286329037.json"

    # Load the animation JSON from the file
    with open(path, "r") as file:
        animation_json = json.load(file)

    st_lottie(animation_json,width=None,height=None )
            
    st.markdown("""
    <style>
    .main {
        padding: 20px;
        color: var(--text-color);
        background-color: var(--background-color);
    }
    .title {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 30px;
        color: var(--title-color);
    }
    .section-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
        color: var(--section-title-color);
    }
    .content {
        font-size: 18px;
        color: var(--content-color);
    }
    .highlight {
        background-color: var(--highlight-background-color);
        padding: 15px;
        border-radius: 10px;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main">', unsafe_allow_html=True)

    st.markdown('<div class="highlight">It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items that they did not purchase. To achieve this, credit card fraud detection systems utilize various techniques, including machine learning.</div>', unsafe_allow_html=True)

    st.markdown('<div class="title">How Credit Card Fraud Detection Works</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Pattern Recognition</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">The system analyzes your spending patterns and behaviors over time. It looks at factors such as the frequency of transactions, typical purchase amounts, locations where purchases are made, and the types of merchants you usually transact with.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Anomaly Detection</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Any transaction that deviates significantly from your normal behavior is flagged as potentially fraudulent. For example, a large purchase made in a foreign country or at an unusual time of day may trigger suspicion.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Machine Learning Algorithms</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Many fraud detection systems use machine learning algorithms to continually improve their ability to identify fraudulent activity. These algorithms analyze vast amounts of transaction data to detect subtle patterns and trends associated with fraudulent behavior. In this system, CatBoost and XGBoost are utilized for their effectiveness in handling categorical features and handling imbalanced data, respectively.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Real-time Monitoring</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Transactions are monitored in real-time as they occur. If a transaction is flagged as suspicious, the system may temporarily freeze the card or require additional verification from the cardholder before approving the transaction.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Geolocation and Device Identification</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">The system may use geolocation data and device identification techniques to verify the legitimacy of transactions. For example, if a transaction originates from a location far from your usual whereabouts or is made from an unrecognized device, it may raise a red flag.</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="section-title">Customer Verification</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">In cases where a transaction is flagged as potentially fraudulent, the credit card company may contact the cardholder through various channels (e.g., phone call, text message, email) to verify the transaction\'s authenticity. This may involve confirming details about recent transactions or providing a one-time password for authentication.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


if __name__ == '__main__':
    app()
