def resolve_mizani_path(path: str) -> str:
	if not path:
		return "index"

	from frappe.website.path_resolver import resolve_path

	return resolve_path(path)
