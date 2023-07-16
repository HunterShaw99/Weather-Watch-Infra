CREATE DATABASE ww;
CREATE SCHEMA app;

CREATE TABLE app.users (
    id bigserial NOT NULL,
    "user_email" text NULL,
    "f_name" text NULL,
    "l_name" text NULL,
    "phone_num" text NULL,
    "street" text NULL,
    "zip" text NULL,
    "city" text NULL,
    "state" text NULL,
    "GUID" text,
    "usr_hash" text,
    PRIMARY KEY(id)
);

CREATE UNIQUE INDEX id_idx ON app.users (id);

CREATE TABLE app.loc (
    id bigint NOT NULL,
    "lat" text NULL,
    "lon" text NULL,
    "zip" text,
    PRIMARY KEY(id)
);
