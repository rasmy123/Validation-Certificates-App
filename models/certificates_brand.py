from odoo import  models,fields

class CertificatesVehicleBrand(models.Model):
    _name="certificates.vehiclebrand"
    _description="Certificates Vehicle Brands"

    name=fields.Char()


