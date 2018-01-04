from models import models
from handlers import vmhandler
from handlers import instancehandler
from threading import Thread
from handlers import networkhandler
import sys


def main():

    vm = models.VM_Model('upbeat-medley-184111', 'us-central1-f',
                         'instance-1', None)

    vmhandler.get_vm_data(vm.project, vm.zone)

    tcp_thread = Thread(target=instancehandler.instanceLoop)
    network_thread = Thread(target=networkhandler.serve)

    tcp_thread.start()
    network_thread.start()

    if raw_input() == 'exit':
        print('trying')
        quit()



if __name__ == '__main__':
    main()
