import frappe

@frappe.whitelist(allow_guest=True)
def get_all_events():
    events = frappe.get_all(
        "Home Gallery",
        fields=["name", "title", "category", "year", "main_image", "order_id"],
        order_by="order_id asc"
    )

    # Convert image paths to full URLs
    for event in events:
        if event.get("main_image"):
            event["main_image"] = frappe.utils.get_url(event["main_image"])

    return events
