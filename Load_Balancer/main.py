from models import models
from handlers import vmhandler
from handlers import instancehandler


def main():
    vm_ips = list()
    vm = models.VM_Model('upbeat-medley-184111', 'us-central1-f',
                         'instance-1', None)

    vmhandler.get_vm_ips(vm.project, vm.zone, vm_ips)
    print(vm_ips)

if __name__ == '__main__':
    main()
