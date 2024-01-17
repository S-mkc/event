# Copyright (c) 2024, Mukesh  and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	columns =[

		{
            'fieldname': 'TDs Type',
            'label': _('TDs Type'),
            'fieldtype': 'Link',
	    	'options': 'Supplier',
           
        },
		{
			'fieldname': 'Account Head',
			'lable': _('Account Head'),
			'fieldtype': 'Link',
			'options': 'Account',
		},
		{
			'fieldname': 'TDs Amount',
			'label': _('TDs Amount'),
			'fieldtype': 'Currency',
		},
		{
			'fieldname': 'Paid Amount',
			'label': _('Paid Amount'),
			'fieldtype': 'Currency',
		},
		{
			'fieldname': 'TDs Balance',
			'label': _('TDs Balance'),
			'fieldtype': 'Currecy',
		},

	]

	data = []
	return columns, data
