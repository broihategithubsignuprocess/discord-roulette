import web
import random
import math

app = web.application(('(.*)', 'DiscordRoulette'), globals())
web.config.debug = False
host = "0.0.0.0"
port = 8000

chance = 50

with open('media/cute.jpg', 'rb') as f:
    cute = f.read()
with open('media/hentai.webp', 'rb') as f:
    hentai = f.read()

class DiscordRoulette:
    def handleReq(self):
        try:
            web.header('Cache-Control', 'no-store')

            if random.randint(1, int(100/chance)) == 1:
                web.header('Cache-Control', 'no-store')
                return hentai
            else:
                web.header('Cache-Control', 'no-store')
                return cute
        except:
            pass
        
    def GET(self, name):
        web.header('Content-type', 'image/png')
        web.header('Cache-Control', 'no-store')
        return self.handleReq() or "no"

if __name__ == "__main__":
    web.httpserver.runsimple(app.wsgifunc(), (host, port))
