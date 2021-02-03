frappe.ui.form.on('Sales Order', {
	setup(frm) {
		// your code here
// 		frm.page.remove_inner_button(__("Pick List"))
setTimeout(function(){ 		frm.page.remove_inner_button('Pick List', "Create");
frm.add_custom_button(__('Pick List'), () => {
frappe.model.open_mapped_doc({
    method: "picklist_customization.api.create_pick_list",
    frm: frm
})
}, __('Create'));}, 1000);
        console.log('custom')

	}
})