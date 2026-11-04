import frappe


def get_context(context):
	return {
		"mizani_logo": frappe.get_website_settings("app_logo")
		or context.get("splash_image")
		or "/assets/mizani_site/images/logo.svg"
	}
