import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('Please add /profile/yourloginname to the end of the web address to access your login page.')