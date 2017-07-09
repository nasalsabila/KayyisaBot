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

KayyisaBot juga memanfaatkan data do'a sehari-hari di situs aandazkar.com/chapter-4-daily-essential-duas/.

# Cara Penggunaan
Cari KayyisaBot dengan mengetikkan @KayyisaBot pada kolom search. Kemudian start chat.
Terdapat beberapa perintah/commands pada KayyisaBot, yaitu:
- /start = terdapat informasi mengenai KayyisaBot
- /shalat = menampilkan jadwal shalat hari ini sesuai masukan wilayah dari pengguna
- /quran = menampilkan ayat Al-Qur'an yang diinginkan pengguna
- /cari = mencari kata tertentu dalam Al-Qur'an. Bot akan menampilkan list surat dan ayatnya
- /catatan = menampilkan catatan depag mengenai terjemahan ayat tertentu
- /doa = menampilkan do'a yang diinginkan pengguna sesuai daftar do'a yang ada
- /setdaily = pengguna set perintah pada bot untuk mengirim ayat pilihan tiap hari
- /help = bantuan
