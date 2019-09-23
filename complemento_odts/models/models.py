# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MolOdtMedios(models.Model):
	_inherit = "odt.medios"

	#CAMPOS EDITADOS
	target_especial = fields.Char(string='En caso de ser Target de compra especial, especificar', track_visibility=True)
	target_compra_modulo = fields.Selection([('1','Niños 4-12'),('2','Jóvenes 13-18'),('3','Personas 19+'),('4','Hombres 19+'),('5','Mujeres 19+'),('6','Amas de casa 19-54 S/DE'),('7','Personas 19-54 S/DE'),('8','Hombres 19-54 S/DE'),('9','Mujeres 19-54 S/DE'),('10','Amas de casa')],string='Target de compra Módulos o Franja', track_visibility=True)
	med_periodo_camap = fields.Char(string='Periodo campaña y/o promoción', track_visibility=True)
	#Radio
	rad_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)
	rad_target_interes = fields.Char(string='Target de Interés', track_visibility=True)
	rad_periodo_campana = fields.Char(related="med_periodo_camap", string='Periodo de transmisión', track_visibility=True)

	# Digital
	d_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)
	d_periodo_campana = fields.Char(related="med_periodo_camap", string='Periodo de la campaña', track_visibility=True)
	d_target_demo = fields.Char(string='Target Demográfico', track_visibility=True)
	d_target_perfil = fields.Char(string='Target perfil Psicográfico', track_visibility=True)
	d_objetivo_campana = fields.Text(string='Objetivo de la campaña', track_visibility=True)

	# Revista
	r_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)
	r_target_interes = fields.Char(string='Target de Interés', track_visibility=True)
	r_periodo_campana = fields.Char(related="med_periodo_camap", string='Periodo de la campaña')

	#Spoteo
	sc_canales = fields.Selection([('1','Rank Rating'),('2','Afinidad Target')],string='Criterio de selección de canales', track_visibility=True)
	sc_canales_conocen = fields.Text(string='Especificar canales si ya se conocen', track_visibility=True)
	sc_marca_producto = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)

	rotation_indication = fields.Text(string="Indicación de rotación", track_visibility=True)

	#Analisi habitos
	an_marca1 = fields.Char(string='Categoría o Marca/Producto de interés', track_visibility=True)
	an_target_interes1 = fields.Char(string='Target de interés', track_visibility=True)

	#Analisis Audiencias
	an_target_interes = fields.Char(string='Target de interés', track_visibility=True)

	nt_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)
	ot_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)

	p_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto', track_visibility=True)
	p_target_interes = fields.Char(string='Target de Interés', track_visibility=True)
	p_periodo_campana = fields.Char(related="med_periodo_camap", string='Período de la campaña', track_visibility=True)

	sptv_periodo_camp2 = fields.Char(related="med_periodo_camap", string='Período de la Campaña', track_visibility=True)
	period_campania_tvab = fields.Char(related="med_periodo_camap", string="Período de la campaña", track_visibility=True)
	aaeetv_periodo_camp = fields.Char(related="med_periodo_camap", string='Período de la Campaña', track_visibility=True)
	sc_periodo_campana = fields.Char(related="med_periodo_camap", string='Período de la Campaña', track_visibility=True)
	nt_periodo_campana = fields.Char(related="med_periodo_camap", string='Período de la Campaña', track_visibility=True)
	oh_periodo_campana = fields.Char(related="med_periodo_camap", string='Período de la campaña', track_visibility=True)

	oh_marca = fields.Char(related="crm_odt_id.marca.name", string='Marca o Producto')

	opcion_compra = fields.Selection([('1','CPR MÓDULOS'),('2','CPR FRANJAS'),('3','MIXTO MÓDULO Y FRANJA'),('4','CPR POR PROGRAMA'),('5','SPOTEO')],string='Negociación del cliente', track_visibility=True)

	#CAMPOS NUEVOS
	med_spot_tv_abierta_local = fields.Boolean(string='TVSA TVA Local', track_visibility=True)

	ot_inversion = fields.Float(string="Inversión")
	ot_regulacion_cofepris = fields.Boolean(string="COFEPRIS", track_visibility=True)
	ot_regulacion_favor = fields.Boolean(string="A favor de lo mejor", track_visibility=True)
	ot_regulacion_kids = fields.Boolean(string="Kids policy", track_visibility=True)
	ot_canales_sel = fields.Selection([('1','Rank Rating'),('2','Afinidad Target')],string='Criterio de selección de canales', track_visibility=True)
	ot_canales_conocen = fields.Text(string='Especificar si ya se conocen', track_visibility=True)
	ot_observacion = fields.Text()
	tabla_ot = fields.One2many('mod.ot.tbl', 'id_ot_tbl', ondelete="cascade", track_visibility=True)
	ot_indicar_rotacion = fields.Text(string="Indicar rotación", track_visibility=True)

	regulacion_cofepris = fields.Boolean(string="COFEPRIS", track_visibility=True)
	regulacion_favor = fields.Boolean(string="A favor de lo mejor", track_visibility=True)
	regulacion_kids = fields.Boolean(string="Kids policy", track_visibility=True)

	spot_regulacion_cofepris = fields.Boolean(string="COFEPRIS", track_visibility=True)
	spot_regulacion_favor = fields.Boolean(string="A favor de lo mejor", track_visibility=True)
	spot_regulacion_kids = fields.Boolean(string="Kids policy", track_visibility=True)

	an_otra_cat = fields.Char(string="Otra categoria")

	nt_regulacion_cofepris = fields.Boolean(string="COFEPRIS", track_visibility=True)
	nt_regulacion_favor = fields.Boolean(string="A favor de lo mejor", track_visibility=True)
	nt_regulacion_kids = fields.Boolean(string="Kids policy", track_visibility=True)

	target_tvsa = fields.Char(string="Target", track_visibility=True)

	aaee_marca_producto = fields.Char(related="crm_odt_id.marca.name", string="Marca o producto", track_visibility=True)
	aaee_inversion = fields.Float(string="Inversión", track_visibility=True)

	telenovelas_bool = fields.Boolean(string='Telenovelas', track_visibility=True)
	tvsa_requerir_especificaciones = fields.Text(string='', track_visibility=True)
	tvsa_abierta_observaciones_dos = fields.Text(string='', track_visibility=True)

	tvsa_local_rotacion = fields.Char(string="Indicar rotación", track_visibility=True)
	tvsa_local_rotacion_dos = fields.Char(string="Indicar rotación", track_visibility=True)
	tvsa_local_regulacion_cofepris = fields.Boolean(string="COFEPRIS", track_visibility=True)
	tvsa_local_regulacion_favor = fields.Boolean(string="A favor de lo mejor", track_visibility=True)
	tvsa_local_regulacion_kids = fields.Boolean(string="Kids policy", track_visibility=True)

	ir_network = fields.Char(string="Indicación de rotación", track_visibility=True)
	rad_ir = fields.Char(string="Indicación de rotación", track_visibility=True)

	tabla_box_bool = fields.One2many('mod.box.tbl', 'id_box_tbl', ondelete="cascade", track_visibility=True)
	tabla_canal5_bool = fields.One2many('mod.canal5.tbl', 'id_canal5_tbl', ondelete="cascade", track_visibility=True)
	tabla_comedia_bool = fields.One2many('mod.come.tbl', 'id_comedia_tbl', ondelete="cascade", track_visibility=True)
	tabla_enlatados_bool = fields.One2many('mod.enlatados.tbl', 'id_enlatados_tbl', ondelete="cascade", track_visibility=True)
	tabla_revista_bool = fields.One2many('mod.revista.tbl', 'id_revista_tbl', ondelete="cascade", track_visibility=True)
	tabla_deportivos_bool = fields.One2many('mod.deportivos.tbl', 'id_deportivos_tbl', ondelete="cascade", track_visibility=True)
	tabla_lucha_bool = fields.One2many('mod.lucha.tbl', 'id_lucha_tbl', ondelete="cascade", track_visibility=True)
	tabla_noticieros_bool = fields.One2many('mod.noticieros.tbl', 'id_noticieros_tbl', ondelete="cascade", track_visibility=True)
	tabla_telenovelas_bool = fields.One2many('mod.telenovelas.tbl', 'id_telenovelas_tbl', ondelete="cascade", track_visibility=True)

	nt_tabla_net =fields.One2many('mod.net.tbl', 'id_net_tbl', ondelete="cascade", track_visibility=True)

	tvsa_primario = fields.Char(string="TERGET PRIMARIO CREADO", compute="_get_valor_primario", track_visibility=True)
	tvsa_marca_pro = fields.Char(related="crm_odt_id.marca.name", string="Marca o producto", track_visibility=True)
	tvsa_marca_pro_nac = fields.Char(related="crm_odt_id.marca.name", string="Marca o producto", track_visibility=True)

	sc_inversion = fields.Float(string="Inversión", track_visibility=True)
	sc_indicar_rotacion = fields.Text(string="Indicar rotación", track_visibility=True)
	sc_cobertura = fields.Selection([('1','Nacional'),('2','Local')], string="Cobertura", track_visibility=True)
	sc_local = fields.Char(string="Plazas", track_visibility=True)

	nt_inversion = fields.Float(string="Inversión", track_visibility=True)
	nt_conoce_programas = fields.Char(string='Si conoce el(los) programa(s) indicar', track_visibility=True)
	#nt_cofepris = fields.Selection([('1','COFEPRIS'),('2','A favor de lo mejor'),('3','Kids policy')],string=' ', track_visibility=True)
	nt_observacion = fields.Char(string=" ", track_visibility=True)
	nt_rot_indicar = fields.Char(string="Indicar rotación")

	#-- FUNCION PARA OBTENER EL VALOR EN AUTOMATICO DEL CAMPO PRIMARIO --#
	@api.depends('years_03','years_48','years_912','tvsa_rol_family','tvsa_sexo','tvsa_nse_1','tvsa_nse_2','tvsa_nse_3','tvsa_nse_4','tvsa_grupo_edad_1','tvsa_grupo_edad_2','tvsa_grupo_edad_3','tvsa_grupo_edad_4','tvsa_grupo_edad_5','tvsa_grupo_edad_6','tvsa_grupo_edad_otro')
	def _get_valor_primario(self):
		sexo = ""
		ge_1 = ""
		ge_2 = ""
		ge_3 = ""
		ge_4 = ""
		ge_5 = ""
		ge_6 = ""
		ge_otro = ""
		nse_1 = ""
		nse_2 = ""
		nse_3 = ""
		nse_4 = ""
		rol = ""
		rn = ""
		rn2 = ""
		rn3 = ""

		if self.tvsa_sexo:
			if self.tvsa_sexo == '1':
				sexo = 'Personas'
			elif self.tvsa_sexo == '2':	
				sexo = 'Mujeres'
			else:
				sexo = 'Hombres'

		if self.tvsa_grupo_edad_1 == True:
			if self.tvsa_sexo :
				ge_1 = ', 4-12'
			else:
				ge_1 = '4-12'
		if self.tvsa_grupo_edad_2 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True:
				ge_2 = ',  13-18'
			else:
				ge_2 = '13-18'
		if self.tvsa_grupo_edad_3 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True:
				ge_3 = ',  19-29'
			else:
				ge_3 = '19-29'
		if self.tvsa_grupo_edad_4 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True:
				ge_4 = ',  30-44'
			else:
				ge_4 = '30-44'
		if self.tvsa_grupo_edad_5 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True:
				ge_5 = ',  45-54'
			else:
				ge_5 = '45-54'	
		if self.tvsa_grupo_edad_6 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True:
				ge_6 = ',  55+'
			else:
				ge_6 = '55+'
		if self.tvsa_grupo_edad_otro:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True:
				ge_otro = ',  ' + self.tvsa_grupo_edad_otro
			else:	
				ge_otro = self.tvsa_grupo_edad_otro

		if self.tvsa_nse_1 == True:
			if self.tvsa_sexo or self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True:
				nse_1 = ", ABC+"
			else:
				nse_1 = "ABC+"
		if self.tvsa_nse_2 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True or self.tvsa_nse_1 == True:
				nse_2 = ",  C"
			else:
				nse_2 = "C"
		if self.tvsa_nse_3 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True or self.tvsa_nse_1 == True or self.tvsa_nse_2 == True:
				nse_3 = ",  D+"
			else:
				nse_3 = "D+"
		if self.tvsa_nse_4 == True:
			if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True or self.tvsa_nse_1 == True or self.tvsa_nse_2 == True or self.tvsa_nse_3 == True:
				nse_4 = ",  DE"
			else:	
				nse_4 = "DE"

		if self.tvsa_rol_family:
			if self.tvsa_rol_family == '1':
				if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True or self.tvsa_nse_1 == True or self.tvsa_nse_2 == True or self.tvsa_nse_3 == True or self.tvsa_nse_4 == True:
					rol = ', Jefes de Familia'
				else:
					rol = 'Jefes de Familia'	
			elif self.tvsa_rol_family == '2':
				if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True or self.tvsa_nse_1 == True or self.tvsa_nse_2 == True or self.tvsa_nse_3 == True or self.tvsa_nse_4 == True:
					rol = ', Amas de casa'
				else:
					rol = 'Amas de casa'
			else:
				if self.tvsa_sexo or self.tvsa_grupo_edad_1 == True or self.tvsa_grupo_edad_2 == True or self.tvsa_grupo_edad_3 == True or self.tvsa_grupo_edad_4 == True or self.tvsa_grupo_edad_5 == True or self.tvsa_grupo_edad_6 == True or self.tvsa_grupo_edad_otro == True or self.tvsa_nse_1 == True or self.tvsa_nse_2 == True or self.tvsa_nse_3 == True or self.tvsa_nse_4 == True:
					rol = ', Responsables de niños:'
				else:
					rol = 'Responsables de niños: '	

		if self.years_03 == True:
			rn = ' 0 a 3 años'
		if self.years_48 == True:
			if self.years_03 == True:
				rn2 = ', 4 a 8 años'
			else:
				rn2 = ' 4 a 8 años'	
		if self.years_912 == True:
			if self.years_03 == True or self.years_48 == True:
				rn3 = ', 9 a 12 años'
			else:
				rn3 = ' 9 a 12 años'	

		self.tvsa_primario = sexo + ge_1 + ge_2 + ge_3 + ge_4 + ge_5 + ge_6 + ge_otro + nse_1 + nse_2 + nse_3 + nse_4 + rol + rn + rn2 + rn3
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
	box_especificar_aaee = fields.Selection([('1','Super'),('2','Banner'),('3','Mención 10"'),('4','Mención 20"'),('5','Cortinilla a corte'),('6','Patrocinio de programa'),('7','Patrocinio de sección')], string="Especificar AAEE")

