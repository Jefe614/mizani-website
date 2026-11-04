import frappe


LOGO_URL = "/assets/mizani_site/images/logo.svg"


def after_install():
	settings = frappe.get_single("Website Settings")
	if not settings.app_logo:
		settings.app_logo = LOGO_URL
		settings.save(ignore_permissions=True)
