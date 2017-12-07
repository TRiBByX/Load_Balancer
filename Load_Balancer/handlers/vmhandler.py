# import requests
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build
from models import models


dict_of_ips = {}


def start_vm(vm_model):
    """"Starts the VM based on the model given
        args vm_model:
        project: vm project location
        zone: vm zone location
        instance: name of the instance
        ip: can be null
    """
    
    credentials = GoogleCredentials.get_application_default()
    compute = build('compute', 'v1', credentials=credentials)

    # r = compute.instances().reset
    try:
        compute.instances().start(project=vm_model.project,
                                  zone=vm_model.zone,
                                  instance=vm_model.instance).execute()

        data = compute.instances().get(project=vm_model.project,
                                       zone=vm_model.zone,
                                       instance=vm_model.instance).execute()
    except Exception as e:
        raise e
    print('It worked!')
    vm_model.ip = (data.get('networkInterfaces')[0]
                       .get('accessConfigs')[0]
                       .get('natIP'))
    print(vm_model.ip)


def stop_vm(vm_model):
    """"Stops the VM based on the model given
        args: vm_model:
            project: vm project location
            zone: vm zone location
            instance: name of the instance
            ip: can be null
    """
    credentials = GoogleCredentials.get_application_default()
    compute = build('compute', 'v1', credentials=credentials)

    # r = compute.instances().reset
    try:
        compute.instances().stop(project=vm_model.project,
                                 zone=vm_model.zone,
                                 instance=vm_model.instance).execute()
        print("VM stopped")
    except Exception as e:
        raise e


def get_vm_ips(project, zone):
    """Populates dict of ips based on project and zone.

        args:
            project: the vm project location
            zone: the vms zone
    """
    credentials = GoogleCredentials.get_application_default()
    compute = build('compute', 'v1', credentials=credentials)
    dict_of_ips.clear()
    # r = compute.instances().reset
    try:
        ips = compute.instances().list(project=project, zone=zone)
        while ips is not None:
            response = ips.execute()
            for instance in response['items']:
                data = instance.get('selfLink')
                data = data.split("/")
                data_vm_model = str((models.VM_Model(data[6], data[8],
                                    instance.get('name'),
                                    instance.get('networkInterfaces')[0]
                                            .get('accessConfigs')[0]
                                            .get('natIP'))))                                            
                dict_of_ips[instance.get('name')] = data_vm_model
            ips = compute.instances().list_next(previous_request=ips,
                                                previous_response=response)
    except Exception as e:
        raise e
    pass

def get_ip_dict():
    """Returns dict of ips.

    Use get_vm_ips to populate it.
    """

    return dict_of_ips