class ModCanal5Tbl(models.Model):
	_name = "mod.canal5.tbl"

	id_canal5_tbl = fields.Many2one('odt.medios')
	canal5_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	canal5_programa = fields.Char(string="Programa")
	canal5_genero = fields.Char(string="Genero", default="Caricaturas, películas y series")
	canal5_duracion = fields.Char(string="Duración")
	canal5_especificar_aaee = fields.Selection([('1','Edición creativa'),('2','Cortinilla a corte'),('3','L en contenido'),('4','Patrocinio de programa'),('5','Promos vea'),('6','Social TV'),('7','BUG (Logo)')], string="Especificar AAEE")

class ModComediaTbl(models.Model):
	_name = "mod.come.tbl"

	id_comedia_tbl = fields.Many2one('odt.medios')
	comedia_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	comedia_programa = fields.Char(string="Programa")
	comedia_genero = fields.Char(string="Genero", default="Comedia")
	comedia_duracion = fields.Char(string="Duración")
	comedia_especificar_aaee = fields.Selection([('1','Cortinilla a corte'),('2','Avance del programa'),('3','Patrocinio de programa')], string="Especificar AAEE")

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
								('6','Mención 120"'),('7','Promos vea'),('8','Patrocinio de programa'),('9','Patrocinio de sección'),
								('10','Entrevista 60"'),('11','Entrevista 120"'),('12','Bumper'),('13','Wiper')], string="Especificar AAEE")

