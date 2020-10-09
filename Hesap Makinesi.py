seçenek1 = "(1) topla"
seçenek2 = "(2) çıkar"
seçenek3 = "(3) çarp"
seçenek4 = "(4) böl"
seçenek5 = "(5) karesini hesapla"
seçenek6 = "(6) karekök hesapla"

print(seçenek1, seçenek2, seçenek3, seçenek4, seçenek5, seçenek6, sep="\n")
soru = input("Yapmak istediğiniz işlemin kodunu giriniz.\n")


if soru == "1":
    sayı1 = int(input("İlk sayıyı giriniz.:"))
    sayı2 = int(input("İkinci sayıyı giriniz.:"))
    print("İşlemin sonucu:",sayı1 + sayı2)

elif soru == "2":
    sayı1 = int(input("İlk sayıyı giriniz.:"))
    sayı2 = int(input("İkinci sayıyı giriniz.:"))
    print("İşlemin sonucu:",sayı1 - sayı2)

elif soru == "3":
    sayı1 = int(input("İlk sayıyı giriniz.:"))
    sayı2 = int(input("İkinci sayıyı giriniz.:"))
    print("İşlemin sonucu:",sayı1 * sayı2)

elif soru == "4":
    sayı1 = int(input("İlk sayıyı giriniz.:"))
    sayı2 = int(input("İkinci sayıyı giriniz.:"))
    print("İşlemin sonucu:",sayı1 / sayı2)

elif soru == "5":
    sayı1 = int(input("Sayıyı giriniz.:"))
    print("İşlemin sonucu:",sayı1 ** 2)

elif soru == "6":
    sayı1 = int(input("Sayıyı giriniz.:"))
    print("İşlemin sonucu:",sayı1 ** 0.5)

else:
    print("Yanlış işlem koduyla işlem yapmaya çalıştınız...")

