import time
from notifypy import Notify
from DesktopNotifier import topStories

ICON_PATH =r"C:\Users\Deepak Pandya\Documents\Learning\Python\Projects\NewsIcon.png"
newsItems = topStories()

n=Notify()
n.icon=ICON_PATH
n.title="News Notifier"

for news in newsItems:
    n.message=news['description']
    n.title=news['title']
    n.send()
    time.sleep(15)