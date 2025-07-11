import pandas as pd
import csv

# Sample Nigerian-style scam + safe messages
data = [
    # Smishing (SMS-based scams)
    ("Your NIN has been blocked. Click here to update immediately: http://bit.ly/nin-update", "smishing"),
    ("GTBank Alert: Your account has been locked. Verify now at secure-gtbnigeria.com", "smishing"),
    ("You won N2,000,000 in the Dangote Promo! Send your account details to 080XXXXXXX", "smishing"),
    ("Dear customer, upgrade your SIM registration now to avoid disconnection. Click: simupdate.ng", "smishing"),
    
    # Phishing (email-based scams)
    ("Dear user, your PayPal account has been limited. Log in now to restore access: fake-paypal.com", "phishing"),
    ("UBA: We noticed suspicious activity. Please confirm your identity: uba-ng.com/verify", "phishing"),
    ("You have a pending package. Pay N500 to release it: nigeria-post.com", "phishing"),
    ("Apple ID suspended. Click to reactivate now: apple.com.fake.ng", "phishing"),
    
    # Safe messages
    ("Hey, don’t forget our meeting at 3PM today.", "safe"),
    ("Your Airtime Recharge of N500 was successful. Thank you for using our service.", "safe"),
    ("Welcome to 3MTT! Your training starts on Monday. Details will be shared soon.", "safe"),
    ("GTBank: Your account balance is N23,450. Use our app for quick transfers.", "safe"),
]

# Create DataFrame
df = pd.DataFrame(data, columns=["message", "label"])

# Save to CSV with proper quoting to avoid parser errors
dataset_path = "data/scam_dataset.csv"
df.to_csv(dataset_path, index=False, quoting=csv.QUOTE_ALL)

print(f"Dataset saved to {dataset_path}")