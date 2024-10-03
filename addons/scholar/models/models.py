# models/aula.py

from odoo import models, fields, api, exceptions

class Aula(models.Model):
    _name = 'aula.aula'
    _description = 'Aula'

    name = fields.Char(string='Nombre del Aula', required=True)
    numeral = fields.Integer(string='Numeral', required=True)
    literal = fields.Char(string='Literal', required=True)
    capacidad = fields.Integer(string='Capacidad', required=True)
    materias_ids = fields.Many2many('aula.materia', string='Materias')
    profesores_ids = fields.Many2many('aula.profesor', string='Profesores')
    estudiantes_ids = fields.Many2many('aula.estudiante', string='Estudiantes')
    horario_ids = fields.One2many('aula.horario', 'aula_id', string='Horarios')

    materias_text = fields.Char(string='Materias Asignadas', compute='_compute_materias_text')

    def _compute_materias_text(self):
        """
        Concatena los nombres de las materias asignadas a un aula en un solo campo.
        
        Se utiliza como computado para el campo 'materias_text' y se actualiza
        cada vez que se modifica la lista de materias asignadas a un aula.
        """
        for record in self:
            materias = record.materias_ids.mapped('name')
            record.materias_text = ', '.join(materias) or 'Sin materias asignadas'
    @api.constrains('capacidad')
    def _check_capacidad(self):
        """
        Verifica que la capacidad del aula sea un valor positivo.
        """
        for record in self:
            if record.capacidad < 0:
                raise exceptions.ValidationError('La capacidad del aula no puede ser negativa.')
    
class Materia(models.Model):
    _name = 'aula.materia'
    _description = 'Materia'

    name = fields.Char(string='Nombre de la Materia', required=True)
    description = fields.Text(string='Descripción')
    
    aula_ids = fields.Many2many('aula.aula', string='Aulas')
    profesor_ids = fields.Many2many('aula.profesor', string='Profesores')
    horario_ids = fields.One2many('aula.horario', 'materia_id', string='Horario', ondelete='cascade')
    
class Profesor(models.Model):
    _name = 'aula.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    especializacion = fields.Char(string='Especialización')
    aulas_ids = fields.Many2many('aula.aula', string='Aulas')
    
class Estudiante(models.Model):
    _name = 'aula.estudiante'
    _description = 'Estudiante'

    name = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')

    aula_id = fields.Many2one('aula.aula', string='Aula')
    
class Horario(models.Model):
    _name = 'aula.horario'
    _description = 'Horario de Clase'

    materia_id = fields.Many2one('aula.materia', string='Materia', ondelete='cascade')
    profesor_id = fields.Many2one('aula.profesor', string='Profesor', required=True)
    aula_id = fields.Many2one('aula.aula', string='Aula', required=True)
    dia_semana = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ], string='Día de la Semana', required=True)
    hora_inicio = fields.Datetime(string='Hora de Inicio', required=True)
    hora_fin = fields.Datetime(string='Hora de Fin', required=True)