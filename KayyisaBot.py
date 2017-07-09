from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Job
import requests
import json
import re
import logging
import random
#from datetime import datetime, time


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Start
def start(bot, update):
    update.message.reply_text("Assalamu'alaikum {}!"
		"\nSelamat datang di KayyisaBot."
		"\nKayyisaBot akan membantumu untuk menampilkan jadwal shalat, ayat Al-Quran dan do'a sehari-hari."
		"\nKirim perintah /shalat <alamat> untuk tahu jadwal sholat di wilayahmu hari ini."
		"\nKirim perintah /quran <surat:ayat> untuk menampilkan ayat Al-Qur'an pilihanmu."
		"\nKirim perintah /cari <kata> untuk menampilkan ayat yang terdapat kata tersebut"
		"\nKirim perintah /catatan <nomor> untuk menampilkan catatan depag mengenai terjemahan ayat tertentu"
		"\nKirim perintah /doa <nomor do'a> untuk menampilkan do'a harian yang kamu pilih"
		"\nKirim perintah /setdaily untuk mendapat kiriman ayat pilihan tiap hari"
		"\nKirim perintah /help untuk bantuan".format(update.message.from_user.first_name))

# Menampilkan jadwal shalat hari ini
def shalat(bot, update, args):
    try:
	arg = args[0]
	addr = args[0:]
	payload = {'address' : '{}'.format(addr), 'method' : '4'}
	r = requests.get('http://api.aladhan.com/timingsByAddress', params=payload)
	data = json.loads(r.content)
	#jadwal = data['data']['timings']
	#for key, value in jadwal.items():
		#update.message.reply_text('{} {}'.format(key, value))
	fajr = data['data']['timings']['Fajr']
	sunrise = data['data']['timings']['Sunrise']
	dhuhr = data['data']['timings']['Dhuhr']
	asr = data['data']['timings']['Asr']
	sunset = data['data']['timings']['Sunset']
	maghrib = data['data']['timings']['Maghrib']
	isha = data['data']['timings']['Isha']
	imsak = data['data']['timings']['Imsak']
	midnight = data['data']['timings']['Midnight']
	date = data['data']['date']['readable']

	update.message.reply_text("--Jadwal {}--\nSubuh {}\nMatahari Terbit {}\nDzuhur {}\nAshar {}\nMatahari Terbenam {}\nMaghrib {}\nIsya {}\nImsak {}\nTengah Malam {}\n\nMetode : Umm al-Qura, Makkah\n\nBiasakan shalat di awal waktu, ya!:)".format(date, fajr, sunrise, dhuhr, asr, sunset, maghrib, isha, imsak, midnight))

    except (IndexError, ValueError):
        update.message.reply_text('Kirim perintah /shalat <wilayah> untuk tahu jadwal shalat di wilayahmu hari ini.'
'\nContoh :\n/shalat Bekasi\n/shalat Universitas Al Azhar Indonesia')

# Menampilkan ayat Al-Qur'an 
def quran(bot, update, args):
    try:
	x = args[0]
	x.split(',')
	s, a = x.split(':')
	match = re.match("\d+\-\d*", a)
	if match is not None:
		awal, akhir = a.split('-')
		akhir = int(akhir)-int(awal)+1
		r = requests.get('http://api.fathimah.ga/quran/format/json/surat/{}/ayat/{}'.format(s, a))
		data=r.content
		data=json.loads(data)
		for i in range(akhir):
			ayat = data['ayat']['data']['ar'][i]['teks'].encode('utf-8')
			arti = data['ayat']['data']['id'][i]['teks'].encode('utf-8')
			update.message.reply_text('{}\n{}'.format(ayat, arti))
	else:
		r = requests.get('http://api.fathimah.ga/quran/format/json/surat/{}/ayat/{}'.format(s, a))
		data=r.content
		data=json.loads(data)
		ayat = data['ayat']['data']['ar'][0]['teks'].encode('utf-8')
		arti = data['ayat']['data']['id'][0]['teks'].encode('utf-8')
		update.message.reply_text('{}\n{}'.format(ayat, arti))
		
	
    except (IndexError, ValueError):
        update.message.reply_text("Kirim perintah /quran <surat:ayat> untuk menampilkan ayat Al-Qur'an pilihanmu!"
"\nContoh :\n/quran 2:255\n/quran 2:255-256"
"\n\nKeterangan :\n Nomor di dalam kurung kurawal {3} seperti ini maksudnya adalah catatan depag mengenai terjemahan tersebut."
"\nLihat catatan depag tersebut dengan mengirim perintah /catatan <nomor>."
"\nKamu juga bisa mencari kata tertentu dan menampilkan surat dan ayat berapa saja dalam Al-Qur'an yang terdapat kata tersebut. Kirim perintah /cari <kata>")

