# Dokumentasi Protokol Komunikasi

Dokumentasi ini menjelaskan implementasi dua protokol komunikasi yang berbeda: **Request-Response** dan **Publish-Subscribe**. Kedua protokol ini digunakan dalam aplikasi berbasis web untuk berinteraksi dengan pengguna dan mengelola komunikasi antara klien dan server.

## 1. Protokol Request-Response

Protokol Request-Response adalah metode komunikasi di mana klien mengirimkan permintaan (request) kepada server, dan server memberikan respons (response) sesuai dengan permintaan tersebut. Protokol ini sering digunakan dalam aplikasi web untuk melakukan operasi CRUD (Create, Read, Update, Delete) dan mendapatkan data dari server.

### Kelebihan:
- **Sederhana**: Mudah dipahami dan diimplementasikan.
- **Deterministik**: Hasil respons dapat diprediksi berdasarkan permintaan yang diajukan.
- **Pengelolaan Kesalahan**: Mudah dalam menangani kesalahan, karena server dapat memberikan status yang jelas dalam respons.

### Kekurangan:
- **Latency Tinggi**: Waktu respons dapat tinggi jika server sibuk.
- **Blocking**: Klien harus menunggu hingga respons diterima sebelum melanjutkan proses.
- **Kurang Efisien untuk Banyak Pengguna**: Tidak ideal untuk aplikasi dengan banyak pengguna yang memerlukan pembaruan real-time.

### Use Case:
- Aplikasi web untuk pengambilan data dari server (misalnya, mengambil informasi pengguna).
- Operasi CRUD pada basis data (misalnya, menambah, mengubah, atau menghapus data).

### Hasil Uji Latensi:
- **Server Latency:** 500.35 ms
- **Client Latency:** 516 ms

## 2. Protokol Publish-Subscribe

Protokol Publish-Subscribe (Pub/Sub) adalah metode komunikasi di mana klien dapat mengirimkan (publish) pesan ke topik tertentu, dan klien lain yang telah berlangganan (subscribe) ke topik tersebut akan menerima pesan yang dikirimkan. Protokol ini sangat berguna dalam aplikasi yang memerlukan komunikasi real-time, seperti aplikasi IoT dan chat.

### Kelebihan:
- **Real-time**: Memberikan pembaruan secara langsung kepada klien yang terdaftar.
- **Scalability**: Dapat menangani banyak klien secara bersamaan tanpa membebani server.
- **Loose Coupling**: Pengirim dan penerima tidak perlu mengetahui satu sama lain, memungkinkan fleksibilitas dalam pengembangan.

### Kekurangan:
- **Kompleksitas**: Lebih sulit untuk diimplementasikan dan dikelola dibandingkan Request-Response.
- **Pengelolaan Kesalahan**: Penanganan kesalahan dapat lebih sulit karena tidak ada umpan balik langsung.
- **Latency Variabel**: Latensi dapat bervariasi tergantung pada jumlah langganan dan kondisi jaringan.

### Use Case:
- Aplikasi chat yang memerlukan pengiriman pesan secara real-time.
- Sistem IoT di mana perangkat harus berkomunikasi secara langsung dan terus-menerus.
- Pembaruan informasi di dashboard real-time.

### Hasil Uji Latensi:
- **Latency:** 310 ms

## Kesimpulan

Kedua protokol ini menyediakan cara yang efisien untuk menangani komunikasi antara klien dan server. Protokol Request-Response cocok untuk situasi di mana klien memerlukan respons segera setelah mengirimkan permintaan. Di sisi lain, protokol Publish-Subscribe lebih sesuai untuk aplikasi yang memerlukan komunikasi real-time dengan banyak pengguna.

Dokumentasi ini memberikan gambaran umum tentang cara kerja kedua protokol, serta hasil uji latensi yang menunjukkan performa masing-masing.
