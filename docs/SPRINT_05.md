# Sprint 5 Documentation -- Sewaku

## Sprint

Sprint 5 -- Payment System

## Objective

Membangun modul pembayaran yang terintegrasi dengan proses penyewaan
sehingga pengguna dapat memilih metode pembayaran, mengunggah bukti
transfer, atau melakukan pembayaran tunai, serta memberikan kemampuan
kepada admin untuk melakukan verifikasi pembayaran.

------------------------------------------------------------------------

## Features Completed

### 5.8.1 Payment Model

-   Menambahkan model `Payment`
-   Relasi One-to-One dengan `Rental`
-   Status pembayaran:
    -   Belum Dibayar
    -   Menunggu Verifikasi
    -   Disetujui
    -   Ditolak
    -   Dibatalkan
-   Metode pembayaran:
    -   Transfer
    -   Cash

### 5.8.2 Automatic Payment Creation

-   Payment otomatis dibuat setelah Rental berhasil dibuat.
-   Total pembayaran mengikuti `Rental.total_price`.

### 5.8.3 Checkout Summary

-   Halaman ringkasan checkout.
-   Menampilkan:
    -   Produk
    -   Harga
    -   Lama sewa
    -   Quantity
    -   Total pembayaran
-   User memilih metode pembayaran.

### 5.8.4 Transfer Payment

-   Upload bukti pembayaran.
-   Preview gambar.
-   Status berubah menjadi **Menunggu Verifikasi**.
-   Admin dapat melihat preview bukti.

### 5.8.5 Cash Payment

-   Halaman informasi pembayaran tunai.
-   User diarahkan ke riwayat penyewaan.
-   Status tetap **Belum Dibayar** hingga diverifikasi admin.

### 5.8.6 Admin Verification

-   Approve pembayaran.
-   Reject pembayaran.
-   Approve pembayaran otomatis menjalankan proses konfirmasi rental.
-   Stok produk berkurang setelah rental dikonfirmasi.

------------------------------------------------------------------------

## Flow

### Transfer

Rental → Checkout Summary → Transfer → Upload Bukti → Menunggu
Verifikasi → Admin Approve → Rental Confirmed

### Cash

Rental → Checkout Summary → Cash → Informasi Cash → My Rentals → Admin
Approve → Rental Confirmed

------------------------------------------------------------------------

## Testing Checklist

-   Login
-   Rental
-   Checkout
-   Transfer
-   Upload Bukti
-   Cash
-   Admin Approve
-   Admin Reject
-   Status Rental
-   Pengurangan Stok

Semua pengujian utama berhasil.

------------------------------------------------------------------------

## Hasil Sprint

Sprint 5 menghasilkan modul pembayaran yang telah terintegrasi dengan
sistem rental dan siap menjadi fondasi bagi Sprint 6 (Recommendation
System).
