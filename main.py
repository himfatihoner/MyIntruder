# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
# github:himfatihoner
# tryhackme:himfatihoner
# linkedin:fatih-oner
# §§§§§§§§§§§§§§§§§§§§§§§§§§§§§
import argparse
import forward
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help="URL")
parser.add_argument("-r","--request", help="Request Path")
parser.add_argument("-p","--payload",help="Payload Path")
parser.add_argument("-sp","--spayload",help="Second Payload Path (Optional)")
args=parser.parse_args()
print("Request Path:{}\nPayload Path:{}\nSecond Payload Path(Optional):{}".format(args.request,args.payload,args.spayload))
with open(args.request, 'r') as reqfile:
	my_req_lines=reqfile.readlines()
	firstline = my_req_lines[0]
	method=firstline.split()[0]
look_for_sp=False
pindex=None
spindex=None
for line in my_req_lines:
	if(line.find('§') != -1):
		if(look_for_sp == False):
			pindex=line.find('§')
			pline = my_req_lines.index(line)
			look_for_sp=True
			if(line.find('§',pindex+1)!=-1):
				spindex = line.find('§',pindex+1)
				spline = pline
				break
		else:
			spindex = line.find('§')
			spline = my_req_lines.index(line)
			break		
if args.payload is None:
	print("You forgot something!(Set at least one payload with '-p' flag)")
else:
	if pindex is not None:
		print("The payload marker has been found at index {} in line {}".format(pindex+1,pline+1))
		if args.spayload is not None:
			if spindex is not None:
				print("The payload marker has been found at index {} in line {}".format(spindex+1,spline+1))
				print("Script will run for both payloads.")
				forward.forward_req(args.url,args.request,method,args.payload,args.spayload)
			else:
				print("Probably you forgot to insert second payload marker.")
		else:
			print("Script will run for only one payload.")
			forward.forward_req(args.url,args.request,method,args.payload)
	else:
		print("Probably you forgot to insert payload marker.")
