from app.core.security import get_password_hash, verify_password
from app.crud.base import CRUDBase, UpdateSchemaType
from app.models.model_user import DepartmentModel
from app.schemas.schemas_user import DepartmentSchemas, DepartmentCreate, DepartmentUpdate
from sqlalchemy.orm import Session


# 控制器


class CRUDDepartment(CRUDBase[DepartmentModel, DepartmentCreate, DepartmentUpdate]):

    def get_department_users(self, db: Session, id):
        pass


crud_department = CRUDDepartment(DepartmentModel)
