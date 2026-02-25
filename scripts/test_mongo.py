from pymongo import MongoClient

uri = "mongodb+srv://bd-230104040124:bdasik@cluster0.sebkmkj.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    # Force connection test
    client.admin.command('ping')
    print("[OK] Koneksi ke MongoDB Atlas berhasil!")
    print("Database yang tersedia:")
    for db_name in client.list_database_names():
        print(f"  - {db_name}")
except Exception as e:
    print("[GAGAL] Koneksi gagal:", e)