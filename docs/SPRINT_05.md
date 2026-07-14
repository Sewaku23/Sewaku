# Sprint 5 - Rental System

## Tujuan

Membangun sistem penyewaan yang dapat digunakan sebagai sumber data sistem rekomendasi.

---

## Business Rules

1. Produk tidak dapat disewa jika stok habis.

2. Jumlah penyewaan tidak boleh melebihi stok.

3. Tanggal kembali harus lebih besar dari tanggal sewa.

4. Status Pending tidak mengurangi stok.

5. Status On Rent mengurangi stok.

6. Status Returned menambah stok.

7. Rental Completed masuk ke History Rental.

---

## Workflow

Login

↓

Pilih Produk

↓

Checkout

↓

Pending

↓

Confirmed

↓

On Rent

↓

Returned

↓

Completed

↓

Recommendation


## Sprint 5.6

### Tujuan

Menghitung subtotal dan total transaksi secara otomatis.

### Rumus

Subtotal

Harga × Qty × Lama Sewa

Total

Σ Semua Subtotal

## Sprint 5.7

### Stock Management

Business Rule:

- Pending → Stock tetap.
- Confirmed → Stock tetap.
- On Rent → Stock berkurang.
- Returned → Stock bertambah.

Alasan:

Barang dianggap keluar gudang saat benar-benar dipinjam.