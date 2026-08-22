import csv

from pathlib import Path

import psycopg


DB_CONFIG = {
    "host": "db",
    "port": 5432,
    "dbname": "prime_bank",
    "user": "postgres",
    "password": "postgres",
}

CSV_FILES = {
    "branch": "branches.csv",
    "customer": "customers.csv",
    "account": "accounts.csv",
}

DATASET_DIR = Path(__file__).resolve().parent.parent / "dataset"

for table, file in CSV_FILES.items():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            filepath = DATASET_DIR / file
            with open(filepath, encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                columns = reader.fieldnames

                if not columns:
                    raise ValueError("CSV has no columns.")

                column_sql = ", ".join(columns)

                if file in ["branches.csv", "customers.csv"]:
                    column_sql += ", is_active"
                    columns.append("is_active")

                placeholders = ", ".join(["%s"] * len(columns))

                sql = f"""
                    INSERT INTO {table} ({column_sql})
                    VALUES ({placeholders})
                """

                for row in reader:
                    values = [
                        True if column == "is_active" else row[column]
                        for column in columns
                    ]
                    cur.execute(sql, values)
        conn.commit()
