from models.train_model import train_model
import schedule
import time

def retrain():
    print("Retraining model...")
    train_model()
    print("Retraining complete.")

# Schedule retraining every week
schedule.every().week.do(retrain)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)