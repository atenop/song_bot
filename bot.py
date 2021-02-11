import telebot
bot = telebot.TeleBot("1336087291:AAEBMEg-to2z3Gc95wtSFcGElLJXAjPkdj0")
@bot.message_handler(commands=['start'])
def welcome(message):
    reply = """
<b>Welcome to OP Downloader bot!</b>
"""
    bot.send_message(message.chat.id, reply, parse_mode="HTML")
    
SONG_CACHE = []
@bot.message_handler(commands=['list'])
def list_reply(message):
    global SONG_CACHE
    user_message = message.text
    user_url = user_message.text.split()[1]
    # Validate User_url
    bot.send_message(message.chat.id, "Fetching song info...")
    songs = get_songs(user_url)
    reply = """
The songs available for download are :
"""
    for i in range(len(songs)): # Adding the songs to our reply
        reply += """{}. {}
""".format(i+1, songs[i]['title'])
    
    SONG_CACHE[message.chat.id] = songs
    
def get_song(message, song_index):
    try:
        songs_list = SONG_CACHE[message.chat.id]
        if song_index < 0 or song_index > len(songs_list)-1:
            bot.send_message(message.chat.id, "Requested song not found in the list.")
            return None
        req_song = songs_list[song_index]
        return req_song
    except KeyError as e:
         bot.send_message(message.chat.id, "You have not generated a song list to download songs. Refer /help on how to do it.")
         return None
def _download_song(song, url):
 if os.path.exists(os.path.join(os.getcwd(),
                                unquote(song['title'])+".mp3")):
     return unquote(song['title'])+".mp3"
 else:
     filename = wget.download(url, unquote(song['title'])+".mp3")
     return filename
@bot.message_handler(commands=['download'])
def download_song(message)
    text = message.text
    song_index = int(text.split()[1]) - 1 # READ NOTE BELOW
    req_song = get_song(message, song_index)
    if req_song != None:
         download_url = decrypt_url(req_song['url'])
         bot.send_message(message.chat.id, "Your download has begun. Please wait...")
         # Now we will download and send the requested song
         # We are using a utility function defined above to download
         filename = _download_song(req_song, download_url)
         bot.send_message(message.chat.id, "You download has finished. Please wait while we send this song to you...")
         audio = open(os.path.join(os.getcwd(), filename), 'rb')
         bot.send_audio(
              message.chat.id,
              audio,
              title=req_song['title'],
               performer=req_song['singers']
         )
         audio.close()
         os.unlink(os.path.join(os.getcwd(), filename))
