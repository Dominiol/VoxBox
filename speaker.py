import config, urllib

class Speaker:
    def speechSynthesis(self, text, lang = 'pl_PL'):
        text_str = urllib.quote(text)
        url = 'https://tts.voicetech.yandex.net/tts?lang=%s&format=mp3&quality=hi&text=%s' % (lang, text_str)
        
        try:
            urllib.urlretrieve(url, 'tmp_speech.mp3')
            self.playMp3('tmp_speech.mp3')
        except:
            raise Exception()
    
    def playMp3(self, path):
        # play mp3 song
        pass