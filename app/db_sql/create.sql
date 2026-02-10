create table if not exists tasks (
id serial primary key,
title TEXT not null,
description TEXT,
category VARCHAR(20),
difficulty VARCHAR(20),
priority VARCHAR(20),
status VARCHAR(20) not null default 'in progress',
created_at TIMESTAMP not null default CURRENT_TIMESTAMP,
last_updated TIMESTAMP,
due_to DATE 
);


create table if not EXISTS task_time_logs (
id serial primary key,
task_id integer references tasks(id),
started_at timestamp,
ended_at timestamp null,
duration_sec integer null
)

