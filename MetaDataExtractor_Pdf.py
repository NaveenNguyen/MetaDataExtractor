#/usr/bin/python 
#get_doc_info.py
 
from PyPDF2 import PdfFileReader
import sys,glob,os
reload(sys)
sys.setdefaultencoding('utf8')

	
def recon_pdf_list(dom):
	command1 = "goofile -d " + dom + " -f pdf | grep " + dom + ">> " +dom+".txt ;sed -i 1d "+dom+".txt"
	process=os.popen(command1)

def download_files():
	command2= "for i in $(cat "+dom+".txt); do wget $i; done"
	process=os.popen(command2)


def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
	print("Title: " + str(info.title))
	print("Subject: " + str(info.subject))
	print("Author: " + str(info.author))
	print("Producer: " + str(info.producer))
	print("Creator: " + str(info.creator))
 
if __name__ == '__main__':
	try:
		dom = sys.argv[1]
	except:
		print("Usage: enter the domain name eg.google.com")
		sys.exit()
		
	if sys.argv[1]==0:	
		print("Usage: enter the domain name eg.google.com")
		sys.exit()

	recon_pdf_list(dom)
	download_files()
	files_list=glob.glob("*.pdf")
	for flist in files_list:
		print("Getting metadata for file: " + flist)
		get_info(flist)
		print("\n")

