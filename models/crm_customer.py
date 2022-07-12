from odoo import fields,models,api
from odoo.exceptions import ValidationError

class CrmCustomerInherite(models.Model):
    _inherit = "res.partner"

    related_patient_id=fields.Many2one("certificates.certificate")



    # @api.constrains('email')
    # def _validate_email(self):
    #     if self.email:
    #         if self.related_patient_id.email != self.email:
    #             raise ValidationError('The customer email must be the same as the patient email')
    #
    # def unlink(self):
    #     for record in self:
    #         if record.related_patient_id:
    #             raise ValidationError(f"The operation cannot be completed:Can not delete customer related with the patient: {record.related_patient_id.first_name}")
    #     super().unlink()