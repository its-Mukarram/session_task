# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, fields


class StudentDetail(models.TransientModel):
    _name = "student.detail"
    _description = "Student Detail"

    name = fields.Char(string="Name", help="Name of the Applicant",
                       required=True)
    mobile = fields.Integer(string="Mobile No.",
                            help="Enter Mobile Number ")
    address = fields.Text(string="Address")
    percentage = fields.Float(string="Percentage",
                              help="Enter Percentage with 2 decimals")
    date_of_birth = fields.Date(string="Date of Birth",
                                help="Select Date of Birth")
    education = fields.Selection(
        [('me', "M.E."), ('be', "B.E."), ('diploma', "Diploma"),
         ('12', "12th")], string="Education", default='be')
    product_id = fields.Many2one(comodel_name="product.product",
                                 string="Products", required=False, )
    product_type = fields.Selection(string="type",
                                    related='product_id.detailed_type',
                                    readonly=False)

    def action_print_report(self):
        return self.env.ref(
            'abstract_model_demo.action_student_report').report_action(self)
