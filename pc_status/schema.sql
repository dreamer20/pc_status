DROP TABLE IF EXISTS pc_status;

CREATE TABLE pc_status (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cur_date INTEGER NOT NULL,
    cpu_temp REAL,
    ssd_temp REAL,
    cpu_fan INTEGER,
    add_fan INTEGER,
    ram_total INTEGER,
    ram_available INTEGER,
    disk_space_total INTEGER,
    disk_space_available INTEGER,
    uptime TEXT,
    load_average TEXT,
    last_update TEXT,
    process_count INTEGER
);

CREATE TABLE total_uptime (
    total_uptime INTEGER
);

INSERT INTO total_uptime VALUES (0);