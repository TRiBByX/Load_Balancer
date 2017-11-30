# import requests
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

def start_vm(vm_model):
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
    vm_model.ip = data.get('networkInterfaces')[0].get('accessConfigs')[0].get('natIP')
    print(vm_model.ip)


def stop_vm():
    print(vm.project)
    pass


def get_vm_ips():
    pass
