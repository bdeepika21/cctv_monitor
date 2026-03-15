import sqlite3

def log_fault(camera_id, location, zone, downtime):
    conn = sqlite3.connect('cctv_monitor.db')
    cursor = conn.cursor()

    # 1. Log the Ticket
    ticket_sql = "INSERT INTO Tickets (camera_id, location, zone, downtime) VALUES (?, ?, ?, ?)"
    cursor.execute(ticket_sql, (camera_id, location, zone, downtime))

    # 2. Log the Audit Trail (for Security)
    audit_sql = "INSERT INTO Audit_Logs (user_name, action_type, target_id) VALUES (?, ?, ?)"
    cursor.execute(audit_sql, ("System_Automator", "AUTO_FAULT_DETECT", camera_id))

    conn.commit()
    conn.close()
    print(f"✅ Fault logged for {camera_id} in {zone} zone.")

# Simulation: Checking a broken camera
log_fault("CAM-RRR-001", "Main Gate", "East", 15)
