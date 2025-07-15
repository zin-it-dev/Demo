from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelRestApi

from . import appbuilder, db
from .models import Category


class CategoryModelApi(ModelRestApi):
    resource_name = 'categories'
    datamodel = SQLAInterface(Category)
    allow_browser_login = True
    exclude_route_methods = ['get', 'info', 'post', 'put', 'delete']
    
    openapi_spec_methods = {
        "get_list": {
            "get": {
                "description": "Get all categories",
            }
        }
    }

appbuilder.add_api(CategoryModelApi)

