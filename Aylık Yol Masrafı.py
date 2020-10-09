gidiş_ücreti = 2.25 #Bu ilk 3 satırda masrafı hesaplamak için ihtiyacımız olan değişkenleri belirttim.
dönüş_ücreti = 2.7
çalışılan_gün= 25
masraf = (gidiş_ücreti + dönüş_ücreti) * çalışılan_gün #Masraf değişkeni toplam maliyeti hesaplamak için gerekli formülü barındırıyor.
print("*"*10,'AYLIK YOL MASRAFI',"*"*10)#Tırnak içerisinde bulunan yıldızlar 10 sayısı ile çarpıldığında ekrana 10 adet yıldız yazılıyor.(Süslemek için)
print("Çalışılan gün sayısı:", çalışılan_gün)#Burada özel birşey yok.\t ifadesi dışında.\t dizisi klavyedeki tab'ın görevini yapıyor.(Görsellik nedeniyle)
print("Gidiş ücreti\t:", gidiş_ücreti,"TL")
print("Dönüş ücreti\t:", dönüş_ücreti,"TL")
print("*"*10,"Sonuç","*"*10)
print("Yol Masrafı\t:",masraf,"TL")


