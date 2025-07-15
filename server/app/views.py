from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

from . import appbuilder, db
from .models import Category


class BaseModelView(ModelView):
    show_template = 'appbuilder/general/model/show_cascade.html'
    edit_template = 'appbuilder/general/model/edit_cascade.html'
    
    edit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
    add_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']

    list_columns = ['id', 'active', 'created_by','created_on', 'changed_by','changed_on']


class CategoryModelView(BaseModelView):
    datamodel = SQLAInterface(Category)

    list_columns = BaseModelView.list_columns + ['name']
    

appbuilder.add_view(
    CategoryModelView,
    "Categories",
    icon="fa-folder-open-o",
    category="Management",
    category_icon='fa-envelope'
)

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