# Menampilkan pencarian kata pada Al-Qur'an
def cari(bot, update, args):
    try:
	kata = args[0].lower()
	r = requests.get('http://api.fathimah.ga/quran/format/json/cari/{}/bahasa/id/mulai/0/limit/100'.format(kata))

	data = json.loads(r.content)
	qs = []
	for i in range(100):
		try :
			surat = data['cari']['id']['data'][i]['surat']
			ayat = data['cari']['id']['data'][i]['ayat']
			carian = 'QS. {} : {}'.format(surat, ayat)
			qs.append(carian)
		except:
			None
	qs = '\n'.join(qs)
	if qs == '':
		update.message.reply_text('Tidak ada hasil pencarian untuk kata {}'.format(kata))
	else:
		update.message.reply_text('Hasil pencarian untuk kata {}:\n{}'.format(kata, qs))
	
    except (IndexError, ValueError):
        update.message.reply_text("Kirim perintah /cari <kata> untuk menampilkan surat dan ayat apa saja dalam Al-Qur'an yang terdapat kata tersebut."
"\nContoh :\n/cari puasa\n/cari beriman"
"\n\nMaksimal surat dan ayat yang tampil sebanyak 100")

def catatan (bot, update, args):
    try:
	no = int(args[0])
	if no in range(1, 1611):
		r = requests.get('http://api.fathimah.ga/quran/format/json/catatan/{}'.format(no))
		data = json.loads(r.content)
		cttn = data['catatan']['teks']
		nmr = data['catatan']['nomor']
		update.message.reply_text('Catatan nomor {}:\n{}'.format(nmr, cttn))	
	else:
		update.message.reply_text('Tidak terdapat catatan depag dengan nomor {}.'.format(no))	

    except (IndexError, ValueError):
        update.message.reply_text('Kirim perintah /catatan <nomor> untuk mengetahui catatan depag mengenai terjemahan ayat tertentu.'
'\nContoh :\n/catatan 5\n/catatan 256')
   
# Menampilkan do'a	
def doa (bot, update, args):
    try:
	arg = int(args[0])
	kode = arg-1
	if kode in range(0, 20):
		with open('scraping.json', 'r') as fp:
			data = json.load(fp)
		name = data['dua'][kode]
		ref = data['reference'][kode]
		pronun = data['pronunciation'][kode]
		trans = data['translation'][kode]
		hadith = data['hadith'][kode]
		no = str(arg)
		img = 'd'+no+'.png'	
		update.message.reply_photo(open(img, 'rb'))
		update.message.reply_text("Du'a:\n{}\n\nReference:\n{}\n\nPronunciation:\n{}\n\nTranslation:\n{}\n\nHadith/Benefit:\n{}\n\nSumber: Daily essential duas oleh http://www.duaandazkar.com/".format(name, ref, pronun, trans, hadith))
	else:
		update.message.reply_text("Nomor {} tidak terdapat dalam daftar do'a. Hanya terdapat 20 do'a. Untuk lihat daftarnya, kirim perintah /doa".format(arg))
    except (IndexError, ValueError):
        update.message.reply_text("Kirim perintah /doa <nomor do'a> untuk menampilkan do'a sehari-hari yang kamu inginkan dalam bahasa Inggris"
"\nContoh :\n/doa 1\n/doa 18."
"\n\nBerikut adalah daftar do'a sehari-hari yang ada :\n"
"1. Upon Going to sleep\n"
"2. Wake up from sleep\n"
"3. Entering the Toilet\n"
"4. Leaving the Toilet\n"
"5. Start of Wudu\n"
"6. Completion of Wudu\n"
"7. Entering the Mosque\n"
"8. Leaving the Mosque\n"
"9. Before the Meals\n"
"10. Forgetting to recite Bismillah\n"
"11. After meals\n"
"12. After meals (Second Option)\n"
"13. Leaving Home\n"
"14. Entering Home\n"
"15. On Journey\n"
"16. Return From Journey\n"
"17. When Sneezing\n"
"18. Hearing someone sneeze\n"
"19. Sneezers replies back\n"
"20. Entering the Market\n")

