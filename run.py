from app.app import app
import schedule
import time
import threading
from models.update import update_database


def job_manager():
    schedule.every().day.at("23:00").do(update_database())
    while True:
        schedule.run_pending()
        time.sleep(1)


thread_0 = threading.Thread(target=job_manager)
thread_0.start()

if __name__ == "__main__":
    app.run()
