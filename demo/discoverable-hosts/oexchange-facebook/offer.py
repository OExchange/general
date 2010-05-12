from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import urllib 

class MainPage(webapp.RequestHandler):

    def get(self):
        url = self.request.get("url")
        title = self.request.get("title")
        if not url:
            self.error(400)
            return
        redirect = "http://facebook.com/sharer.php?u=" + urllib.quote_plus(url) + "&t=" + urllib.quote_plus(title)
        self.redirect(redirect)

application = webapp.WSGIApplication([('/offer', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()