from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI(title="Sistem Koperasi API")

DB_FILE = "koperasi.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS anggota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            tglLahir TEXT,
            umur TEXT,
            alamat TEXT,
            telp TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

class Anggota(BaseModel):
    nama: str
    tglLahir: str
    umur: str
    alamat: str
    telp: str
    status: str

@app.get("/api/anggota")
def get_semua_anggota():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM anggota")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.post("/api/anggota")
def tambah_anggota(anggota: Anggota):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO anggota (nama, tglLahir, umur, alamat, telp, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (anggota.nama, anggota.tglLahir, anggota.umur, anggota.alamat, anggota.telp, anggota.status))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"message": "Anggota berhasil ditambahkan", "id": new_id, "status": anggota.status}

@app.put("/api/anggota/{id}")
def update_anggota(id: int, anggota: Anggota):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE anggota
        SET nama=?, tglLahir=?, umur=?, alamat=?, telp=?, status=?
        WHERE id=?
    ''', (anggota.nama, anggota.tglLahir, anggota.umur, anggota.alamat, anggota.telp, anggota.status, id))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Anggota tidak ditemukan")
    return {"message": "Data anggota diperbarui"}

@app.delete("/api/anggota/{id}")
def hapus_anggota(id: int):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM anggota WHERE id=?", (id,))
    conn.commit()
    rowcount = cursor.rowcount
    conn.close()
    if rowcount == 0:
        raise HTTPException(status_code=404, detail="Anggota tidak ditemukan")
    return {"message": "Data anggota dihapus"}

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
def read_root():
    return RedirectResponse(url="/static/form_anggota.html")
