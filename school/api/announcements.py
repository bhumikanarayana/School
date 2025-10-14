import frappe
@frappe.whitelist(allow_guest=True)
def get_announcements():
    announcements = frappe.get_all(
        "Announcements",
        filters={"published": 1},
        fields=["name", "title", "icon", "about", "date", "show_know_more", "more_content"],
        order_by="date desc"
    )

    result = []
    for ann in announcements:
        result.append({
            "name": ann.name,
            "title": ann.title,
            "icon": frappe.utils.get_url(ann.icon) if ann.icon else "",
            "about": ann.about,
            "date": ann.date.strftime("%Y-%m-%d") if ann.date else "",
            "more": ann.show_know_more,
            "more_content": ann.more_content
        })

    return result  # must return a serializable list/dict
