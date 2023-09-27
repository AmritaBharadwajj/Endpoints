from fastapi import APIRouter

from api.google_workspace.service.gw_query import GoogleWorkspaceQuery

router = APIRouter()

@router.post("/google/query/{service_name}/version/{version_name}", tags=["query"])
async def read_users(service_name, version_name):
    return GoogleWorkspaceQuery(service_name, version_name, 'drive').query()

@router.post("/google/drive/reports", tags=["google_workspace"])
async def drive_reports():
    return GoogleWorkspaceQuery('admin', 'reports_v1', 'drive').get_drive_reports()

#Endpoint for login logs 
@router.post("/google/query/{service_name}/version/{version_name}", tags=["query"])
async def read_users(service_name, version_name):
    return GoogleWorkspaceQuery(service_name, version_name, 'admin').query()
   # return GoogleWorkspaceQuery(service_name, version_name, 'audit').query()
#Here within  the return function not sure admin/audit parameter should be taken as I have seen different on different sources 
#same thingn for the following admin logs 

@router.post("/google/admin/audit/login",tags=["google_workspace"])
async def login_reports():
    return GoogleWorkspaceQuery('admin','reports_v1', 'audit').get_login_reports()
    

#Endpoint for admin logs
@router.post("/google/query/{service_name}/version/{version_name}", tags=["query"])
async def read_users(service_name, version_name):
    return GoogleWorkspaceQuery(service_name, version_name, 'admin').query()
    #return GoogleWorkspaceQuery(service_name, version_name, 'audit').query()


@router.post("/google/admin/activity/users",tags=["google_workspace"])
async def login_reports():
    return GoogleWorkspaceQuery('admin', 'reports_v1', 'activity').get_audit_reports()



# @router.post("/google/login/reports", tags=["google_workspace"])
# async def drive_reports():
#     return GoogleWorkspaceQuery('admin', 'reports_v1', 'login').query()
