# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "globuseducation"
app_title = "Globus Education"
app_publisher = "Biswajit Sahoo"
app_description = "Education Themes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "biswa@techlift.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = [
    # "/assets/globuseducation/css/globus.css",
    # "/assets/globuseducation/css/skin-blue.css",
    # "/assets/globuseducation/css/custom.css",
    # "/assets/globuseducation/css/temp.css",
]
app_include_js = [
    # "/assets/globuseducation/js/globus.js",
    # "/assets/globuseducation/js/custom.js",
    # "/assets/js/globus-template.min.js",
]
# app_include_css = "/assets/globuseducation/css/globuseducation.css"
# app_include_js = "/assets/globuseducation/js/globuseducation.js"

# include js, css files in header of web template
web_include_css = "/assets/globuseducation/css/globus-web.css"
# web_include_js = "/assets/globuseducation/js/globuseducation.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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
# get_website_user_home_page = "globuseducation.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "globuseducation.install.before_install"
# after_install = "globuseducation.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "globuseducation.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"globuseducation.tasks.all"
# 	],
# 	"daily": [
# 		"globuseducation.tasks.daily"
# 	],
# 	"hourly": [
# 		"globuseducation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"globuseducation.tasks.weekly"
# 	]
# 	"monthly": [
# 		"globuseducation.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "globuseducation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "globuseducation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "globuseducation.task.get_dashboard_data"
# }

