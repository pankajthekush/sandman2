"""This module contains the custom admin class that allows for a nicer admin
interface."""

# pylint: disable=maybe-no-member,too-few-public-methods

# Third-party imports
from flask_admin.contrib.sqla import ModelView
import getpass
from datetime import datetime
import pytz


class CustomAdminView(ModelView):  # pylint: disable=no-init
    #override aja_update to update username
    
    def on_model_change(self, form, model, is_created):
        #update current user
        curr_user = getpass.getuser()
        model.updatedby = curr_user
        
        #calculate current time
        tz_India = pytz.timezone('Asia/Kolkata')
        datetime_India = datetime.now(tz_India)
        curr_time =  datetime_India.strftime("%D-%M-%Y %H:%M:%S")
        current_user_time_remarks = f'{curr_time} {curr_user} wrote :'

        #update remarks
        current_remarks = f'{current_user_time_remarks} {model.remarks}\n'
        old_remarks = model.rhistory
        model.rhistory = old_remarks + current_remarks

    # def after_model_change(self, form, model, is_created):

    #     model.rhistory = 'history'
    #     print(model.rhistory)
                 


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

  
    

  





