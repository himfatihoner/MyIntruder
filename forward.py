import argparse
import txt_req_parser
import requests
# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
def forward(method,url,headers,params,cookie,req_code=None,needed_dict=None,index=None,payload=None):
	if(method=="GET"):	
		if (req_code == 0):
			response = requests.get(url,headers=needed_dict,params=params,cookies=cookie)
		elif (req_code == 1):
			response = requests.get(url,params=params,headers=headers,cookies=needed_dict)
		elif (req_code == 2):
			response = requests.get(url,params=needed_dict,headers=headers,cookies=cookie)
		else:
			response = requests.get(url,params=params,headers=headers,cookies=cookie)
	elif(method=="POST"):
		if (req_code == 0):
			response = requests.post(url,headers=needed_dict,data=params,cookies=cookie)
		elif (req_code == 1):
			response = requests.post(url,data=params,headers=headers,cookies=needed_dict)
		elif (req_code == 2):
			response = requests.post(url,data=needed_dict,headers=headers,cookies=cookie)
		else:
			response = requests.post(url,data=params,headers=headers,cookies=cookie)
	if(len(response.content) != 276):
		print("{:<10}{:<40}{:<10}{:<10}".format(index,payload,response.status_code,len(response.content)))
def change_key(method,url,headers,cookie,params,req_code,payload_path,needed,findex,needed_dict):
	with open(payload_path,'r') as first_payload_file:
		tmp_value=needed_dict[needed]
		needed_dict.pop(needed)
		index=0
		for tmp1 in first_payload_file:
			first_temp_req = needed
			tmp1 = tmp1.strip()
			lenoftmp1 = len(tmp1)
			first_temp_req = payload_swap(first_temp_req,findex,tmp1)
			needed_dict.update({first_temp_req: tmp_value})
			needed_dict.pop(first_temp_req)
			index=index+1
			forward(method,url,headers,params,cookie,req_code,needed_dict,index=index,payload=tamp1)
def change_value(method,url,headers,cookie,params,req_code,payload_path,needed,findex,needed_dict):
	with open(payload_path,'r') as first_payload_file:
		temp_dict=needed_dict.copy()
		index=0
		for tamp1 in first_payload_file:
			first_temp_req = needed_dict[needed]
			tamp1 = tamp1.strip()
			lenoftmp1 = len(tamp1)
			first_temp_req = payload_swap(first_temp_req,findex,tamp1)
			temp_dict.update({needed: first_temp_req})
			index=index+1
			forward(method,url,headers,params,cookie,req_code,temp_dict,index=index,payload=tamp1)
def change_loc(method,url,headers,cookie,params,payload_path):
	with open(payload_path,'r') as first_payload_file:
		index=0
		for tmp1 in first_payload_file:
			tmp1 = tmp1.strip()
			index = index + 1
			forward(method,url+"/"+tmp1,headers,params,cookie,index=index,payload=tmp1)
def find_marker(location_or_dict):
	if(type(location_or_dict)==dict):
		given_dict=location_or_dict
		for key in given_dict:
			for x in key:
				if(x=='§'):
					return key,key.index(x),True
			for x in given_dict[key]:
				if(x=='§'):
					return key,given_dict[key].index(x),False
	else:
		for x in location_or_dict:
			if(x=='§'):
				return location_or_dict.index(x)
	return -1
def payload_swap(req,index,word):
	if index not in range(len(req)):
        	raise ValueError("Index outside given string")
	return req[:index] + word + req[index + 1:]
def forward_req(url,req_path,method,payload_path,spayload_path=None):
	if(spayload_path == None):
		if(method == "GET"):
			print("\n\n{:<10}{:<40}{:<10}{:<10}\n".format("Index","Payload","Status","Length"))
			if url[-1:]=="/":
				url=url[:-1]
			headers={}
			cookie={}
			params={}
			needed=None
			needed_dict={}
			headers,cookie,location,params = txt_req_parser.parse_the_request(req_path)		
			if(find_marker(headers) != -1):
				needed,findex,key_or_value=find_marker(headers)
				req_code=0
				needed_dict = headers
			elif(find_marker(cookie) != -1):
				needed,findex,key_or_value=find_marker(cookie)
				req_code=1
				needed_dict = cookie
			elif(find_marker(params) != -1):
				needed,findex,key_or_value=find_marker(params)
				req_code=2
				needed_dict = params
			elif(find_marker(location) != -1):
				loc_pay_index=find_marker(location)
			if needed is not None:
				if(key_or_value):
					change_key(method,url+location,headers,cookie,params,req_code,payload_path,needed,findex,needed_dict)
				else:
					change_value(method,url+location,headers,cookie,params,req_code,payload_path,needed,findex,needed_dict)
			elif loc_pay_index is not None:
				change_loc(method,url,headers,cookie,params,payload_path)
		elif(method == "POST"):
			if url[-1:]=="/":
				url=url[:-1]
			headers={}
			cookie={}
			data={}
			needed = None
			needed_dict={}
			headers,cookie,location,data = txt_req_parser.parse_the_request(req_path)
			if(find_marker(headers) != -1):
				needed,findex,key_or_value=find_marker(headers)
				req_code=0
				needed_dict = headers
			elif(find_marker(cookie) != -1):
				needed,findex,key_or_value=find_marker(cookie)
				req_code=1
				needed_dict = cookie
			elif(find_marker(data) != -1):
				needed,findex,key_or_value=find_marker(data)
				req_code=2
				needed_dict = data
			elif(find_marker(location) != -1):
				loc_pay_index=find_marker(location)
			if needed is not None:
				if(key_or_value):
					change_key(method,url+location,headers,cookie,data,req_code,payload_path,needed,findex,needed_dict)
				else:
					change_value(method,url+location,headers,cookie,data,req_code,payload_path,needed,findex,needed_dict)
			elif loc_pay_index is not None:
				change_loc(method,url,headers,cookie,data,payload_path)
	else:
		print("Be patient!!!")
