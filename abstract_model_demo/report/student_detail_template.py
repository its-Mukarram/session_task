# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, api


class StudentDetailTemplate(models.AbstractModel):
    _name = 'report.abstract_model_demo.report_student_template'
    _description = 'Abstract Model for Report'


    @api.model
    def _get_report_values(self, docids, data=None):
        print(docids,self,data)
        records = self.env['student.detail'].browse(docids)
        return {
            'school_name': 'Aktiv Software',
            'docs': records,
        }
