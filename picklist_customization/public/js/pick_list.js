frappe.ui.form.on('Pick List', {
	refresh(frm,cdt,cdn) {
		console.log("***##")
		// your code here
		let locations = frm.get_field("locations").grid;
		locations.toggle_enable("warehouse", true);
		if(frm.doc.is_rush){
		    let value = "<h2>Rush</h2>"
		    frm.fields_dict.rush.html(value)
		}
		else{
		    frm.fields_dict.rush.html("")
		}
		var table = locals[cdt][cdn].locations
		if(table){
			table.map(item => {
				frappe.call({
					method: "picklist_customization.api.get_warehouse",
					args: {
						"item_code": item.item_code,
						"so": item.sales_order
					},
					async: false,
					callback: function(r){
						if(r.message){
							let data = r.message[0]
							item.warehouse = data.warehouse
						}
					}
				})

			})
			frm.refresh_field('locations')
		}

	},
})

