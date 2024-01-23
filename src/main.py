import asyncio
import os, os.path
import tornado.web
import Index, Profile, TemplateTest       #new
import os

HTMLDIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 "..","html"
    )
)

def makeApp():
    endpoints=[
        ("/",Index.Handler),
        ("/Profile/.*", Profile.ProfileHandler)
    ]
    app = tornado.web.Application(endpoints,
        static_path=HTMLDIR
    )
    app.listen(8000)
    return app

if __name__ == "__main__":
    app = makeApp()
    asyncio.get_event_loop().run_forever()