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

##Reservas_Requisitos_RealizarReserva
* Reservas_Requisitos_RealizarReserva
    - utter_Reservas_Requisitos_RealizarReserva

##Reservas_CambiosReserva
* Reservas_CambiosReserva
    - utter_Reservas_CambiosReserva

##Reservas_ProblemasPortalReservas
* Reservas_ProblemasPortalReservas
    - utter_Reservas_ProblemasPortalReservas

##Reservas_MediosCancelacionReservas
* Reservas_MediosCancelacionReservas
    - utter_Reservas_MediosCancelacionReservas

##Reservas_MotivoCancelacionReserva
* Reservas_MotivoCancelacionReserva
    - utter_Reservas_MotivoCancelacionReserva

##Reservas_CambiosConservandoTarifa
* Reservas_CambiosConservandoTarifa
    - utter_Reservas_CambiosConservandoTarifa

##Reservas_CancelarReactivarReserva
* Reservas_CancelarReactivarReserva
    - utter_Reservas_CancelarReactivarReserva

##Reservas_PlanearEsAhorrar
* Reservas_PlanearEsAhorrar
    - utter_Reservas_PlanearEsAhorrar

##Reservas_EdadPagoNiños
* Reservas_EdadPagoNiños
    - utter_Reservas_EdadPagoNiños

##Reservas_CostoHospedaje
* Reservas_CostoHospedaje
    - utter_Reservas_CostoHospedaje

##Reservas_DisponibilidadTarifas
* Reservas_DisponibilidadTarifas
    - utter_Reservas_DisponibilidadTarifas

##Reservas_CederReserva
* Reservas_CederReserva
    - utter_Reservas_CederReserva

##Reservas_LimiteAcompañantes
* Reservas_LimiteAcompañantes
    - utter_Reservas_LimiteAcompañantes

##SobreHoteles_UbicacionHoteles
* SobreHoteles_UbicacionHoteles
    - utter_SobreHoteles_UbicacionHoteles

##SobreHoteles_DocumentosParaCheckIn
* SobreHoteles_DocumentosParaCheckIn
    - utter_SobreHoteles_DocumentosParaCheckIn

##SobreHoteles_HorarioIngresoHoteles
* SobreHoteles_HorarioIngresoHoteles
    - utter_SobreHoteles_HorarioIngresoHoteles

##SobreHoteles_TransporteHoteles
* SobreHoteles_TransporteHoteles
    - utter_SobreHoteles_TransporteHoteles

##SobreHoteles_PermiteIngresoAlimentos
* SobreHoteles_PermiteIngresoAlimentos
    - utter_SobreHoteles_PermiteIngresoAlimentos

##SobreHoteles_IngresoMascotas
* SobreHoteles_IngresoMascotas
    - utter_SobreHoteles_IngresoMascotas

##SobreHoteles_PiscinaNiños
* SobreHoteles_PiscinaNiños
    - utter_SobreHoteles_PiscinaNiños

##SobreHoteles_HabitacionesAireAcondicionado
* SobreHoteles_HabitacionesAireAcondicionado
    - utter_SobreHoteles_HabitacionesAireAcondicionado

##SobreHoteles_ServicioParqueadero
* SobreHoteles_ServicioParqueadero
    - utter_SobreHoteles_ServicioParqueadero

##SobreHoteles_SillaDeRuedas
* SobreHoteles_SillaDeRuedas
    - utter_SobreHoteles_SillaDeRuedas

##SobreHoteles_PlanesRomanticos
* SobreHoteles_PlanesRomanticos
    - utter_SobreHoteles_PlanesRomanticos

##SobreHoteles_Lavanderia
* SobreHoteles_Lavanderia
    - utter_SobreHoteles_Lavanderia

 ##SobreHoteles_HotelTiendas
 * SobreHoteles_HotelTiendas
    - utter_SobreHoteles_HotelTiendas  

##SobreHoteles_CanchaTenis
* SobreHoteles_CanchaTenis
    - utter_SobreHoteles_CanchaTenis

