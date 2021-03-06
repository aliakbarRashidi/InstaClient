import schedule
import time
import datetime
from tkinter import messagebox
from UserDetails import UserDetails
from UserPostDetails import UserPostDetails


class ClientScheduler:
    def __init__(self, time1, proxyPath, filesPath, credentials):
        self.time1 = time1
        self.proxyPath = str(proxyPath.get().strip())
        self.filesPath = str(filesPath.get().strip())
        self.credentials = credentials
        self.clientStartedTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                            "%Y-%m-%d %H:%M:%S")
        self.clientEndingTime = datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                           "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=24)

    def job(self):
        upd = UserPostDetails()
        upd.userPostDetails(self.credentials, self.clientStartedTime, self.clientEndingTime, self.filesPath)
        print('Executed the job!')

    def jobScheduler(self, timeToRun, job):
        print('Scheduler started!')
        #schedule.every(timeToRun).seconds.do(job)
        schedule.every(timeToRun).minutes.do(job)
        # schedule.every().hour.do(job)
        # schedule.every().day.at("10:30").do(job)

        count = 0
        while 1:
            schedule.run_pending()
            time.sleep(1)
            if self.clientEndingTime <= datetime.datetime.now():
                self.generateFollowers()
                messagebox.showinfo("Info", "Finished Data Collecting")
                break
            count = count + 1

    def schedulerInitialize(self):
        self.jobScheduler(int(self.time1.get().strip()), self.job)

    def job_that_executes_once(self):
        return schedule.CancelJob

    def generateFollowers(self):
        ud = UserDetails()
        ud.getTotalFollowers(self.credentials, self.filesPath)
