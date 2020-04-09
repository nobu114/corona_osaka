from app.app import app
import schedule
import time
import threading
from models.update import update_database


def job():
    update_database()


def job_manager():
    schedule.every().day.at("23:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    thread_0 = threading.Thread(target=job_manager)
    app.run(debug=True)
    thread_0.start()
