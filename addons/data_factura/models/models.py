# -*- coding: utf-8 -*-

from odoo import models, fields, api # type: ignore


class data_factura(models.Model):
    _name = 'data_factura.data_factura'
    _description = 'data_factura.data_factura'

    nombre = fields.Char(string='Nombre')
    apellido = fields.Char(string='Apellido')
    empresa = fields.Char(string='Empresa',required=True)
    email = fields.Char(string='Email')
    fecha = fields.Date(string='Fecha')
    productos_comprados = fields.One2many('data_factura.precio_productos', 'factura_id', string='Productos Comprados')
    total = fields.Float(string='Total', compute='_compute_total')


    @api.depends('productos_comprados')
    def _compute_total(self):
          for record in self:
              record.total = sum(producto.subtotal for producto in record.productos_comprados)

class Productos(models.Model):
    _name = 'data_factura.productos'
    _description = 'Categorías de productos'

    bebidas = fields.Selection(
        [
        ('malta_morena', 'Malta Morena'),
        ('coca_Cola', 'Coca-Cola'),
        ('sprite', 'Sprite'),
        ('fanta', 'Fanta'),
        ('agua_Malta', 'Agua Malta'),
        ('fresco_de_chinola', 'Fresco de Chinola'),
        ('fresco_de_Guanábana', 'Fresco de Guanábana'),
        ('kola_Real', 'Kola Real')
    ],
        string='Bebidas')
    
    arroz = fields.Selection(
        [

            ('arroz_la_garza', 'Arroz La Garza'),
            ('campo_dorado', 'Campo Dorado'),
            ('arroz_gema', 'Arroz Gema'),
            ('arroz_campeon' ,'Arroz Campeón'),
            ('arroz_cofre' ,'Arroz Cofre'),
            ('arroz_don_cola','Arroz Don Colá'),
            ('arroz_san_rafael' ,'Arroz San Rafael'),
            ('arroz_sol' ,'Arroz Sol'),
            ('arroz_chino' ,'Arroz Chino'),
            ('arroz_bisono' ,'Arroz Bisonó'),
            ('arroz_pimco' ,'Arroz Pimco')

        ],
        string='Arroz'
    )
    
    verduras = fields.Selection(
        [
            ('tomates_verdes' , 'Tomates Verdes'),
            ('ajo' , 'Ajo'),
            ('espinaca' , 'Espinaca'),
            ('calabacin' , 'Calabacín'),
            ('cebolla_morada' , 'Cebolla morada'),
            ('zanahoria' , 'Zanahoria'),
            ('pepino' , 'Pepino'),
            ('ajies' , 'Ajíes'),
            ('apio' , 'Apio'),
            ('silantro_ancho' , "Silantro Ancho")
        ],
        string='Verduras'
    )
    
    pan = fields.Selection(
        [

            ('pan_de_agua' , 'Pan de Agua'),
            ('pan_sobao' , 'Pan Sobao'),
            ('pan_de_telera' , 'Pan de Telera'),
            ('pan_de_maiz' , 'Pan de Maíz'),
            ('pan_de_coco' , 'Pan de Coco'),
            ('pan_de_batata' , 'Pan de Batata'),
            ('pan_de_guayaba' , 'Pan de Guayaba'),
            ('pan_de_casabe' , 'Pan de Casabe'),
            ('pan_de_manteca' , 'Pan de Manteca')
        ],
        string='Pan'
    )


class PrecioProductos(models.Model):
    _name = 'data_factura.precio_productos'
    _description = 'Productos comprados por el cliente'

    factura_id = fields.Many2one('data_factura.data_factura', string='Factura')
    producto_id = fields.Many2one('data_factura.productos', string='Producto')
    cantidad = fields.Integer(string='Cantidad')
    precio_unitario = fields.Float(string='Precio Unitario')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal')

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario