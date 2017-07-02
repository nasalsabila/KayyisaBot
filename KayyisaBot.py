from telegram.ext import Updater, CommandHandler
import requests
import json
import re

def start(bot, update):
    update.message.reply_text("Assalamu'alaikum {}!"
		"\nSelamat datang di KayyisaBot."
		"\nKayyisaBot akan membantumu untuk menampilkan jadwal shalat, ayat Al-Quran dan doa harian"
		"\nKirim perintah /shalat <alamat> untuk tahu jadwal sholat di wilayahmu hari ini."
		"\nContoh : /shalat Bekasi"
		"\nKirim perintah /quran <surat:ayat> untuk menampilkan ayat Al-Qur'an pilihanmu."
		"\nContoh : /quran 3:15 atau /quran 2:255-257".format(update.message.from_user.first_name))

def shalat(bot, update, args):
    try:
	addr = str(args[0])
	payload = {'address' : '{}'.format(addr), 'method' : '4'}
	r = requests.get('http://api.aladhan.com/timingsByAddress', params=payload)
	data = json.loads(r.content)
	jadwal = data['data']['timings']
	for key, value in jadwal.items():
		update.message.reply_text('{} {}'.format(key, value))
	
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /shalat <address>')

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
        update.message.reply_text('Usage: /quran <surat:ayat>')

def cari(bot, update, args):
    try:
	kata = args[0].lower()
	r = requests.get('http://api.fathimah.ga/quran/format/json/cari/{}'.format(kata))
	data = json.loads(r.content)
	for i in range(10):
		try :
			carian = data['cari']['id']['data'][i]
			update.message.reply_text('-Hasil {}-'.format(i+1))
			for key, value in carian.items():
				update.message.reply_text('{}{}'.format(key, value))
		except:
			None
	
    except (IndexError, ValueError):
        update.message.reply_text('Usage: /cari <kata>')
	

updater = Updater('SECRET TOKEN')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('shalat', shalat, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('quran', quran, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('cari', cari, pass_args=True))

updater.start_polling()
updater.idle()
