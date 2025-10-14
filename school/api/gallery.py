# school/school/api/gallery.py
import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_gallery_images():
    """
    Returns all published and active gallery images as JSON
    """
    images = frappe.get_all(
        "Gallery Item",
        filters={
            "published": 1,
            "is_active": 1  # only active images
        },
        fields=["name", "image"],
        order_by="creation desc"
    )
    
    # Optionally, prepend the site URL to the image path
    site_url = frappe.utils.get_url()
    for img in images:
        img["image"] = site_url + img["image"]
    
    return images
