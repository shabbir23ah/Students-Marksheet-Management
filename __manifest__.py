{
    'name': 'Student Marksheet Management System',
    'version': '1.0.0',
    'author': 'Shabbir Ahmmed',
    'email': '@gmail.com',
    'sequence': '2',
    'summary': 'Manage student marksheets',
    'description': """
    This module allows schools to manage student marksheets
    """,
    'depends': ['base', 'mail',
    ],
    'data': ['security/ir.model.access.csv', 'views/task_main_view.xml', 'views/menu_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}