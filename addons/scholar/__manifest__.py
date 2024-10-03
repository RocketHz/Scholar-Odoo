# -*- coding: utf-8 -*-
{
    'name': "Scholar",  # Replace with a more descriptive name 

    'summary': "Manage Aulas, Materias, Profesores, Estudiantes and Assignments",

    'description': """
        This module allows you to manage a basic school registration system 
        including Aulas (classrooms), Materias (subjects), Profesores (teachers), 
        Estudiantes (students) and their Assignments.
    """,

    'author': "root3b - Ronni Hernandez",  
    'website': "https://www.yourwebsite.com",  

    'category': 'Education',  

    'version': '0.1',

    'depends': ['base'],

    "data": [
        "security/ir.model.access.csv",
        "views/aula_aula_views.xml",
        "views/templates.xml",
        "views/aula_materia_views.xml",
        "views/aula_profesor_views.xml",
        "views/aula_estudiante_views.xml"
    ],

    'demo': [
        'demo/demo.xml',  # Add demo data if needed
    ],
}