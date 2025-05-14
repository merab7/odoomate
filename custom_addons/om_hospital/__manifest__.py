{
    "name": "Hospital Management System",
    "author":"Merab Todua",
    "version": "17.0.1.1",

    "depends":['mail', 'product', 'account'],

    "data":[
      'security/security.xml',
      'security/ir.model.access.csv',
      'data/sequence.xml',
      'views/patient_views.xml',
      'views/patient_readonly_views.xml',
      'views/patient_appointment.xml',
      'views/patient_tag.xml',
      'views/appointment_line.xml',
     'views/account_move_views.xml',
      'views/menu.xml',


    ],

    "license": "LGPL-3",
}