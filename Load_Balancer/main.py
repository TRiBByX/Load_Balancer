from models import models
from handlers import vmhandler
from handlers import instancehandler
from threading import Thread
import time


def main():
    vm = models.VM_Model('upbeat-medley-184111', 'us-central1-f',
                         'instance-1', None)

    
    time_thread = Thread(target=timer)
    time_thread.start()

    tcp_thread = Thread(target=instancehandler.instanceLoop)
    tcp_thread.start()


def timer():
    print('time!')
    time.sleep(5)
    print('time! + 5')

if __name__ == '__main__':
    main()
