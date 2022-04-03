from fastapi import APIRouter


router_hsi = APIRouter(
    # prefix="/hsi/api/v1",
    prefix="/portalpaciente/api/v1",
    responses={404: {"description": "Not Found"}}
)


router_local = APIRouter(
    # prefix="/hsi/api/v1",
    prefix="/portalpaciente/api/v1",
    responses={404: {"description": "Not Found"}}
)

router_admin = APIRouter(
    tags=["Admin"],
    prefix="/portalpaciente/api/v1/admin",
    responses={404: {"description": "Not Found"}}
)

