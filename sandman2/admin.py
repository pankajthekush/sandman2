"""This module contains the custom admin class that allows for a nicer admin
interface."""

# pylint: disable=maybe-no-member,too-few-public-methods

# Third-party imports
from flask_admin.contrib.sqla import ModelView
import getpass



class CustomAdminView(ModelView):  # pylint: disable=no-init
    #override aja_update to update username
    def on_model_change(self, form, model, is_created):
        curr_user = getpass.getuser()
        model.updatedby = curr_user
    """Define custom templates for each view."""
    
    ModelView.list_template = 'list.html'
    ModelView.create_template = 'create.html'
    ModelView.edit_template = 'edit.html'
    ModelView.details_template = 'details.html'
    column_display_pk = False
    ModelView.can_export = True
    ModelView.can_delete = False
    ModelView.can_view_details = True
    ModelView.can_set_page_size = True
    ModelView.can_create = False
    ModelView.can_edit = True
    ModelView.page_size = 200
    ModelView.column_editable_list = ['remarks']

  
    

  