class ModDeportivosTbl(models.Model):
	_name = "mod.deportivos.tbl"

	id_deportivos_tbl = fields.Many2one('odt.medios')
	deportivos_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	deportivos_programa = fields.Char(string="Programa")
	deportivos_genero = fields.Char(string="Genero", default="Deportivos")
	deportivos_duracion = fields.Char(string="Duración")
	deportivos_especificar_aaee = fields.Selection([('1','Pleca'),('2','Super'),('3','Banner'),('4','Cortinilla a corte'),
											 		('5','Promos vea'),('6','Mención 30"'),('7','Mención 60"'),('8','Patrocinio de sección'),('9','Patrocinio de sección con pie'),('10','Patrocinio de programa')], string="Especificar AAEE")
class ModLuchaTbl(models.Model):
	_name = "mod.lucha.tbl"

	id_lucha_tbl = fields.Many2one('odt.medios')
	lucha_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	lucha_programa = fields.Char(string="Programa")
	lucha_genero = fields.Char(string="Genero", default="Lucha Libre")
	lucha_duracion = fields.Char(string="Duración")
	lucha_especificar_aaee = fields.Selection([('1','Super'),('2','Banner'),('3','Mención 10"'),('4','Mención 30"'),('5','Mención 60"'),('6','Mención 120"'),('7','Cortinilla a corte'),
									('8','Patrocinio de programa'),('9','Patrocinio de sección'),('10','Patrocinio de sección con pie')], string="Especificar AAEE")

