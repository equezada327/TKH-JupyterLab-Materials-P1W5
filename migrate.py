# migrate.py — adds new barcode and price columns to the existing products table.
# Equivalent to running the ALTER TABLE commands in SQLTools.
# My SQL Lite stopped working. It froze and wouldn't let me run a new connection. 

import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Add barcode column
try:
    cursor.execute("ALTER TABLE products ADD COLUMN barcode INT")
    print("✓ Added barcode column")
except sqlite3.OperationalError as e:
    print(f"barcode: {e}")

# Add price column
try:
    cursor.execute("ALTER TABLE products ADD COLUMN price VARCHAR(255)")
    print("✓ Added price column")
except sqlite3.OperationalError as e:
    print(f"price: {e}")

conn.commit()
conn.close()
print("Migration complete.")