# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
	'name': 'Student Addons for Abstract Model',
	'version': '17.0.1.0.0',
	'category': 'Sale',
	'summary': 'This is a test addon for Abstract Model',
	'depends': ['sale'],
	'data': [
		'security/ir.model.access.csv',
		'report/student_detail_template.xml',
		'report/report.xml',
		'views/student_detail_view.xml',
	],
	'license': 'OPL-1',
}
