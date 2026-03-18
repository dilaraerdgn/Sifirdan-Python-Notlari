file = open("dosya.txt","r")  # w-> dosyayı açmak ve yazmak için kip , r-> okuma modu
"""
file.write("\nnaber python")    # a-> önceki yazdıklarımız dursun ama yeni şeyler de ekleyelim
file.write("\nnaber java")
"""

"""
veri=file.read()
print(veri)
file.close()
"""

"""
file.seek(10)  # 10. karaktere git
veri=file.read(10) # 10 tane oku
print(veri)
file.close()
"""
for satir in file: # satır satır okur
    print(satir)
file.close()