from models import models
from handlers import vmhandler
from handlers import instancehandler
from threading import Thread
from handlers import networkhandler


def main():

    vm = models.VM_Model('upbeat-medley-184111', 'us-central1-f',
                         'instance-1', None)

    vmhandler.get_vm_ips(vm.project, vm.zone)
<<<<<<< HEAD

    tcp_thread = Thread(target=instancehandler.instanceLoop)
    network_thread = Thread(target=networkhandler.serve)

    tcp_thread.start()
    #network_thread.start()
=======
    print(vmhandler.get_list_vmmodels())
>>>>>>> fd6179ebf11a2cdb3064962269fe5d3d4a6ba6ea


if __name__ == '__main__':
    main()
