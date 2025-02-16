{
    'name': 'Sales Team Specific Menus',
    'version': '1.0',
    'summary': 'Dynamically creates menu items for each sales team',
    'author': 'Samiha',
    'depends': ['sale_management', 'crm'],
    'data': [
        'security/crm_team_record_rule.xml',
        'security/crm_team_manager_rule.xml',
        'views/crm_team_dynamic_menu.xml',
    ],
    'installable': True,
    'application': True,
}
