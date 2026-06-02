{
    'name': 'Construction Project Management',
    'version': '1.0',
    'summary': 'Track site surveys, BOQ generation, and engineering project lifecycles.',
    'category': 'Operations',
    'author': 'IT Operations Team',
    'depends': ['base', 'mail'],  # 'mail' gives us chatter/activity tracking features
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml',
    ],
    'installable': True,
    'application': True,
}
