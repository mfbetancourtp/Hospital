CREATE TABLE empleados(
	id_empleado INT PRIMARY KEY,
	nombres 	VARCHAR(50),
	apellidos	VARCHAR(20),
	cedula		VARCHAR(12),
	correo		VARCHAR(30),
	celular		VARCHAR(10),
	direccion	VARCHAR(100),
	cargo		VARCHAR(15),
	contrasena	VARCHAR(15)
);

CREATE TABLE pacientes(
	id_paciente  			INT PRIMARY KEY,
	fecha_ingreso           DATE,
	nombres  				VARCHAR(50), 
	apellidos				VARCHAR(50), 
	tipo_de_identificacion 	VARCHAR(50), 
	nro_identificacion 		VARCHAR(50),
	direccion  				VARCHAR(50),
	correo  				VARCHAR(50),
	celular 				VARCHAR(50),
	familiar_asignado  		INT,
	contrasena  			VARCHAR(50),
	medico_asignado  		INT,
	
	FOREIGN KEY (medico_asignado) REFERENCES empleados(id_empleado)
	FOREIGN KEY (familiar_asignado) REFERENCES familiares(id_familiar)
 );

CREATE TABLE familiares (
	id_familiar  			INT PRIMARY KEY,
	nombres  				VARCHAR(50), 
	apellidos				VARCHAR(50), 
	celular 				VARCHAR(50),
	correo 				    VARCHAR(50), 	
	genero  				VARCHAR(50),
	parentesco              VARCHAR(50),
    id_paciente             INT,

	FOREIGN KEY (paciente_familiar) REFERENCES pacientes(id_paciente)
 );

CREATE TABLE signosvitales(
	fecha 					DATE,
	oximentria 				INT,
    frecuencia_respiratoria INT,
    frecuencia_cardiaca 	INT,
    temperatura 			INT,
    presion_arterial 		VARCHAR(10),
   	glicemia 				INT,
	paciente 				INT,

    foreign key (paciente) references pacientes(id_paciente)
);

CREATE TABLE historia_clinica(
	 id_hc         	INT PRIMARY KEY,
	 fecha 			VARCHAR(10),
	 cod_patologia 	VARCHAR(10),
	 medico 		INT,
	 paciente		INT,
	 tratamiento 	TEXT,
	 cuidados 		TEXT,
	 
	 FOREIGN KEY(paciente) REFERENCES Pacientes(id_paciente),
	 FOREIGN KEY(medico) REFERENCES Empleados(id_empleado)
);