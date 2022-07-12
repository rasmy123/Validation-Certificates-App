{
    "name":"Vehicles Validation Certificate",
    "decription":"The Validation Certificate module is used to check vehicles and issues validation certificates"
                 " by the company that licensed by the Ministry of interior ",
    "depends" : ["crm"],
    "data":[
        "security/certificates_security.xml",
        "security/ir.model.access.csv",
        "views/certificates_certificate_view.xml",
        "views/certificates_type_view.xml",
        "views/certificates_trafficdepartment_view.xml",
        "views/certificates_customer_view.xml",
        "report/certificate_template.xml",
        "report/certificate_report.xml"



    ]
}