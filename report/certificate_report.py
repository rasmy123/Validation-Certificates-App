
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class CertificateReport(models.AbstractModel):
    _name = 'report.certificates.certificate_template'
    _description = 'Inherit print function to check if the normal user printed the report before'



   # oveloade print report funtion to restrict normal user to print only once
    @api.model
    def _get_report_values(self, docids, data):
        current_certificate = self.env["certificates.certificate"].browse(docids)
        print(current_certificate.allow_reprint_report)
        if  self.env.user.has_group('certificates.certificates_normal_group'):

            if not current_certificate.allow_reprint_report:
                raise ValidationError('You are not  allowed to print the report again')

        self.env["certificates.print.history"].create({"certificate_id": current_certificate.id})
        return {
            'doc_ids' : docids,
            'doc_model' : self.env['certificates.certificate'],
            'data' : data,

        }
