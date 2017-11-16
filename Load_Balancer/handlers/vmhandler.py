import requests
from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build


def start_vm():
    credentials = GoogleCredentials.get_application_default()
    compute = build('compute', 'v1', credentials=credentials)

    r = requests.post('https://www.googleapis.com/compute/v1/projects/upbeat-medley-184111/zones/us-central1-f/instance-1/reset')

    print(r)

    pass


def stop_vm():
    pass


def get_vm_ips():
    pass


start_vm()
