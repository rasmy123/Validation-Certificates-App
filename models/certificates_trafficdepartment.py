from odoo import  models,fields

class CertificatesTrafficDepartment(models.Model):
    _name="certificates.trafficdepartment"
    _description="Certificates Traffic Department"

    name=fields.Char()


