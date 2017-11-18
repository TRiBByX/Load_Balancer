# import requests
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build


def start_vm():
    credentials = GoogleCredentials.get_application_default()
    compute = build('compute', 'v1', credentials=credentials)

    # r = compute.instances().reset

    print(compute.instances().start(project='upbeat-medley-184111',
                                    zone='us-central1-f',
                                    instance='instance-1').execute())

    # print(compute.instances().list(project='upbeat-medley-184111',
    #                                zone='us-central1-f').execute())
    # r = requests.post('https://www.googleapis.com/compute/v1/projects/upbeat-medley-184111/zones/us-central1-f/instances/instance-1/stop?access_token={0}'.format(compute))

    pass


def stop_vm():
    pass


def get_vm_ips():
    pass


start_vm()
