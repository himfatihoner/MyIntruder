def parse_the_request(path):
	with open(path, 'r') as req_file:
		my_req_line=req_file.readlines()
		firstline = my_req_line[0]
		method=firstline.split()[0]
		if(method == "GET"):
			headers={}
			params={}
			cookie={}
			for line in my_req_line:
				if my_req_line.index(line) != 0:
					index=line.find(": ")
					my_header_key= line[:index]
					my_header_value=line[index+2:-1]
					if my_header_key == 'Cookie':
						for raw_cookie in my_header_value.split("; "):
							index_of_cookie=raw_cookie.find("=")
							key_of_cookie=raw_cookie[:index_of_cookie]
							value_of_cookie=raw_cookie[index_of_cookie+1:]
							cookie.update({key_of_cookie: value_of_cookie})
					elif(my_header_key == ''):
						continue
					else:
						headers.update({my_header_key: my_header_value})
				else:
					param_tmp=line[4:]
					param_tmp=param_tmp.split(" ")[0]
					location=param_tmp
					if(param_tmp.find("?")!=-1):
						location=param_tmp.split("?")[0]
						param_tmp=param_tmp.split("?")[1]
						for param in param_tmp.split("&"):
							param_key=param.split("=")[0]
							param_value=param.split("=")[1]
							params.update({param_key: param_value})
			return headers,cookie,location,params
		elif(method == "POST"):
			headers={}
			data={}
			cookie={}
			after_blank=0
			for line in my_req_line:
				if my_req_line.index(line) != 0 and after_blank==0:
					if(line == "\n"):
						after_blank=1
					else:
						index=line.find(": ")
						my_header_key= line[:index]
						my_header_value=line[index+2:-1]
						if my_header_key == 'Cookie':
							for raw_cookie in my_header_value.split("; "):
								index_of_cookie=raw_cookie.find("=")
								key_of_cookie=raw_cookie[:index_of_cookie]
								value_of_cookie=raw_cookie[index_of_cookie+1:]
								cookie.update({key_of_cookie: value_of_cookie})
						elif(my_header_key == ''):
							continue
						else:
							headers.update({my_header_key: my_header_value})
				elif(after_blank == 1):
					for per_data in line.split("&"):
						data_key=per_data.split("=")[0]
						data_value=per_data.split("=")[1]
						data_value = data_value.strip()
						data.update({data_key: data_value})
				elif(my_req_line.index(line) == 0):
					param_tmp=line[5:]
					param_tmp=param_tmp.split(" ")[0]
					location=param_tmp
			return headers,cookie,location,data
