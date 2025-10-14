import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def submit_admission(student_name, email, phone_number, message):
    frappe.local.flags.ignore_csrf = True  
    try:
        # Create Admission document without specifying 'name' so Frappe auto-generates it
        admission_doc = frappe.get_doc({
            "doctype": "Admission",
            "student_name": student_name,
            "email": email,
            "phone_number": phone_number,
            "message": message
        })
        admission_doc.insert(ignore_permissions=True)
        frappe.db.commit()

        # Send email notification
        subject = "New Admission Submitted"
        message_content = f"""
A new admission has been submitted:

Student Name: {student_name}
Email: {email}
Phone Number: {phone_number}
Message: {message}
"""
        frappe.sendmail(
            recipients=["bhumikanarayana1@gmail.com"],
            subject=subject,
            message=message_content
        )

        return {"status": "success", "message": "Admission submitted successfully."}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Admission Submission Error")
        return {"status": "error", "message": str(e)}
