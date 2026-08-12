import csv

import psycopg


CSV_FILE = "./dataset/branches.csv"

DB_CONFIG = {
    "host": "db",
    "port": 5432,
    "dbname": "prime_bank",
    "user": "postgres",
    "password": "postgres",
}

with psycopg.connect(**DB_CONFIG) as conn:
    with conn.cursor() as cur:
        with open(CSV_FILE, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                cur.execute(
                    """
                    INSERT INTO branch (id, name, city, state, opened_date, ifsc_code)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    (
                        row["branch_id"],
                        row["branch_name"],
                        row["city"],
                        row["state"],
                        row["opened_date"],
                        row["ifsc_code"],
                    ),
                )

    conn.commit()
