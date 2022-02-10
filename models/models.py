#-*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, timedelta

class recipe(models.Model):
     _name = 'cook.recipe'
     _description = 'Cooking recipes'

     name = fields.Char()
     description = fields.Text()
     datetime_begin = fields.Datetime('Datetime', default=fields.datetime.now())
     datetime_end = fields.Datetime(compute="_date_end", store=True)
     timelabor = fields.Integer() #compute='_compute_time_lab', store=True)
#     timeinstr = fields.Integer(related='instruction_ids.timeinstr', store=True)
     ingredient_ids = fields.Many2many('cook.ingredient', string='ingredients')
     instruction_ids = fields.One2many('cook.instruction','recipe_id', string='instructions')
#     amount_ids = fields.Many2many('cook.amount', string='amounts')
     employee_ids= fields.Many2many('hr.employee', string='Employee')
     cooktype = fields.Selection([('micro', 'Microwave'), ('grill', 'Grill'), ('oven', 'Oven'), ('none','None'), ('mix','Mixture')], string='Cook type', default='none')
     state = fields.Selection([('not started', 'Not started'), ('started', 'Started'), ('heating', 'Heating'), ('ready','Ready'), ('eated','Eated')], string='State', default='not started')
     isvegan = fields.Boolean('Vegan', default=False)
     ultraproc = fields.Boolean('Ultraprocessed', default=False)
     cmilk = fields.Boolean('Milk',default=False)
     ceggs = fields.Boolean('Eggs',default=False)
     cfish = fields.Boolean('Fish',default=False)
     cshellfish = fields.Boolean('Shell Fish',default=False)
     ctreenuts= fields.Boolean('Tree nuts',default=False)
     cpeanuts = fields.Boolean('Peanuts',default=False)
     cwheat =fields.Boolean('Wheat',default=False)
     csoybean=fields.Boolean('Soybeans',default=False)
     allergen=fields.Boolean(compute="_allerg", store=True)

     @api.onchange('datetime_begin')
     def _date_end(self):
         for record in self:
             record.datetime_end = record.datetime_begin + timedelta(minutes=record.timelabor)

     @api.depends('cshellfish','cpeanuts','cwheat','ceggs','cmilk','cfish','csoybean','ctreenuts')
     def _allerg(self):
          self.allergen = self.cshellfish or self.cwheat or self.cpeanuts or self.cmilk or self.ceggs or self.cfish or self.csoybean or self.ctreenuts

#     @api.depends('timeinstr')
#     def _compute_time_lab(self):
#         aux=0
#         for record in self:
#             aux = record.timeinstr+aux
#         self.timelabor=aux

class ingredient(models.Model):
     _name ='cook.ingredient'
     _description='cooking ingredients'

     name =fields.Char()
     description =fields.Text()
     calories =fields.Float(compute="_calcomp", store=True)
     carbh = fields.Float()
     protein =fields.Float()
     fat = fields.Float()
     #units = fields.Integer()
     amount = fields.Float()
     #help="Must be expressed in g")
     recipe_ids = fields.Many2many('cook.recipe',string='recipes')

     @api.depends('carbh','protein','fat','amount')
     def _calcomp(self):
          self.calories = ( self.carbh*4 + self.protein*4 + self.fat*9 ) *self.amount / 100

class instruction(models.Model):
     _name='cook.instruction'
     _description='cooking instructions'

     name = fields.Char()
     amount=fields.Integer()
     description = fields.Text()
     step = fields.Integer()
     recipe_id = fields.Many2one('cook.recipe', string='recipe')
     timeinstr = fields.Integer()
