import yaml
from google.cloud import bigquery
from google.cloud import iam
#from google.cloud import iam_admin

# Load the YAML file
with open('permissions.yaml', 'r') as file:
    permissions = yaml.safe_load(file)

# def principal_exists(principal):
#     """
#     Check if a principal exists in GCP IAM.
#     Returns True if the principal exists, False otherwise.
#     """
#     client = iam_admin.IamAdminServiceClient()

#     try:
#         client.get_service_account(name=principal)
#         return True
#     except Exception as e:
#         print(f'Principal {principal} does not exist: {e}')
#         return False

def add_iam_roles(roles, user_email):
    """Add IAM roles to a user account."""
    # iam_client = iam.IAMCredentialsClient()

    print("IAM roles " + roles)
    print("User: " + user_email)
    # Get the user's unique ID
    # user = iam_client.generate_access_token(name=f"projects/-/serviceAccounts/{user_email}")
    # user_id = user.identity.principal_email.split('@')[0]

    # Add the roles to the user
    # policy = iam_client.get_iam_policy(request={"resource": f"projects/-/serviceAccounts/{user_email}"})
    # binding = policy.bindings.add()
    # binding.role = role
    # binding.members.append(f"user:{user_id}")
    # iam_client.set_iam_policy(request={"resource": f"projects/-/serviceAccounts/{user_email}", "policy": policy})

def add_bigquery_roles(dataset_name, roles, user_email):
    """Add BigQuery data set roles to a user account."""
    # bigquery_client = bigquery.Client()
    print("Dataset: " + dataset_name )
    print("Role " + roles)
    print("User: " + user_email )
    # Get the data set object
    # dataset = bigquery_client.get_dataset(dataset_name)

    # Add the roles to the user
    # entry = bigquery.AccessEntry(
    #    role=role,
    #    entity_type=bigquery.EntityType.USER_EMAIL,
    #    entity_id=user_email
    # )
    # dataset.access_entries.append(entry)

    # Update the data set
    # bigquery_client.update_dataset(dataset, ["access_entries"])

# Iterate through the user accounts and their permissions
for project in permissions['projects']:
    project_id = project['project']
    iam_permissions = project['permissions'].get('iam', None)
    bigquery_permissions = project['permissions'].get('Bigquery', None)

    # if principal_exists(principal):
    #     print(f'Principal {principal} exists')
    # else:
    #     print(f'Principal {principal} does not exist')

    print("")
    print( "- - - - - " + project_id + " - - - - -")
    # Add the IAM roles
    if iam_permissions:
        print("-     Adding IAM permissions     -")
        for permission in iam_permissions:
            add_iam_roles(permission, f"{project_id}@example-project.iam.gserviceaccount.com")
    else:
        print("- No IAM permissions to add -")
    
    print("")
    # Add the BigQuery roles
    if bigquery_permissions:
        print("-   Adding BigQuery permissions   -")
        for permission in bigquery_permissions:
            dataset_name = permission['dataset']
            dataset_roles = permission['permissions']
            for role in dataset_roles:
                add_bigquery_roles(dataset_name, role, f"{project_id}@example-project.iam.gserviceaccount.com")
    else:
        print("- No BigQuery permissions to add -")
