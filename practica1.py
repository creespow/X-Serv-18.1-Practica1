#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import socket

class contentApp (webapp.webApp):

	short_urls = {}
	shortened_urls = {}
	count = 0

	def parse (self, request):
		httpmethod = request.split(' ', 2)[0]
		resource = request.split(' ', 2)[1]
		if httpmethod == 'POST':
			body = request.split("\r\n\r\n",1)[1]
		else:
			body = ""
		return (httpmethod, resource, body)

	def process (self, parsedRequest):
		httpmethod, resource, body = parsedRequest
		form = ('<form action="" method="POST">Request your URL:'
				+ '<input type="text" name="name" value="" /><br/>'
				+ '<input type="submit" value="SEND" /></form>')

		if httpmethod == 'GET':
			print "estoy en get"
			if resource == '/':
				print "le envio el form"
				httpcode = '200 OK'
				htmlbody = ("<html><body>" + str(self.short_urls) +
							form + "</html></body>")
			else:
				shorturl = int(recurso.split('/')[1])
				if shorturl in self.shortened_urls:
					page = self.content[int(shorturl)]
					httpcode = '300 Redirect'
					htmlbody = '<html><body><h1>Redirect</h1>\
					<meta http-equiv="Refresh" content="2;url=' 
					+ str(page) +'"></body></html>'
				else:
					httpcode = '404 Not Found'
					htmlbody = '<html><body><h1>Not Found </h1></body></html>'

		elif httpmethod == 'POST':
			if body.find("http") == -1:
				body = "http://" + body
			else:
				body = (body.split("%3A%2F%2F")[0] +
						"://" +
						body.split("%3A%2F%2F")[1])
			if body in self.short_urls:
				shorturl = self.short_urls[body]
			else:
				self.shorturl = self.short_urls +1
				shorturl = self.shorturls
				self.short_urls[body] = short_url
				self.shortened_urls[body] = body

			httpcode = '200 OK'
			htmlbody = ("<html><body>" +
						"<h1>larga y corta: </h1>" +
						"<a href=" + body + '>' + body + "</href><br>" +
						"<a href=" + str(shorturl) + '>' + str(shorturl) + 
						"</href></body></html>")
			
if __name__ == "__main__":
	testWebApp = contentApp (socket.gethostname(), 1234)
