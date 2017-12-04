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


def stop_vm(vm_model):
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


def get_vm_ips(project, zone, list_of_ips):
    credentials = GoogleCredentials.get_application_default()
    compute = build('compute', 'v1', credentials=credentials)
    del list_of_ips[:]
    # r = compute.instances().reset
    try:
        ips = compute.instances().list(project=project, zone=zone)
        while ips is not None:
            response = ips.execute()
            for instance in response['items']:
                list_of_ips.append(instance
                                   .get('networkInterfaces')[0]
                                   .get('accessConfigs')[0]
                                   .get('natIP'))
            ips = compute.instances().list_next(previous_request=ips,
                                                previous_response=response)
    except Exception as e:
        raise e
    pass
