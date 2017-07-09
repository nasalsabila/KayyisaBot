# KayyisaBot

بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ

Tugas Akhir Pemrograman Python - Membuat Chatbot Telegram

Dibuat oleh : Nikmatun Aliyah Salsabila - 0102514014

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Daftar isi**

- [Deskripsi](#deskripsi)
- [Cara Penggunaan Bot](#cara-penggunaan)

<!-- markdown-toc end -->

# Deskripsi

KayyisaBot merupakan chatbot telegram yang memiliki tiga fitur utama, yaitu 
jadwal shalat, Al-Qur'an, dan do'a sehari-hari. Dengan fitur jadwal shalat, 
bot akan menampilkan jadwal shalat sesuai wilayah yang dimasukkan oleh pengguna
pada hari ini. Pengguna dapat meminta bot untuk menampilkan ayat tertentu dengan
memanfaatkan fitur Al-QUr'an. Bukan hanya itu, pengguna pun dapat melihat catatan
depag mengenai terjemahan ayat dan mencari kata dalam Al-Qur'an, sehingga bot akan
menampilkan list surat dan ayatnya.

KayyisaBot dikembangkan dengan bahasa pemrograman python dan didukung API berikut:
- python-telegram-bot (python-telegram-bot.org)
- Prayer Times API (https://aladhan.com/prayer-times-api)
- API Fathimah (api.fathimah.ga)

KayyisaBot juga memanfaatkan data do'a sehari-hari di situs duaandazkar.com/chapter-4-daily-essential-duas/.

# Cara Penggunaan
Cari KayyisaBot dengan mengetikkan @KayyisaBot pada kolom search. Kemudian start chat.
Terdapat beberapa perintah/commands pada KayyisaBot, yaitu:
- /start = menampilkan informasi mengenai KayyisaBot. Kirim perintah **/start**
- /shalat = menampilkan jadwal shalat hari ini sesuai masukan wilayah dari pengguna. Kirim perintah **/shalat <wilayah>**. Contoh : /shalat Bekasi Utara
- /quran = menampilkan ayat Al-Qur'an yang diinginkan pengguna. Kirim perintah **/quran <surat:ayat>**. Contoh : /quran 2:255-256
- /cari = mencari kata tertentu dalam Al-Qur'an. Bot akan menampilkan list surat dan ayatnya. Kirim perintah **/cari <kata>**. Contoh : /cari puasa
- /catatan = menampilkan catatan depag mengenai terjemahan ayat tertentu. Kirim perintah **/catatan <nomor>**. Contoh : /catatan 5
- /doa = menampilkan do'a yang diinginkan pengguna sesuai daftar do'a yang ada. Kirim perintah **/doa <nomor>**. Contoh : /doa 1
- /setdaily = pengguna set perintah pada bot untuk mengirim ayat pilihan tiap hari. Kirim perintah **/setdaily**
- /help = bantuan. Kirim perintah **/help**

![example]

[example]: http://imgur.com/6NLQwG2 "Contoh percakapan"

