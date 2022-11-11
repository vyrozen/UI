def Lower(inString):
    return(inString.lower())

x = None
print(f"Selamat datang di program Mengenal Angkatan!\n===========================================\nMasukkan identitas mahasiswa:")
while not x == 'STOP':
    x = str(input()) #Input 0 = Nama (Only front), 1 = NIM(Int Unique), 2 = Separator, 3 = Day(Int 1-31), 4 = Month(Incasesensitive - 12 posisbilities), 5 = 2004(Int).
