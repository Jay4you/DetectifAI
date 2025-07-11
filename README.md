<img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/42ebf942-ec96-43d3-91af-35bd9fe496dd" />


# DetectifAI

DetectifAI is an AI-powered tool that helps identify phishing, smishing, and safe messages. It is trained specifically on Nigerian-style scam messages, including common SMS and email-based fraud.

Whether it's a fake bank alert, a fraudulent NIN update message, or a suspicious promotional link, DetectifAI is designed to help users quickly identify and avoid potential scams.

---

## Current Features

- Detects phishing (email-based scams)
- Detects smishing (SMS-based scams)
- Flags legitimate/safe messages
- Built with a machine learning model trained on real Nigerian scam data
- Web interface using Streamlit (no installation required for end users once hosted)

---

## Planned Features

These features are planned for future development:

- Confidence scores showing how likely a message is to be a scam
- File legitimacy checks (e.g. scan attachments or linked files)
- Batch scanning through CSV upload or pasted message lists
- Advanced natural language processing for better prediction accuracy
- Scam URL lookup using external threat intelligence APIs
- Summary dashboard showing scam statistics and usage trends
- API endpoints for third-party integrations
- Mobile SMS app integration:
  - Scan incoming text messages in real time
  - Flag smishing attempts with warning alerts
  - Optionally run detection offline using an embedded version of the model

---

## Project Structure

    DetectifAI/
    ├── app.py # Streamlit user interface
    ├── train_model.py # Model training script
    ├── generate_dataset.py # Dataset creation script
    ├── requirements.txt # Python dependencies
    ├── data/
    │ └── scam_dataset.csv # Sample labeled messages
    ├── model/
    │ └── scam_model.pkl # Trained model file
    └── venv/ # Python virtual environment


---

## Getting Started

To run DetectifAI locally:

### 1. Clone the repository
    git clone https://github.com/Jay4you/DetectifAI.git
    cd DetectifAI

### 2. Set up a virtual environment
    python3 -m venv venv
    source venv/bin/activate

### 3. Install dependencies
    pip install -r requirements.txt

### 4. Run the app
    streamlit run app.py

Then open the URL shown in your terminal (typically http://localhost:8501) in your browser.

## Sample Messages
- Safe:
Your Airtime Recharge of N500 was successful.

- Phishing:
-- UBA: We noticed suspicious activity. Please confirm your identity: uba-ng.com/verify
-- Apple ID suspended. Click to reactivate now: apple.com.fake.ng

- Smishing:
-- Your NIN has been blocked. Click here to update: http://bit.ly/nin-update
-- You won N2,000,000 in the Dangote Promo! Send your account details.

## Why This Matters
Scam messages in Nigeria are becoming increasingly sophisticated.
Common tactics include:

- Fake BVN/NIN update links
- SMS from spoofed telecoms or banks
- Phishing emails demanding credentials
- Fake promotions and job offers

DetectifAI is trained on examples of these scams to help users identify and avoid them.

## Deployment
The project is being prepared for hosting on Streamlit Cloud. Once deployed, users will be able to access it from a browser without installing anything locally.

## Contributions
Contributions are welcome. You can contribute by:

- Suggesting or adding real-world scam message examples
- Improving the model
- Enhancing the user interface or backend
- Reporting bugs or submitting feature requests

## License
This project is licensed under the MIT License.

## Technologies Used
Python
scikit-learn
pandas
Streamlit
joblib
