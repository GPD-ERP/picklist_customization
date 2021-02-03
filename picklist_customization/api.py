from __future__ import unicode_literals
import frappe
import json
from six import iteritems
from frappe.model.document import Document
from frappe import _
from collections import OrderedDict
from frappe.utils import floor, flt, today, cint
from frappe.model.mapper import get_mapped_doc, map_child_doc
from erpnext.stock.get_item_details import get_conversion_factor
from erpnext.selling.doctype.sales_order.sales_order import make_delivery_note as create_delivery_note_from_sales_order

@frappe.whitelist()
def before_save_update(self,method):
	setting = frappe.get_doc("Pick List Cutomization Setting","Pick List Cutomization Setting")
	if not setting.warehouse:
		frappe.throw(_("Set Warehouse In Pick List Customization Setting"))
	if frappe.db.get_value("Warehouse",self.parent_warehouse,"is_group") == 0:
		for row in self.get('locations'):
			w_stock_qty = get_warehouse_stock(setting.warehouse)
			row.warehouse = setting.warehouse
			row.stock_qty = row.stock_qty = row.qty if flt(w_stock_qty) >= flt(row.qty) else w_stock_qty
			row.picked_qty = row.stock_qty
	# self.aggregate_item_qty()
@frappe.whitelist()
def create_pick_list(source_name, target_doc=None):
	def update_item_quantity(source, target, source_parent):
		target.qty = flt(source.qty) - flt(source.delivered_qty)
		target.stock_qty = (flt(source.qty) - flt(source.delivered_qty)) * flt(source.conversion_factor)

	doc = get_mapped_doc('Sales Order', source_name, {
		'Sales Order': {
			'doctype': 'Pick List',
			'validation': {
				'docstatus': ['=', 1]
			}
		},
		'Sales Order Item': {
			'doctype': 'Pick List Item',
			'field_map': {
				'parent': 'sales_order',
				'name': 'sales_order_item'
			},
			'postprocess': update_item_quantity,
			'condition': lambda doc: abs(doc.delivered_qty) < abs(doc.qty) and doc.delivered_by_supplier!=1
		},
	}, target_doc)

	doc.purpose = 'Delivery'

	doc.set_item_locations()
	setting = frappe.get_doc("Pick List Cutomization Setting","Pick List Cutomization Setting")
	if not setting.warehouse:
		frappe.throw(_("Set Warehouse In Pick List Customization Setting"))
	doc.parent_warehouse = setting.warehouse
	if doc.get("locations"):
		for row in doc.get("locations"):
			w_stock_qty = get_warehouse_stock(setting.warehouse)
			row.warehouse = setting.warehouse
			row.stock_qty = row.qty if flt(w_stock_qty) >= flt(row.qty) else w_stock_qty  
			row.picked_qty = row.stock_qty
	return doc

def get_warehouse_stock(warehouse):
	bin = frappe.get_all("Bin",filters={"warehouse":warehouse},fields=["actual_qty"])
	if bin:
		return bin[0].actual_qty
	else:
		return 0

@frappe.whitelist()
def get_warehouse(item_code, so):
	query = """select item_code,warehouse from `tabSales Order Item` where item_code = '{0}' and parent='{1}';""".format(item_code,so)
	warehouse = frappe.db.sql(query,as_dict = True)
	return warehouse

