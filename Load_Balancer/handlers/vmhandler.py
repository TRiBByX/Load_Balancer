# import requests
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

dict_of_ips = {}


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


def get_vm_ips(project, zone):
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
                dict_data = {}
                dict_data['project:'] = data[6]
                dict_data['zone:'] = data[8]
                dict_data['ip'] = (instance.get('networkInterfaces')[0]
                                           .get('accessConfigs')[0]
                                           .get('natIP'))

                dict_of_ips[instance.get('name')] = dict_data
            ips = compute.instances().list_next(previous_request=ips,
                                                previous_response=response)
    except Exception as e:
        raise e
    pass

def get_ip_dict():
    return dict_of_ips
