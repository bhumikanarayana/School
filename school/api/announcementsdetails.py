import frappe

@frappe.whitelist(allow_guest=True)
def get_announcement_details(name=None):
    if not name:
        frappe.throw("No announcement name provided")

    try:
        announcement = frappe.get_doc("Announcements", name)
    except frappe.DoesNotExistError:
        frappe.throw(f"Announcement '{name}' not found")
    except Exception as e:
        frappe.throw(f"Error fetching announcement: {str(e)}")

    return {
        "name": announcement.name,
        "title": announcement.title,
        "icon": frappe.utils.get_url(announcement.icon) if announcement.icon else "",
        "date": announcement.date.strftime("%Y-%m-%d") if announcement.date else "",
        "about": announcement.about,
        "show_know_more": getattr(announcement, "show_know_more", 0),
        "more_content": getattr(announcement, "more_content", "")
    }
