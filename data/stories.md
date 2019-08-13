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