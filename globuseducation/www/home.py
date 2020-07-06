import frappe

def get_context(context):
    # context['custom1'] = 'Custom Homepage'
    sliders = frappe.db.get_value("Item")
    frappe.msgprint('sliders... ')
    frappe.msgprint(sliders)
    # context.sliderssss = frappe.db.sql("select image from `tabSlider`")
    # context.marks = frappe.db.sql("select trade_mark_name,image,name from `tabTrade Mark`")
    # context.news = frappe.db.sql("select title,image,subject,name from `tabNews`")