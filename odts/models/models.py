# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MolOdtMedios(models.Model):
	_inherit = "odt.medios"

	#CAMPOS EDITADOS
	target_compra_modulo = fields.Selection([('1','Niños 4-12'),('2','Jóvenes 13-18'),('3','Personas 19+'),('4','Hombres 19+'),('5','Mujeres 19+'),('6','Amas de casa 19-54 S/DE'),('7','Personas 19-54 S/DE'),('8','Hombres 19-54 S/DE'),('9','Mujeres 19-54 S/DE')],string='Target de compra Módulos o Franja', track_visibility=True)
	cofepris = fields.Selection([('1','COFEPRIS'),('2','A favor de lo mejor'),('3','Kids policy')],string=' ', track_visibility=True)

	#CAMPOS NUEVOS
	aaee_marca_producto = fields.Char(string="Marca o producto")
	aaee_inversion = fields.Char(string="Inversión")

	telenovelas_bool = fields.Boolean(string='Telenovelas', track_visibility=True)
	tvsa_requerir_especificaciones = fields.Text(string='', track_visibility=True)
	tvsa_abierta_observaciones_dos = fields.Text(string='', track_visibility=True)

	tabla_box_bool = fields.One2many('mod.box.tbl', 'id_box_tbl', ondelete="cascade")
	tabla_canal5_bool = fields.One2many('mod.canal5.tbl', 'id_canal5_tbl', ondelete="cascade")
	tabla_comedia_bool = fields.One2many('mod.come.tbl', 'id_comedia_tbl', ondelete="cascade")
	tabla_enlatados_bool = fields.One2many('mod.enlatados.tbl', 'id_enlatados_tbl', ondelete="cascade")
	tabla_revista_bool = fields.One2many('mod.revista.tbl', 'id_revista_tbl', ondelete="cascade")
	tabla_deportivos_bool = fields.One2many('mod.deportivos.tbl', 'id_deportivos_tbl', ondelete="cascade")
	tabla_lucha_bool = fields.One2many('mod.lucha.tbl', 'id_lucha_tbl', ondelete="cascade")
	tabla_noticieros_bool = fields.One2many('mod.noticieros.tbl', 'id_noticieros_tbl', ondelete="cascade")
	tabla_telenovelas_bool = fields.One2many('mod.telenovelas.tbl', 'id_telenovelas_tbl', ondelete="cascade")

	nt_tabla_net =fields.One2many('mod.net.tbl', 'id_net_tbl', ondelete="cascade")

	tvsa_primario = fields.Char(string="Primario", compute="_get_valor_primario")
	tvsa_marca_pro = fields.Char(string="Marca o producto")
	tvsa_marca_pro_nac = fields.Char(string="Marca o producto")

	sc_inversion = fields.Float(string="Inversión")
	sc_indicar_rotacion = fields.Char(string="Indicar rotación")
	sc_cobertura = fields.Selection([('1','Nacional'),('2','Local'),('3','Elección de canales'),('4','Específico si ya lo conocen')], string="Cobertura")
	sc_local = fields.Char(string="Local")

	nt_inversion = fields.Float(string="Inversión")
	nt_conoce_programas = fields.Char(string='Si conoce el(los) programa(s) indicar', track_visibility=True)
	nt_cofepris = fields.Selection([('1','COFEPRIS'),('2','A favor de lo mejor'),('3','Kids policy')],string=' ', track_visibility=True)
	nt_observacion = fields.Char(string=" ")

	#-- FUNCION PARA OBTENER EL VALOR EN AUTOMATICO DEL CAMPO PRIMARIO --#
	@api.depends('tvsa_nse_1','tvsa_nse_2','tvsa_nse_3','tvsa_nse_4','tvsa_grupo_edad_1','tvsa_grupo_edad_2','tvsa_grupo_edad_3','tvsa_grupo_edad_4','tvsa_grupo_edad_5','tvsa_grupo_edad_6','tvsa_grupo_edad_otro')
	def _get_valor_primario(self):
		nse_1 = ""
		nse_2 = ""
		nse_3 = ""
		nse_4 = ""
		ge_1 = ""
		ge_2 = ""
		ge_3 = ""
		ge_4 = ""
		ge_5 = ""
		ge_6 = ""
		ge_otro = ""
		if self.tvsa_nse_1 == True:
			nse_1 = "ABC+"
		if self.tvsa_nse_2 == True:
			nse_2 = ",  C"
		if self.tvsa_nse_3 == True:
			nse_3 = ",  D+"
		if self.tvsa_nse_4 == True:
			nse_4 = ",  DE"

		if self.tvsa_grupo_edad_1 == True:
			ge_1 = '  4-12'
		if self.tvsa_grupo_edad_2 == True:
			ge_2 = ',  13-18'
		if self.tvsa_grupo_edad_3 == True:
			ge_3 = ',  19-29'
		if self.tvsa_grupo_edad_4 == True:
			ge_4 = ',  30-44'
		if self.tvsa_grupo_edad_5 == True:
			ge_5 = ',  45-54'
		if self.tvsa_grupo_edad_6 == True:
			ge_6 = ',  55+'
		if self.tvsa_grupo_edad_otro:
			ge_otro = ',  ' + self.tvsa_grupo_edad_otro

		self.tvsa_primario = nse_1 + nse_2 + nse_3 + nse_4 + ge_1 + ge_2 + ge_3 + ge_4 + ge_5 + ge_6 + ge_otro
		#-- FIN FUNCION PARA OBTENER EL VALOR EN AUTOMATICO DEL CAMPO PRIMARIO --#
		
