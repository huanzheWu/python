#-*- coding:utf-8 -*-
import sys
import os
import http.server
import subprocess

class ServerException(Exception):
	pass


class case_base(object):
    def test(self,handler):
        assert False,'Not implement'

    def act(self,handler):
        assert False,'Not implement'

    def index_path(self,handler):
        return os.path.join(handler.full_path,'index.html')

    def handle_file(self,handler,full_path):
        try:
            with open (full_path,'rb') as reader:
                content = reader.read()
                handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read:{1}".format(handler.path,msg)
            handler.handle_error(msg)


class case_cgi_file(case_base):
    def test(self,handler):
        return os.path.isfile(handler.full_path) and \
                handler.full_path.endswith('.py')
    
    def act(self,handler):
        handler.run_cgi(handler,handler.full_path)

    def run_cgi(self,full_path):
        data=subprocess.check_output(["python",handler.full_path])
        self.send_content(data)

class case_directory_index_file(case_base):
	
	
	def test(self,handler) :
		if not os.path.isdir(handler.full_path):
			raise ServerException("is not path dir '{0}'".format(handler.full_path))

		if not os.path.isfile(self.index_path(handler)) :
			raise ServerException("is not a file '{0}'".format(self.index_path(handler)))			
		return os.path.isdir(handler.full_path) and \
			os.path.isfile(self.index_path(handler))


	def act(self,handler):
		self.handle_file(handler,self.index_path(handler))



class case_no_file(case_base ):
	
	def test(self,handler):
		return not os.path.exists(handler.full_path)
	
	def act(self,handler):
		raise ServerException("'{0}' not found ".format(handler.path))

class case_existing_file(case_base):
	
	def test(self,handler):
		return os.path.isfile(handler.full_path)
	
	def act(self,handler):
		self.handle_file(handler,handler.full_path)

class case_always_fail(case_base):
	
	def test(self,handler):
		return True;
	
	def act(self,handler):
		raise ServerException("Unknow objecfft '{0}'".format(handler.path))




class RequestHandler(http.server.BaseHTTPRequestHandler):
	
	Cases = [case_no_file,
		 case_existing_file,
		case_directory_index_file,
	    case_cgi_file,
        case_always_fail]

	Page = """\
		<html>
		<body>
		<table>
		<tr>  <td>Header</td>         <td>Value</td>          </tr>
		<tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
		<tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
		<tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
		<tr>  <td>Command</td>        <td>{command}</td>      </tr>
		<tr>  <td>Path</td>           <td>{path}</td>         </tr>
		</table>
		</body>
		</html>
	"""
	
	Error_Page="""
		<html>
		<body>
		<h1>Error accessing {path}</h1>
		<p>{msg}</p>
		</body>
		</html>
		"""



	#处理一个请求
	def do_GET(self):
		try:
			#文件的完整路径
			self.full_path = os.getcwd()+self.path
			
			for case in self.Cases:
				handler = case()
				if handler.test(self):
					handler.act(self)
					break


		#	if not os.path.exists(full_path):
		#		raise ServerException("'{0}' not found".format(self.path))
		#	elif os.path.isfile(full_path):
		#		self.handle_file(full_path)
		#
		#	else :
		#		raise ServerEcxeption("Unknown object '{0}'".format(self.path))
		

		except Exception as msg:
			self.handle_error(msg)
		
		
		#page=self.create_page()
		#self.send_content(page)

		

	def handle_error(self , msg):
		content = self.Error_Page.format(path=self.path,msg=msg)
		self.send_content(bytes(content,'utf-8'),404)


	def create_page(self):
		# 待实现
		values = {
			'date_time' : self.date_time_string(),
			'client_host':self.client_address[0],
			'client_port':self.client_address[1],
			'command':self.command,
			'path':self.path
		}
		page = self.Page.format(**values)
		return page


	def send_content(self,content,status=200):	
		self.send_response(status)
		self.send_header("Content-Type","text/html")
		self.send_header("Content-Length",str(len(content)))
		self.end_headers()
		#self.wfile.write(bytes(content,'utf-8'))
		self.wfile.write(content)

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = http.server.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

