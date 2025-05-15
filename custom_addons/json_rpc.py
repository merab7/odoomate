import requests
import json

url = "http://localhost:8069"
username = "admin"
password = "admin"
db = "odoo17mate"

# Create a session to maintain cookies
session = requests.Session()

def json_rpc(url, method, params):
    data = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": params,
        "id": None,
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = session.post(url, data=json.dumps(data), headers=headers)
    return response.json()

# Authenticate and get user id
auth_params = {
    "db": db,
    "login": username,
    "password": password,
}
uid = json_rpc(f"{url}/web/session/authenticate", "call", auth_params)
if not uid.get('result'):
    raise Exception("Authentication failed")

# Get version info
version_info = json_rpc(f"{url}/web/webclient/version_info", "call", {})
print(version_info)

# Search and read patients
params = {
    "args": [],
    "kwargs": {
        "context": {"lang": "en_US"},
        "domain": [],
        "fields": ["name"],
    },
    "model": "hospital.patient",
    "method": "search_read",
}
patients = json_rpc(f"{url}/web/dataset/call_kw/hospital.patient/search_read", "call", params)
print(f'PATIENTS >>>> {patients}')

# Search patient ids
params = {
    "args": [[]],
    "kwargs": {
        "context": {"lang": "en_US"},
    },
    "model": "hospital.patient",
    "method": "search",
}
patient_ids = json_rpc(f"{url}/web/dataset/call_kw/hospital.patient/search", "call", params)
print(f'PATIENT IDS >>>> {patient_ids}')

# Count patients
params = {
    "args": [[]],
    "kwargs": {
        "context": {"lang": "en_US"},
    },
    "model": "hospital.patient",
    "method": "search_count",
}
patient_counts = json_rpc(f"{url}/web/dataset/call_kw/hospital.patient/search_count", "call", params)
print(f'PATIENT COUNT >>>> {patient_counts}')

# Create patient
params = {
    "args": [{
        "name": "John",
        "gender": "male",
        "date_of_birth": "2000-01-01"
    }],
    "kwargs": {
        "context": {"lang": "en_US"},
    },
    "model": "hospital.patient",
    "method": "create",
}
create_patient = json_rpc(f"{url}/web/dataset/call_kw/hospital.patient/create", "call", params)
print(f'create patient >>>> {create_patient}')

if create_patient.get('result'):
    # Update patient
    params = {
        "args": [[create_patient['result']], {"name": "Jane"}],
        "kwargs": {
            "context": {"lang": "en_US"},
        },
        "model": "hospital.patient",
        "method": "write",
    }
    write_patient = json_rpc(f"{url}/web/dataset/call_kw/hospital.patient/write", "call", params)
    print(f'write patient >>>> {write_patient}')

# Delete patient (using ID 31 as an example)
params = {
    "args": [[31]],
    "kwargs": {
        "context": {"lang": "en_US"},
    },
    "model": "hospital.patient",
    "method": "unlink",
}
unlink_patient = json_rpc(f"{url}/web/dataset/call_kw/hospital.patient/unlink", "call", params)
print(f'unlink patient >>>> {unlink_patient}')