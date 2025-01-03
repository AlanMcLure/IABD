CREATE TABLE Tipos_Encuestas ( 
  id_tipo  Integer,  
  descripcion  varchar(150)
); 

CREATE TABlE Encuestas (
  id_encuesta  Integer,
  id_tipo  Integer,
  completada  date,  
  id_familia  integer,  
  id_dpto  integer,
  id_curso  integer
);

CREATE TABLE Preguntas ( 
  id_pregunta  Integer,  
  id_tipo  Integer,
  descripcion  varchar(150)
); 

CREATE TABLE Respuestas (
  id_respuesta  Integer,
  id_pregunta  Integer,
  id_encuesta  Integer,
  valor text
);

CREATE TABLE Departamentos (
  id_dpto  Integer,
  departamento  varchar(30)
);

CREATE TABLE Familias (  
  id_familia  Integer,
  familia  varchar(30)
); 

CREATE TABLE Cursos (
  id_curso  Integer,
  curso  varchar(30)
);