##SobreHoteles_DeportesExtremos
* SobreHoteles_DeportesExtremos
    - utter_SobreHoteles_DeportesExtremos

##SobreHoteles_ServiciosAdicionales
* SobreHoteles_ServiciosAdicionales
    - utter_SobreHoteles_ServiciosAdicionales

##SobreHoteles_Enfermeria
* SobreHoteles_Enfermeria
    - utter_SobreHoteles_Enfermeria

##SobreHoteles_PiscinasHotel
* SobreHoteles_PiscinasHotel
    - utter_SobreHoteles_PiscinasHotel

##SobreHoteles_TVHabitacion
* SobreHoteles_TVHabitacion
    - utter_SobreHoteles_TVHabitacion

##SobreHoteles_HorarioRecepcion
* SobreHoteles_HorarioRecepcion
    - utter_SobreHoteles_HorarioRecepcion

##SobreHoteles_SalirHotel
* SobreHoteles_SalirHotel
    - utter_SobreHoteles_SalirHotel

##SobreHoteles_MaterialCanchaTenis
* SobreHoteles_MaterialCanchaTenis
    - utter_SobreHoteles_MaterialCanchaTenis

##SobreHoteles_NadarLago
* SobreHoteles_NadarLago
    - utter_SobreHoteles_NadarLago

##SobreHoteles_AlojamientoConAlimentacion
* SobreHoteles_AlojamientoConAlimentacion
    - utter_SobreHoteles_AlojamientoConAlimentacion

##SobreHoteles_TiposHabitacionLagosol
* SobreHoteles_TiposHabitacionLagosol
    - utter_SobreHoteles_TiposHabitacionLagosol

##SobreHoteles_CumpleañosLagosol
* SobreHoteles_CumpleañosLagosol
    - utter_SobreHoteles_CumpleañosLagosol

##SobreHoteles_TiposHabitacionLagomar
* SobreHoteles_TiposHabitacionLagomar
    - utter_SobreHoteles_TiposHabitacionLagomar

##SobreHoteles_CumpleañosLagomar
* SobreHoteles_CumpleañosLagomar
    - utter_SobreHoteles_CumpleañosLagomar

##SobreHoteles_WIFIHoteles
* SobreHoteles_WIFIHoteles
    - utter_SobreHoteles_WIFIHoteles

##AlimentosBebidas_ComidasRapidasLagomar
* AlimentosBebidas_ComidasRapidasLagomar
    - utter_AlimentosBebidas_ComidasRapidasLagomar

##AlimentosBebidas_SnaksBebidasLagomar
* AlimentosBebidas_SnaksBebidasLagomar
    - utter_AlimentosBebidas_SnaksBebidasLagomar

##SobreHoteles_GolfLagomar
* SobreHoteles_GolfLagomar
    - utter_SobreHoteles_GolfLagomar

##SobreHoteles_VoleyPlayaLagomar
* SobreHoteles_VoleyPlayaLagomar
    - utter_SobreHoteles_VoleyPlayaLagomar

##SobreHoteles_SalonJuegosLagomar
* SobreHoteles_SalonJuegosLagomar
    - utter_SobreHoteles_SalonJuegosLagomar

##SobreHoteles_CanopyLagomar
* SobreHoteles_CanopyLagomar
    - utter_SobreHoteles_CanopyLagomar

##SobreHoteles_SPALagomar
* SobreHoteles_SPALagomar
    - utter_SobreHoteles_SPALagomar

##SobreHoteles_PlayaLagomar
* SobreHoteles_PlayaLagomar   
    - utter_SobreHoteles_PlayaLagomar

##SobreHoteles_BolosLagomar
* SobreHoteles_BolosLagomar
    - utter_SobreHoteles_BolosLagomar

##SobreHoteles_FutbolLagomar
* SobreHoteles_FutbolLagomar
    - utter_SobreHoteles_FutbolLagomar