class TablaTVabiertaAdi(models.Model):
	_inherit = 'odt.plaza.medios'

	@api.onchange('tipo_actividad')
	def _funcion_duracion(self):
		if self.tipo_actividad == '2':
			self.duracion = "20”"
		else:
		 self.duracion = ""	

#CLASE PARA LA TABLA DE BOX EN ACCIONES ESPECIALES SATANDARD
class ModBoxTbl(models.Model):
	_name = "mod.box.tbl"

	id_box_tbl = fields.Many2one('odt.medios')
	box_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	box_programa = fields.Char(string="Programa")
	box_genero = fields.Char(string="Genero", default="Box")
	box_duracion = fields.Char(string="Duración")
	box_especificar_aaee = fields.Selection([('1','Super'),('2','Banner'),('3','Mención 10"'),('4','Mención 20"'),('5','Cortinilla a corte'),('6','Patrocinio de Programa'),('7','Patrocinio de Sección')], string="Especificar AAEE")

class ModCanal5Tbl(models.Model):
	_name = "mod.canal5.tbl"

	id_canal5_tbl = fields.Many2one('odt.medios')
	canal5_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	canal5_programa = fields.Char(string="Programa")
	canal5_genero = fields.Char(string="Genero", default="Caricaturas, películas y series")
	canal5_duracion = fields.Char(string="Duración")
	canal5_especificar_aaee = fields.Selection([('1','Edición creativa'),('2','Cortinilla a corte'),('3','L en contenido'),('4','Patrocinio de programa'),('5','Promos Vea'),('6','Social TV'),('7','BUG (Logo)')], string="Especificar AAEE")

class ModComediaTbl(models.Model):
	_name = "mod.come.tbl"

	id_comedia_tbl = fields.Many2one('odt.medios')
	comedia_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	comedia_programa = fields.Char(string="Programa")
	comedia_genero = fields.Char(string="Genero", default="Comedia")
	comedia_duracion = fields.Char(string="Duración")
	comedia_especificar_aaee = fields.Selection([('1','Cortinilla a corte'),('2','Avance del Programa'),('3','Patrocinio de programa')], string="Especificar AAEE")

class ModEnlatadosTbl(models.Model):
	_name = "mod.enlatados.tbl"

	id_enlatados_tbl = fields.Many2one('odt.medios')
	enlatados_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	enlatados_programa = fields.Char(string="Programa")
	enlatados_genero = fields.Char(string="Genero", default="Enlatados")
	enlatados_duracion = fields.Char(string="Duración")
	enlatados_especificar_aaee = fields.Selection([('1','Patrocinio de programa'),('2','Cortinilla a corte')], string="Especificar AAEE")

