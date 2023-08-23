#!usr/bin/python


def TambahList():
	daftarList=[]
	while True:
		masukanlist=input("masukan list pekerjaan: ")
		daftarList.append(masukanlist)
		if(masukanlist=="n"):
			daftarList.remove('n')
			break
	with open("ToDoList.txt","w") as openfile:
		for listkerja in daftarList:
			openfile.write(listkerja+"\n")
	print("List Pekerjaan Sukses Disimpan")

def DisplayList():
	with open("ToDoList.txt","r") as openfile:
		data=openfile.read()
		print(data)

def PilihAngka():
	pilihan=input("Masukan Pilihan: ")
	if(pilihan=="1"):
		TambahList()
	elif(pilihan=="2"):
		DisplayList()
	else:
		print("bilangan tidak ditemukan")

if __name__ == '__main__':
	PilihAngka()