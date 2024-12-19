import sqlite3
def create_database():
    """
    Creates a SQLite database with a table to store job information.
    """
    conn = sqlite3.connect("upwork_jobs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            location TEXT NOT NULL,
            job_duration TEXT NOT NULL,
            salary TEXT
        )
    ''')
    conn.commit()
    conn.close()
def insert_job_data(job_title, company, direct_apply_url, salary, location):
    """
    Inserts job data into the database.
    """
    conn = sqlite3.connect("upwork_jobs.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT COUNT(*) FROM jobs WHERE job_title = ? AND company = ?
    ''', (job_title, company))

    result = cursor.fetchone()
    if result[0] > 0:
        print(f"Job already exists: {job_title} at {company}")
        return

    cursor.execute('''
        INSERT INTO jobs (job_title, company, direct_apply_url, salary, location)
        VALUES (?, ?, ?, ?, ?)
    ''', (job_title, company, direct_apply_url, salary, location))
    
    conn.commit()
    conn.close()
    print(f"Inserted: {job_title} at {company}")
