import frappe
from frappe.utils import get_url

@frappe.whitelist(allow_guest=True)
def get_gallery(name=None):
    if not name:
        frappe.throw("Gallery name is required")

    try:
        doc = frappe.get_doc("Home Gallery", name)
    except frappe.DoesNotExistError:
        frappe.throw("Gallery not found")

    # Prepare the main data
    data = {
        "title": doc.title,
        "description": doc.description,
        "main_image": get_url(doc.main_image) if doc.main_image else None,
        "year": doc.year,
        "category": doc.category,
        "order_id": doc.order_id,
        "games_conducted": [],
        "guests": [],
        "gallery_images": []
    }

    # Games Conducted (if you have child table)
    for game in doc.get("games_conducted") or []:
        data["games_conducted"].append({
            "game_name": game.game_name,
            "winners": game.winners,
            "game_image": [{"image": get_url(game.game_image)}] if game.game_image else [],
            "winners_image": [{"image": get_url(game.winners_image)}] if game.winners_image else []
        })

    # Guests (if you have child table)
    for guest in doc.get("guests") or []:
        data["guests"].append({
            "guest_name": guest.guest_name,
            "designation": guest.designation,
            "photo": get_url(guest.photo) if guest.photo else None
        })

    # Gallery Images (if you have child table)
    # Gallery Images
    for img in doc.get("gallery_images") or []:
        data["gallery_images"].append({
            "image": get_url(img.image),
            "published": img.published  # use the correct field name
        })


    return data
