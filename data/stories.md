##General_Saludar
* General_Saludo
    - utter_General_Saludo


##General_Despedida    
* General_Despedida
    - utter_General_Despedida
    - action_restart

##General_ActualizarDatos
* General_ActualizarDatos
    - utter_General_ActualizarDatos

##General_ActualizarDatosNoSoy
* General_ActualizarDatosNoSoy
    - utter_General_ActualizarDatosNoSoy
    - slot{"nombreCompleto": "JUAN PEREZ"}
    - slot{"identificacion": "98765432"}

##Afiliaciones_ConocerCategoria
* Afiliaciones_ConocerCategoria
    - utter_Afiliaciones_ConocerCategoria
    - custAction_Afiliaciones_ConsultarCategoriaXIdentificacion
    - slot{"direccion": "CL x B y B 90 INT 1 APTO 1"}
    - slot{"celular": "3003012345"}
    - slot{"nombreCompleto": "JUAN PEREZ"}
    - slot{"identificacion": "98765432"}
    - slot{"categoria": ""}


##Afiliaciones_ConocerCategoriaXIdentificacion
* Afiliaciones_ConocerCategoriaXIdentificacion
    - slot{"direccion": "CL x B y B 90 INT 1 APTO 1"}
    - slot{"celular": "3003012345"}
    - slot{"nombreCompleto": "JUAN PEREZ"}
    - slot{"identificacion": "98765432"}
    - slot{"categoria": ""}
    - utter_Afiliaciones_ConsultarCategoriaXIdentificacion 
    - action_listen
    - custAction_Afiliaciones_ConsultarCategoriaXIdentificacion

##Afiliaciones_Invitados
* Afiliaciones_Invitados
    - utter_Afiliaciones_Invitados

##Afiliaciones_AsignacionCategoria
* Afiliaciones_AsignacionCategoria
    - utter_Afiliaciones_AsignacionCategoria

##Afiliaciones_AQuienAfiliar
* Afiliaciones_AQuienAfiliar
    - utter_Afiliaciones_AQuienAfiliar

##Afiliaciones_ComoPuedoAfiliarBeneficiarios
* Afiliaciones_ComoPuedoAfiliarBeneficiarios
    - utter_Afiliaciones_ComoPuedoAfiliarBeneficiarios

##Afiliaciones_MediosConsultarGrupoFamiliar
* Afiliaciones_MediosConsultarGrupoFamiliar
    - utter_Afiliaciones_MediosConsultarGrupoFamiliar

##Afiliaciones_AfiliacionCosto
* Afiliaciones_AfiliacionCosto
    - utter_Afiliaciones_AfiliacionCosto

##AlimentosBebidas_PlanesIncluyenBebidas
* AlimentosBebidas_PlanesIncluyenBebidas
    - utter_AlimentosBebidas_PlanesIncluyenBebidas
##AlimentosBebidas_TipoAlimentacion
* AlimentosBebidas_TipoAlimentacion
    -utter_AlimentosBebidas_TipoAlimentacion

##AlimentosBebidas_PlatosCarta
* AlimentosBebidas_PlatosCarta
    -utter_AlimentosBebidas_PlatosCarta

##AlimentosBebidas_MenuInfantil
* AlimentosBebidas_MenuInfantil
    - utter_AlimentosBebidas_MenuInfantil

##AlimentosBebidas_HorarioComidasLagomar
* AlimentosBebidas_HorarioComidasLagomar
    - utter_AlimentosBebidas_HorarioComidasLagomar

##AlimentosBebidas_HorarioComidasLagosol
* AlimentosBebidas_HorarioComidasLagosol
    - utter_AlimentosBebidas_HorarioComidasLagosol

##AlimentosBebidas_VendenBebidasAlcoholicas
* AlimentosBebidas_VendenBebidasAlcoholicas
    - utter_AlimentosBebidas_VendenBebidasAlcoholicas

##Canal_HorarioChat
* Canal_HorarioChat
    - utter_Canal_HorarioChat

##Canal_OficinasHorarios
* Canal_OficinasHorarios
    - utter_Canal_OficinasHorarios

##Canal_horarioLineaTelefonica
* Canal_horarioLineaTelefonica
    - utter_Canal_horarioLineaTelefonica

##Default
* Default
    - utter_Default

##Pagos_TiempoPagoReserva
* Pagos_TiempoPagoReserva
    - utter_Pagos_TiempoPagoReserva

##Pagos_MediosPagosReserva
* Pagos_MediosPagosReserva
    - utter_Pagos_MediosPagosReserva

##Pagos_PagarConLibranzaNomina
* Pagos_PagarConLibranzaNomina
    - utter_Pagos_PagarConLibranzaNomina

##Planes_PlanesNavidadFinDeAnio
* Planes_PlanesNavidadFinDeAnio
    - utter_Planes_PlanesNavidadFinDeAnio

##Reservas_MediosHacerReserva
* Reservas_MediosHacerReserva
    - utter_Reservas_MediosHacerReserva