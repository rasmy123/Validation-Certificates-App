from dateutil.relativedelta import relativedelta

from odoo import models, fields,api
from datetime import datetime,date
from odoo.exceptions import ValidationError

class CertificatesCertificate(models.Model):
    _name="certificates.certificate"
    _description="Certificates Certificate"
    _rec_name="customer"


    serial_number = fields.Char(default=lambda self: self.env['ir.sequence'].next_by_code('increment_serial_number'))
    motor_number=fields.Char()
    chassis_number=fields.Char()

    price=fields.Char()
    vehicle_type=fields.Selection([
        ('car','Car'),
        ('bus','Bus'),
        ('minibus','Minibus'),
        ('microbus','Microbus')
    ])
    certificate_type=fields.Many2one('certificates.type')
    traffic_department = fields.Many2one('certificates.trafficdepartment')
    brand = fields.Many2one('certificates.vehiclebrand')
    customer = fields.Many2one('res.partner')
    print_history_ids = fields.One2many('certificates.print.history', 'certificate_id')
    allow_reprint_report=fields.Boolean()
    #age=fields.Integer(compute="_cal_age")
    #compute_age = fields.Integer()
    #department_id=fields.Many2one("hms.department")

    def get_year_list(self):
        vals = []
        current_year = datetime.now().date().year

        for x in range(21):
            vals.extend([(str(current_year), str(current_year))])
            current_year = current_year - 1

        return vals
    car_model = fields.Selection(selection=get_year_list)

    def allow_reprint(self):
        self.allow_reprint_report=True

#    @api.model
#    def create(self,vals):
#        new_certificate=super().create(vals)
#        self.env["certificates.print.history"].create({"certificate_id": new_certificate.id})
#        return new_certificate





    #     if self.age<30:
    #         self.pcr=True
    #         return {
    #             'warning':{
    #                 'title':'Hello',
    #                 'message':'The PCR field was checked'
    #             }
    #         }
    #     else:
    #         self.pcr=False
#     def change_state(self):
#         self.ensure_one()
#         for record in self:
#             if self.state=='undetermined':
#                 self.state='good'
#             elif self.state=='good':
#                 self.state='fair'
#             elif self.state=='fair':
#                 self.state='serious'
#         self.env["hms.log.history"].create({
#             "description": f" State changed to {self.state}",
#             "patient_id": self.id
#
#         })
#     def reset_undetermined(self):
#         if self.state !='undetermined':
#             self.state='undetermined'
#
#
#     _sql_constraints = [
#         ('duplicate_name','UNIQUE(email)','Email already exists')
#     ]
#     @api.constrains('email')
#     def _validate_email(self):
#         if self.email:
#             match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
#             if match == None:
#                 raise ValidationError('The email is not valid as email format')
#
#
#     def _cal_age(self):
#         for record in self:
#             if record.birth_date:
#                 age = relativedelta(datetime.now().date(), fields.Datetime.from_string(record.birth_date)).years
#                 record.age = int(age)
#
#
#
class PrintHistory(models.Model):
    _name="certificates.print.history"
    certificate_id = fields.Many2one('certificates.certificate')





