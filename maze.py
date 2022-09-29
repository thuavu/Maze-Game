#import logging
import jinja2
import os
import webapp2

template_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.getcwd()))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('maze.html')
        context = {
        }
        self.response.out.write(template.render(context))

class MazePage1(webapp2.RequestHandler):
    def post(self):
        #logging.basicConfif()
        #logging.warning("test")
        template = template_env.get_template('maze1.html')
        context = {
        }
        self.response.out.write(template.render(context))

class MazePage2(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('maze2.html')
        context = {
        }
        self.response.out.write(template.render(context))

class WinPage(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('maze_win.html')
        context = {
        }
        self.response.out.write(template.render(context))

application = webapp2.WSGIApplication([('/', MainPage),
                ('/Maze1', MazePage1),
                ('/Maze2', MazePage2),
                ('/Win', WinPage)],
                debug = True)
