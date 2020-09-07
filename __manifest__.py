{
    'name': 'Invoice Delivery',
    'version': '12.0.1.0.0',
    'summary': 'Handle Delivery invoice',
    'description': """ 
    Feature Module \n
        - handle invoice delivery for expedition
        - manage driver comission
    """,
    'category': 'Extra Tools',
    'author': 'LobotIjo',
    'maintainer':'AdesDev',
    'website': 'digitalfarmer.github.io',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'account',
    ],
    'data': [
            'views/expedition.xml',
            'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'sequence': '4',
    'auto_install': False,

}