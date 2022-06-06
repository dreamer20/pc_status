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
    disk_space_total TEXT,
    disk_space_available TEXT,
    uptime TEXT,
    load_average TEXT,
    last_update TEXT,
    volume_level INTEGER,
    process_count INTEGER,
    keyboard_layout TEXT
);