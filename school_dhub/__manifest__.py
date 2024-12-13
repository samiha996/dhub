{
    'name':"School",
    'author':"Samiha",
    'category':"Education",
    'version':"17.0.0.1.0",
    'depends':[
        'base', 'product','website','website_sale',
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/base_menu.xml',
        'views/school_view.xml',
        'views/city_view.xml',
        'views/product_attribute_view.xml',
        'views/website_sale_search_box.xml',
        
    ],
    
    'assets': {
        'point_of_sale._assets_pos': [
            'school_dhub/static/src/app/**/*',
        ],
         
    },
    
    'application':True,
    'installable':True,
}