from models import models
from handlers import vmhandler
# from handlers import instancehandler
# from threading import Thread
# from handlers import networkhandler


def main():

    vm = models.VM_Model('upbeat-medley-184111', 'us-central1-f',
                         'instance-1', None)

    vmhandler.get_vm_ips(vm.project, vm.zone)
    print(vmhandler.get_list_vmmodels())


if __name__ == '__main__':
    main()
