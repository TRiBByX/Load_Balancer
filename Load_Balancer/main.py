from models import models
from handlers import vmhandler
from handlers import instancehandler


def main():
    vm = models.VM_Model('upbeat-medley-184111', 'us-central1-f',
                         'instance-1', None)

    # vmhandler.start_vm(vm)

    instancehandler.instanceLoop()

    # print(vm.ip)


if __name__ == '__main__':
    main()