##SobreHoteles_FutbolLagosol
* SobreHoteles_FutbolLagosol
    - utter_SobreHoteles_FutbolLagosol

##SobreHoteles_SalonJuegosLagosol
* SobreHoteles_SalonJuegosLagosol
    - utter_SobreHoteles_SalonJuegosLagosol

##SobreHoteles_BicicletasAcuaticasLagosol
* SobreHoteles_BicicletasAcuaticasLagosol
    - utter_SobreHoteles_BicicletasAcuaticasLagosol

##SobreHoteles_CaminatasLagosol
* SobreHoteles_CaminatasLagosol
    - utter_SobreHoteles_CaminatasLagosol

##Pasadia_HorarioTransporteLagosol
* Pasadia_HorarioTransporteLagosol
    - utter_Pasadia_HorarioTransporteLagosol

##Pasadia_PrecioTransporteLagosol
* Pasadia_PrecioTransporteLagosol
    - utter_Pasadia_PrecioTransporteLagosol

##Pasadia_CondicionesRestriccionesTransporte
* Pasadia_CondicionesRestriccionesTransporte
    - utter_Pasadia_CondicionesRestriccionesTransporte

##Pasadia_TransporteNiños
* Pasadia_TransporteNiños
    - utter_Pasadia_TransporteNiños

##Pasadia_PasadiaLagosol
* Pasadia_PasadiaLagosol
    - utter_Pasadia_PasadiaLagosol

##Pasadia_RecomendacionesPasadia
* Pasadia_RecomendacionesPasadia
    - utter_Pasadia_RecomendacionesPasadia

##Tarifas_TarifasPasadiaPorCategoria
* Tarifas_TarifasPasadiaPorCategoria
    - utter_Tarifas_TarifasPasadiaPorCategoria

##Tarifas_TarifasLagomar
* Tarifas_TarifasLagomar
    - utter_Tarifas_TarifasLagomar

##Tarifas_TarifasLagosol
* Tarifas_TarifasLagosol
    - utter_Tarifas_TarifasLagosol

##Convenios_CajaSinFronteras
* Convenios_CajaSinFronteras
    - utter_Convenios_CajaSinFronteras

##Convenios_HotelesEstelar
* Convenios_HotelesEstelar
    - utter_Convenios_HotelesEstelar

##Convenios_ReservarHotelesEstelar
* Convenios_ReservarHotelesEstelar
    - utter_Convenios_ReservarHotelesEstelar

##CreditoTurismo_SobreCreditoTurismo
* CreditoTurismo_SobreCreditoTurismo
    - utter_CreditoTurismo_SobreCreditoTurismo

##CreditoTurismo_BeneficiosCreditoTurismo
* CreditoTurismo_BeneficiosCreditoTurismo
    - utter_CreditoTurismo_BeneficiosCreditoTurismo

##CreditoTurismo_RequisitosCreditoTurismo
* CreditoTurismo_RequisitosCreditoTurismo
    - utter_CreditoTurismo_RequisitosCreditoTurismo    

##CreditoTurismo_DocumentosCreditoTurismo
* CreditoTurismo_DocumentosCreditoTurismo
    - utter_CreditoTurismo_DocumentosCreditoTurismo

##CreditoTurismo_RealizarSolicitudCcredito
* CreditoTurismo_RealizarSolicitudCcredito
    - utter_CreditoTurismo_RealizarSolicitudCcredito

##CreditoTurismo_TiempoAprobacionCreditoTurismo
* CreditoTurismo_TiempoAprobacionCreditoTurismo
    - utter_CreditoTurismo_TiempoAprobacionCreditoTurismo

##CreditoTurismo_LibranzaCreditoTurismo
* CreditoTurismo_LibranzaCreditoTurismo
    - utter_CreditoTurismo_LibranzaCreditoTurismo

##CreditoTurismo_AgenciaViajes
* CreditoTurismo_AgenciaViajes
 - utter_CreditoTurismo_AgenciaViajes