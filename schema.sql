-- Main table for tracking camera issues
CREATE TABLE Tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    camera_id TEXT NOT NULL,
    location TEXT NOT NULL,
    zone TEXT,
    downtime INTEGER NOT NULL,
    latitude REAL,
    longitude REAL,
    status TEXT DEFAULT 'offline',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Security table for compliance
CREATE TABLE Audit_Logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    action_type TEXT NOT NULL,
    target_id TEXT,
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
