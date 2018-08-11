CREATE TABLE events (
id INTEGER PRIMARY KEY,
schedule_id INTEGER NOT NULL,
name VARCHAR(255) NOT NULL,
start_time VARCHAR(5), -- HH:MM
end_time VARCHAR(5), -- HH:MM
FOREIGN KEY(schedule_id) REFERENCES schedules(id)
);

CREATE TABLE schedules (
id INTEGER PRIMARY KEY,
name VARCHAR(255),
date VARCHAR(10) -- YYYY-MM-DD
);
