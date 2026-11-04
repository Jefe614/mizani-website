app_name = "mizani_site"
app_title = "Mizani Site"
app_publisher = "Mizani Labs"
app_description = "Branded homepage and login styling for Mizani Labs tenants."
app_email = "dev@example.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "mizani_site",
# 		"logo": "/assets/mizani_site/logo.png",
# 		"title": "Mizani Site",
# 		"route": "/mizani_site",
# 		"has_permission": "mizani_site.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/mizani_site/css/mizani.css"
# app_include_js = "/assets/mizani_site/js/mizani_site.js"

# include js, css files in header of web template
web_include_css = "/assets/mizani_site/css/mizani.css"
# web_include_js = "/assets/mizani_site/js/mizani_site.js"

# App and website branding
app_logo_url = "/assets/mizani_site/images/logo.svg"
website_context = {"splash_image": "/assets/mizani_site/images/logo.svg"}

# Keep the root route on the shared public homepage for Guests and signed-in users.
website_path_resolver = "mizani_site.website.resolve_mizani_path"
after_install = "mizani_site.install.after_install"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mizani_site/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mizani_site/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mizani_site.utils.jinja_methods",
# 	"filters": "mizani_site.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mizani_site.install.before_install"
# after_install = "mizani_site.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mizani_site.uninstall.before_uninstall"
# after_uninstall = "mizani_site.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mizani_site.utils.before_app_install"
# after_app_install = "mizani_site.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mizani_site.utils.before_app_uninstall"
# after_app_uninstall = "mizani_site.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "mizani_site.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mizani_site.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["mizani_site.search.awesomebar_results"]

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mizani_site.tasks.all"
# 	],
# 	"daily": [
# 		"mizani_site.tasks.daily"
# 	],
# 	"hourly": [
# 		"mizani_site.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mizani_site.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mizani_site.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mizani_site.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "mizani_site.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mizani_site.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mizani_site.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mizani_site.utils.before_request"]
# after_request = ["mizani_site.utils.after_request"]

# Job Events
# ----------
# before_job = ["mizani_site.utils.before_job"]
# after_job = ["mizani_site.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mizani_site.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []
