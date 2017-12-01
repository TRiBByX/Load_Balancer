class VM_Model(object):
    """docstring for VM_Model"""
    def __init__(self, project, zone, instance, ip):
        super(VM_Model, self).__init__()
        self.project = project
        self.zone = zone
        self.instance = instance
        self.ip = ip
