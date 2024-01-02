import web
import random

app = web.application(('(.*)', 'DiscordRoulette'), globals())
web.config.debug = False
host = "127.0.0.1"
port = 8000

with open('media/cute.jpg', 'rb') as f:
    cute = f.read()
with open('media/hentai.webp', 'rb') as f:
    hentai = f.read()

class DiscordRoulette:
    def handleReq(self):
        try:
            web.header('Cache-Control', 'no-store')

            if random.randint(1, 10) == 10:
                return hentai
            else:
                return cute
        except:
            pass
        
    def GET(self, name):
        web.header('Content-type', 'image/png')
        return self.handleReq() or cute

if __name__ == "__main__":
    web.httpserver.runsimple(app.wsgifunc(), (host, port))