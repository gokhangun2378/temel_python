def pascalucgeni(yukseklik,satirlar=[]):
    satirlar.append([1])
    satir=[1]
    for i in range(yukseklik):
        sonraki=0
        siradaki_satir=[]
        for k in satir:
            siradaki_satir.append(sonraki+k)
            sonraki=k
            siradaki_satir.append(1)

            satir=siradaki_satir
            satirlar.append(satir)
    return satirlar

sayi=int(input("yüksekligini giriniz:"))

for x in pascalucgeni(sayi):
    print(x)

