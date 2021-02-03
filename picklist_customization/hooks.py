# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "picklist_customization"
app_title = "Picklist Customization"
app_publisher = "Bhavesh Maheshwari"
app_description = "Pick list customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "maheshwaribhavesh95863@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/picklist_customization/css/picklist_customization.css"
# app_include_js = "/assets/picklist_customization/js/picklist_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/picklist_customization/css/picklist_customization.css"
# web_include_js = "/assets/picklist_customization/js/picklist_customization.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Order" : "public/js/sales_order.js",
    "Pick List" : "public/js/pick_list.js"
}

fixtures = [
	{
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
			"Pick List-rush",
			"Pick List-is_rush",
			"Sales Order-is_rush"
		]
	   ]
	]
    }
]
# doctype_js = {"Pick List" : "public/js/pick_list.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "picklist_customization.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "picklist_customization.install.before_install"
# after_install = "picklist_customization.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "picklist_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Pick List": {
		"before_save": "picklist_customization.api.before_save_update"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"picklist_customization.tasks.all"
# 	],
# 	"daily": [
# 		"picklist_customization.tasks.daily"
# 	],
# 	"hourly": [
# 		"picklist_customization.tasks.hourly"
# 	],
# 	"weekly": [
# 		"picklist_customization.tasks.weekly"
# 	]
# 	"monthly": [
# 		"picklist_customization.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "picklist_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "picklist_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "picklist_customization.task.get_dashboard_data"
# }

