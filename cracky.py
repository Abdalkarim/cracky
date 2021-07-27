import PyPDF2,sys

print("""
     	  __   __   ___     
     	 |ma) |ak\ |__      
         |    |  / |        
                         
	 __        __   __       
	/  `  /\  |th) /on` |__/ 
	\__, /~~\ |  \ \__, |  \ @h0x72us
                         
"""
)
if len(sys.argv) == 3:
	fileName = sys.argv[1]
	passFile = sys.argv[2]
else:
	print("[*] Usage python3 cracky.py pdfFile.pdf wordlist.txt\n")
	sys.exit()

def crack():

	pdfFile = open(fileName,'rb')
	pdfObj  = PyPDF2.PdfFileReader(pdfFile)
	
	if pdfObj.isEncrypted:
		with open(passFile,'rb') as f:
			lines = f.readlines()
			for line in lines:
				line = line.strip()
				try:
					pdfObj.decrypt(line)
					print("[*] Password found : {}\n".format(str(line,'utf-8')))
					break
				except:
					continue
			else:print("[*] Password not found in your wordlist try another wordlist.\n")
	else:
		print("[*] your pdf file not encrypted.")		
		

if __name__ == '__main__':
	crack()
