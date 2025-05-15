import xmlrpc.client

url = "http://localhost:8069"
username = "admin"
password = "admin"
db = "odoo17mate"


common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
print(common.version())

user_ids = common.authenticate(db, username, password, {})
print(user_ids)

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')
patients = models.execute_kw(db, user_ids, password, 'hospital.patient', 'search_read', [], {'fields': ['name']} )
print(f'PATIENTS >>>> {patients}')

patient_ids = models.execute_kw(db, user_ids, password, 'hospital.patient', 'search', [[]] )
print(f'PATIENT IDS >>>> {patient_ids}')

patient_counts = models.execute_kw(db, user_ids, password, 'hospital.patient', 'search_count', [[]] )
print(f'PATIENT COUNT >>>> {patient_counts}')


create_patient = models.execute_kw(db, user_ids, password, 'hospital.patient', 'create', [{'name': 'John', 'gender': 'male', 'date_of_birth': '2000-01-01'}] )
print(f'create patient >>>> {create_patient}')

write_patient = models.execute_kw(db, user_ids, password, 'hospital.patient', 'write', [create_patient, {'name': 'Jane'}] )
print(f'write patient >>>> {write_patient}')

unlink_patient = models.execute_kw(db, user_ids, password, 'hospital.patient', 'unlink', [[31]] )
print(f'unlink patient >>>> {unlink_patient}')