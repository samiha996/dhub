
{
    'name': 'Crm DeeHub Module',
    'version': '1.0',
    'category': 'Product',
    'summary': 'Auto-fill product fields before saving',
    'author': 'Ghaith',
    'depends': ['product','crm','sale','sale_crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/menus.xml',
        'views/crm_lead_view.xml',
    ],
    'installable': True,
    'application': False,
}

