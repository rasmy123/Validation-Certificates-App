from odoo import  models,fields

class CertificatesType(models.Model):
    _name="certificates.type"
    _description="Certificates Types"

    name=fields.Char()


