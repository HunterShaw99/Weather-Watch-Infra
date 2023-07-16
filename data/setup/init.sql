CREATE DATABASE ww;
CREATE SCHEMA app;

CREATE TABLE app.users (
    "u_id" bigserial NOT NULL,
    "user_email" text NULL,
    "f_name" text NULL,
    "l_name" text NULL,
    "phone_num" text NULL,
    "u_GUID" text,
    "usr_hash" text,
    "create_date" timestamp,
    PRIMARY KEY("u_GUID")
);
CREATE UNIQUE INDEX user_email_idx ON app.users ("user_email");

CREATE TABLE app.loc (
    id bigint NOT NULL,
    "lat" text NULL,
    "lon" text NULL,
    "zip" text,
    "ping_date" timestamp,
    PRIMARY KEY(id)
);

CREATE SCHEMA pur;

CREATE TABLE pur.purchases (
    "p_id" bigserial NOT NULL,
    "u_GUID" text NOT NULL,
    "p_UID" text,
    "purchase_date" timestamp,
    "active" boolean,
    "curr_sub" timestamp,
    "next_sub" timestamp,
    PRIMARY KEY("p_UID"),
    CONSTRAINT fk_id
        FOREIGN KEY("u_GUID")
            REFERENCES app.users("u_GUID")
);
