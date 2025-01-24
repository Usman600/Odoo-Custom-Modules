{
    "name": "Hospital Management System",
    "author": "Muhammad Usman Hussain",
    "License": "LGPL-3",
    "version": "1.0",
    "summary": 'Manage all hospital Data',
    'description': """
This module offers the basic functionalities to manage hospital data.
    """,
    "depends":[
        "mail",
        "product",
        "account",
    ],
    "data":[
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/menu_patient.xml",
        "views/menu_patient_readonly.xml",
        "views/appointment_views.xml",
        "views/appointment_line_views.xml",
        "views/patient_tag_view.xml",
        "views/menu.xml",

    ]
}