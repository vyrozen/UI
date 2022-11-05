import math as m
print(f"Selamat mencoba Program Pemeriksa Nilai Dek Depe!\n=================================================\nMasukkan kunci jawaban:")
test, value, benar = [], None, 0
nilai = lambda a, b : m.floor((a/b)*100) #a benar, b total kunjaw
while not value == "STOP":
    value = input(str())
    if not value in ['A', 'B', 'C', 'D', 'E', 'STOP'] : exit(f"\n{value}, ga sesuai kriteria tolol")
    if value == "STOP" : break 
    test.append(value)
if len(test) == 0 : exit(f"MINIMAL 1 KUNJAW")
print(f"Masukkan jawaban kamu:")
answer = [input(str()) for i in range (len(test))]
for i in range (len(test)) : 
    if test[i] == answer[i] : benar += 1
if nilai(benar,len(test)) >= 85 : expression = "Selamat :D"
elif 55<=nilai(benar,len(test))<85 : expression = "Semangat :)"
else : expression = "nt"
print(f"\n{expression}\nTotal jawaban benar adalah {benar} dari {len(test)} soal\nNilai yang kamu peroleh adalah {nilai(benar,len(test))}")