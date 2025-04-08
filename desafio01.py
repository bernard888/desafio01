h1= int(input("coloque uma hora do dia: "))
m1 = int(input("digite os minutos dentro dessa hora: "))
h2 = int(input("coloque uma hora do dia: "))
m2 = int(input("digite os minutos dentro dessa hora: "))

hf = h1+h2
mf = m1+m2
if mf >=60:
   mf = mf % 60
   hf = hf+1
else:
    mf=mf
if hf>=13:
    hf = hf-24
else:
    hf = hf

print(f"{hf}:{mf}")