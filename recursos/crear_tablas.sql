 CREATE TABLE conceptos
  (
     id_concepto      SERIAL PRIMARY KEY,
     simbolo_concepto VARCHAR(200) UNIQUE
  );

CREATE TABLE relaciones
  (
     id_relacion      SERIAL PRIMARY KEY,
     simbolo_relacion VARCHAR(200) UNIQUE
  );

CREATE TABLE contextos
  (
     id_contexto     SERIAL PRIMARY KEY,
     nombre_contexto VARCHAR(200) UNIQUE
  );

CREATE TABLE ternas_conocimiento
  (
     id_terna    SERIAL PRIMARY KEY,
     id_origen   INT REFERENCES conceptos(id_concepto),
     id_relacion INT REFERENCES relaciones(id_relacion),
     id_destino  INT REFERENCES conceptos(id_concepto),
     CONSTRAINT terna_unica UNIQUE(id_origen, id_relacion, id_destino)
  );

CREATE TABLE contexto_tiene_terna
  (
     id_contexto INT REFERENCES contextos(id_contexto),
     id_terna    INT REFERENCES ternas_conocimiento(id_terna),
     PRIMARY KEY(id_contexto, id_terna)
  )  




