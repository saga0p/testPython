import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world, this is a python command running from backend")

class newRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/test",newRequestHandler)
    ])

    port = 8822
    app.listen(port)
    print(f"Application is running on port {port}")
    tornado.ioloop.IOLoop.current().start()