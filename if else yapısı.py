soruk = input("Kullanıcı adınızı giriniz:")
sorup = input("Parolanızı giriniz:")
if len(soruk) + len(sorup) > 10:
    print("Kullanıcı adınız ve parolanız 10 karakteri geçemez.")

else:
    print("Kullanıcı adı ve şifreniz başarıyla oluşturuldu")
