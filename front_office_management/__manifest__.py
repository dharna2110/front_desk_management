{
    'name': 'Front Office Management',
    'version': '17.0.1.0.0',
    'sequence': -100,
    'summary': 'Administer front office operations: overseeing visitors, device management, registration, and activities.',
    'author': "Namah Softech",
    'maintainer': "Namah Softech",
    'description': 'Manage Visitors: Oversee guest arrivals and departures, Keep Check-In, Check-Out. Details of Visitors: Maintain records of visitor entries and exits. '
                   'Issue Visitor Pass: Provide identification passes for access. Manage Visitor Belongings: Secure and track items brought by guests. '
                   'Manage Employee Belongings: Monitor and store personal items of staff. Print Property Label: Create and print labels for tracking property items.',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/visits_insight_view.xml',
        'views/number_of_visits_views.xml',
        'views/menuitems.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