def help(bot, update):
    update.message.reply_text("/shalat <alamat> : menampilkan jadwal sholat di wilayahmu hari ini."
		"\n/quran <surat:ayat> : menampilkan ayat Al-Qur'an pilihanmu."
		"\n/cari <kata> : menampilkan ayat yang terdapat kata tersebut"
		"\n/catatan <nomor> : menampilkan catatan depag mengenai terjemahan ayat tertentu"
		"\n/doa <nomor do'a> : menampilkan do'a harian yang kamu pilih"
		"\n/setdaily : mendapat kiriman ayat pilihan tiap hari"
		"\n/help : bantuan".format(update.message.from_user.first_name))

def alarm(bot, job):
    """Function to send the alarm message"""
    with open("dailyquran.txt", "r") as f:
    	x=f.readlines() 

    pilihan = x[random.randint(0,len(x)-1)]

    pilihan.split(',')
    s, a = pilihan.split(':')
    match = re.match("\d+\-\d*", a)
    bot.send_message(job.context, text="Assalamu'alaikum! Ayat pilihan hari ini adalah QS.{}:{}".format(s, a))
		
    if match is not None:
    	awal, akhir = a.split('-')
	akhir = int(akhir)-int(awal)+1
	r = requests.get('http://api.fathimah.ga/quran/format/json/surat/{}/ayat/{}'.format(s, a))
	data=r.content
	data=json.loads(data)
	for i in range(akhir):
		ayat = data['ayat']['data']['ar'][i]['teks'].encode('utf-8')
		arti = data['ayat']['data']['id'][i]['teks'].encode('utf-8')
		bot.send_message(job.context, text='{}\n{}'.format(ayat, arti))
    else:
	r = requests.get('http://api.fathimah.ga/quran/format/json/surat/{}/ayat/{}'.format(s, a))
	data=r.content
	data=json.loads(data)
	ayat = data['ayat']['data']['ar'][0]['teks'].encode('utf-8')
	arti = data['ayat']['data']['id'][0]['teks'].encode('utf-8')
	bot.send_message(job.context, text='{}\n{}'.format(ayat, arti))
    

def setdaily(bot, update, job_queue, chat_data):
    """Adds a job to the queue"""
    chat_id = update.message.chat_id
    try:
        #days = (0, 1, 2, 3, 4, 5, 6)
        #job = job_queue.run_daily(alarm, time(14, 9), days, context=chat_id)
	job = job_queue.run_repeating(alarm, 86400, first=15, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('Kirim ayat pilihan harian berhasil di-set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /setdaily')

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Maaf, command yang kamu masukkan tidak ada. Kirim perintah /help untuk bantuan.")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

def main():
    updater = Updater('SECRET TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('shalat', shalat, pass_args=True))
    dp.add_handler(CommandHandler('quran', quran, pass_args=True))
    dp.add_handler(CommandHandler('cari', cari, pass_args=True))
    dp.add_handler(CommandHandler('catatan', catatan, pass_args=True))
    dp.add_handler(CommandHandler('doa', doa, pass_args=True))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, start))
    dp.add_handler(CommandHandler('setdaily', setdaily,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    
    dp.add_handler(MessageHandler([Filters.command], unknown))    
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
