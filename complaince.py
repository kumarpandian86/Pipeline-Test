import requests
import json
import time
f = open('complaince_config.json')
config_dict = json.load(f)
def get_summary(job_number):
    f = open('complaince_config.json')
    config_dict = json.load(f)
    user_name = config_dict['username']
    auth_token = config_dict['auth_token']

    url = "https://api-discover.corestack.io/compliance/compliance_control_mapping/assessment_summary_by_job?assessment_job_number="+str(job_number)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Auth-User": user_name[0],
        "X-Auth-Token": auth_token
    }

    response = requests.request("GET", url, headers=headers)
    final_output = json.loads(response.text)

    if final_output.get('status') == 'success' and final_output.get('assessment_job_status') == 'COMPLETED':
        return final_output
    elif final_output.get('status') == 'success' and final_output.get('assessment_job_status') == 'IN_PROGRESS':
        print(final_output)
        time.sleep(5)
        get_summary(job_number)
    else:
        return final_output


def  complaince_job():
    f = open('complaince_config.json')
    config_dict = json.load(f)

    tenant = config_dict['tenants']
    user_name = config_dict['username']
    auth_token = config_dict['auth_token']
    payload = config_dict['payload']

    url = "https://api-discover.corestack.io/compliance/"+str(tenant[0])+"/control_mapping/on_demand_execute_standard"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-Auth-User": user_name[0],
        "X-Auth-Token": auth_token
    }

    response = requests.request("POST", url, json=payload, headers=headers)

    final_output = json.loads(response.text)

    return final_output

res= complaince_job()
#res={}                                                                               
#final_summary=get_summary('NIST-SP800-53/0006/46abf502-c017-417c-afe8-9aff0376ea98') 
#print(final_summary)                                                                 

if res.get('status') =='success' :
    print('CA triggered')
    cloud_acc=config_dict['payload']['cloud_accounts'][0]
    job_number=res['assessment_jobs_by_account'][cloud_acc]
    print(job_number)
    final_summary=get_summary(job_number)
    print(final_summary)