class ModNoticierosTbl(models.Model):
	_name = "mod.noticieros.tbl"

	id_noticieros_tbl = fields.Many2one('odt.medios')
	noticieros_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	noticieros_programa = fields.Char(string="Programa")
	noticieros_genero = fields.Char(string="Genero", default="Noticieros")
	noticieros_duracion = fields.Char(string="Duración")
	noticieros_especificar_aaee = fields.Selection([('1','Pleca'),('2','Super'),('3','Banner'),('4','Cortinilla a corte'),('5','Promos vea'),('6','Avance del programa'),
								 ('7','Patrocinio de programa'),('8','Patrocinio de sección'),('9','Resumen informativo')], string="Especificar AAEE")

class ModTelenovelasTbl(models.Model):
	_name = "mod.telenovelas.tbl"

	id_telenovelas_tbl = fields.Many2one('odt.medios')
	telenovelas_canal = fields.Selection([('1','2'),('2','5'),('3','9')], string="Canal")
	telenovelas_programa = fields.Char(string="Programa")
	telenovelas_genero = fields.Char(string="Genero", default="Telenovelas")
	telenovelas_duracion = fields.Char(string="Duración")
	telenovelas_especificar_aaee = fields.Selection([('1','Cortinilla a corte'),('2','Cortinilla argumental'),('3','Promos vea'),('4','Patrocinio avances'),('5','Integración ambiental'),('6','Integración activa'),('7','Integración argumental')], string="Especificar AAEE")

class ModNetTbl(models.Model):
	_name = "mod.net.tbl"

	id_net_tbl = fields.Many2one('odt.medios')
	nt_network_tbl = fields.Char(string="Network")
	nt_tipo_actividad_tbl = fields.Selection([('1','Spoteo'),('2','Acciones especiales')], string="Tipo actividad")
	nt_duracion_tbl = fields.Char(string="Duración")
	nt_programa_tbl= fields.Char(string="Programa")
	nt_especificar_aaee_tbl = fields.Char(string="Especificar AAEE")

class ModOtTbl(models.Model):
	_name = "mod.ot.tbl"

	id_ot_tbl = fields.Many2one('odt.medios')
	ot_ta = fields.Selection([('1','Acciones especiales'),('2','Spoteo')], string="Tipo de actividad")
	ot_dura = fields.Char(string="Duración")
	ot_eaaee = fields.Char(string="Especificar AAEE (Sujeto a consulta con cada network)")

