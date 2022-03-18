from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, grade, nationality_sap,\
    nationality, nationality_gender, military_service_attitude, marital_status, staff_unit_type,\
    staff_category, organization_unit_type, order_type, order_change_type, employee_status, position

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(grade.router, prefix="/grade", tags=["grade"])
api_router.include_router(nationality_sap.router, prefix="/nationality-sap", tags=["nationality-sap"])
api_router.include_router(nationality.router, prefix="/nationality", tags=["nationality"])
api_router.include_router(nationality_gender.router, prefix="/nationality-gender", tags=["nationality-gender"])
api_router.include_router(military_service_attitude.router, prefix="/military-service-attitude", tags=["military-service-attitude"])
api_router.include_router(marital_status.router, prefix="/marital-status", tags=["marital-status"])
api_router.include_router(staff_unit_type.router, prefix="/staff-unit-type", tags=["staff-unit-type"])
api_router.include_router(staff_category.router, prefix="/staff-category", tags=["staff-category"])
api_router.include_router(organization_unit_type.router, prefix="/organization-unit-type", tags=["organization-unit-type"])
api_router.include_router(order_type.router, prefix="/order-type", tags=["order-type"])
api_router.include_router(order_change_type.router, prefix="/order-change-type", tags=["order-change-type"])
api_router.include_router(employee_status.router, prefix="/employee-status", tags=["employee-status"])
api_router.include_router(position.router, prefix="/position", tags=["position"])