class ModRevistaTbl(models.Model):
	_name = "mod.revista.tbl"

	id_revista_tbl = fields.Many2one('odt.medios')
	revista_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	revista_programa = fields.Char(string="Programa")
	revista_genero = fields.Char(string="Genero", default="Revista")
	revista_duracion = fields.Char(string="Duración")
	revista_especificar_aaee = fields.Selection([('1','Pleca'),('2','Super'),('3','Banner'),('4','Mención 30"'),('5','Mención 60"'),
								('6','Mención 120"'),('7','Promos Vea'),('8','Patrocinio de Programa'),('9','Patrocinio de sección'),
								('10','Entrevista 60"'),('11','Entrevista 120"'),('12','Bumper'),('13','Wiper')], string="Especificar AAEE")

class ModDeportivosTbl(models.Model):
	_name = "mod.deportivos.tbl"

	id_deportivos_tbl = fields.Many2one('odt.medios')
	deportivos_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	deportivos_programa = fields.Char(string="Programa")
	deportivos_genero = fields.Char(string="Genero", default="Deportivos")
	deportivos_duracion = fields.Char(string="Duración")
	deportivos_especificar_aaee = fields.Selection([('1','Pleca'),('2','Super'),('3','Banner'),('4','Cortinilla a corte'),
											 		('5','Promos Vea'),('6','Mención 30"'),('7','Mención 60"'),('8','Patrocinio de sección'),('9','Patrocinio de sección con pie'),('10','Patrocinio de programa')], string="Especificar AAEE")
class ModLuchaTbl(models.Model):
	_name = "mod.lucha.tbl"

	id_lucha_tbl = fields.Many2one('odt.medios')
	lucha_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	lucha_programa = fields.Char(string="Programa")
	lucha_genero = fields.Char(string="Genero", default="Lucha Libre")
	lucha_duracion = fields.Char(string="Duración")
	lucha_especificar_aaee = fields.Selection([('1','Super'),('2','Banner'),('3','Mención 10"'),('4','Mención 30"'),('5','Mención 60"'),('6','Mención 120"'),('7','Cortinilla a corte'),
									('8','Patrocinio de Programa'),('9','Patrocinio de Sección'),('10','Patrocinio de sección con pie')], string="Especificar AAEE")

class ModNoticierosTbl(models.Model):
	_name = "mod.noticieros.tbl"

	id_noticieros_tbl = fields.Many2one('odt.medios')
	noticieros_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	noticieros_programa = fields.Char(string="Programa")
	noticieros_genero = fields.Char(string="Genero", default="Noticieros")
	noticieros_duracion = fields.Char(string="Duración")
	noticieros_especificar_aaee = fields.Selection([('1','Pleca'),('2','Super'),('3','Banner'),('4','Cortinilla a corte'),('5','Promos Vea'),('6','Avance del Programa'),
								 ('7','Patrocinio de Programa'),('8','Patrocinio de sección'),('9','Resumen Informativo')], string="Especificar AAEE")

class ModTelenovelasTbl(models.Model):
	_name = "mod.telenovelas.tbl"

	id_telenovelas_tbl = fields.Many2one('odt.medios')
	telenovelas_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	telenovelas_programa = fields.Char(string="Programa")
	telenovelas_genero = fields.Char(string="Genero", default="Telenovelas")
	telenovelas_duracion = fields.Char(string="Duración")
	telenovelas_especificar_aaee = fields.Selection([('1','Sin resultados')], string="Especificar AAEE")

class ModNetTbl(models.Model):
	_name = "mod.net.tbl"

	id_net_tbl = fields.Many2one('odt.medios')
	nt_network = fields.Char(string="Network")
	nt_tipo_actividad = fields.Selection([('1','Spoteo'),('2','Acciones especiales')], string="Tipo actividad")
	nt_duracion = fields.Char(string="Duración")
	nt_especificar_aaee = fields.Char(string="Especificar AAEE")