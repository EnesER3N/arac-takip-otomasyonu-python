"""
--------------Otomasyon ÖZellikleri--------------
1. integer değere string değer girildiğinde veya boş geçildiğinde "lütfen geçerli id veya tc giriniz isleme devam etmek istiyormusunuz diye sorar"
evet yazılırsa bulunduğu döngüyü baştan çalıştırır. hayir yazılırsa bulunduğu döngüyu durdurur ana menüye gider.

2. aynı tc kilmlik numarası veya id girildiğinde zaten kayıtlı uyarısı verir entere bastığımız da ana menüye döner

3. müşteri silme yaparken kaydetmediğimiz müşteriyi silmeye çalışırsak yani yanlış tc giridiğimizde 
"bu tcye sahip bir müşteri kayıtlarda bulunumadı" hatası verir entere bastığımızda ana menüye döner.
"""

from os import system as sys # os kütüphanesinden system modülünü sys olarak import ediyoruz.

sys("cls") #

Tasitlar = [] #taşıtlar diye boş bir liste oluşturdum
Musteriler = [] # ''
kasa = 0  # kasa diye int değer oluşturdum araç kiralandığında araçların ücretleri toplanıyor
kiraya_verilen_araclar = [] # boş liste
bool1 = False # bool1 diye boolean bil değişken oluşturdum true yada false olarak kullanmak içim
bool2 = False # ''
bool3 = False
bool4 = False

class kiralik_araclar(): # kiralık araçlar diye sınıf oluşturdum
    def __init__(self, ID, marka, plaka, renk, fiyat:float):  # kiralık araçların özelliklerini fonksiyon içinde tanımladım başka fonksiyonlardan erişebilmek için
        self.ID = ID
        self.Marka = marka
        self.Plaka = plaka
        self.Renk = renk
        self.Fiyat = fiyat

class musteri_kayit(): # müşteri kayıt adında bir sınıf oluşturdum
    def __init__(self, TC, ad_soyad, tel, adres): # müşterilerin bilgilerini bir fonksiyon içinde tanımladım başka fonksiyonlardan erişmek için
        self.TC = TC
        self.ad_soyad = ad_soyad
        self.tel = tel
        self.adres = adres

class Otomobil(kiralik_araclar): # kiralık araçlardan miras aldım fonksiyonlarına erişmek için
    pass

class musteri(musteri_kayit):# müşteri kayıtlarından miras aldım fonksiyonlarına erişmek için
    pass

class kiraya_verilen_arac(): # kiraya verilen araçlar adında bir sınıf oluşturdum

    def __init__(self, ID, MARKA, PLAKA, RENK, TC, ISIM, TEL, ADRES): # kiraya verilen araçların özelliklerini fonksiyon içinde tanımladım başka fonksiyonlardan erişmek için

        self.arac_id = ID
        self.arac_marka = MARKA
        self.arac_plaka = PLAKA
        self.arac_renk = RENK
        self.kiraci_tc = TC
        self.kiraci_isim = ISIM
        self.kiraci_tel = TEL
        self.kiraci_adres = ADRES

def Musteri_Kayit(): # müşteri kayıt adında fonksiyon oluşturdum

    while True: # while döngüsü oluşturdum içindeki koşullar sağlandığı sürece program çalışmaya devam edicek

        try:
            TC = int(input("Müşterinin TC kimlik numarasını giriniz: ")) # müşteriden tc bilgi almak için integer dönen input oluşturdum

            TCS = [i.TC for i in Musteriler] #müşterilerin tc sini TCS isimli listeye ekliyorum.

            if TC in TCS: # girilen tc TCS listesinde var ise printi çalıştır.
                print(f"Zaten {TC} TC No'lu bir musteri kayitlarimizda bulunmaktadir!")
                break

        except ValueError as error: # tc değişkenine yanlış bir değer girilirse print çalışıcak
            print("Lutfen gecerli bir TC giriniz!")

            while True:

                karar = input("Isleme devam etmek istiyor musunuz? (Evet-Hayir): ")  # hata mesajından sonra kullancıya işleme devam etmek isiyormu sordum

                if karar == "Evet" or karar == "evet": # eğer kullanıcı evet yazdıysa veya küçük harfle evet yazdıysa
                    bool1 = True # bool ture olduğu kullanıcı işleme devam edicek
                    break # bu while döngüsünden çıkıcak tekrardan tc sorucak

                elif karar == "Hayir" or karar == "hayir": # eğer kullanıcı hayır yazdıysa veya küçük harflerle hayır yazdıysa
                    bool1 = False # bool false oluğunda kullanıcı işlemi sonladıracak
                    break # bu while döngüsünden çıkacak anasayfaya gidecek

                else:  # hata mesajından sorna geçerli bir bilgi girildiğinde akışa devam edicek
                    continue

            if bool1: # sonuç true olduğu zaman akış devam edicek
                continue

            else: # false olursa program durdurulacak
                break

        ad_soyad = str(input("Müşterinin Adı soyadı: ")) # ad soyad adında string değişken oluşturdum müşteri adı soyadını almak için

        try:
            tel = int(input("Müşteri Telefon numarası giriniz: ")) # tel adında integer değişken oluşturdum müşterinini telefon numarasını almak için
        except ValueError as error: # tel değişkeninde yanlış bir değer girilirse print çalışacak
            print("Lutfen gecerli bir telefon numarası giriniz!")

            while True:

                karar = input("Isleme devam etmek istiyor musunuz? (Evet-Hayir): ") # hata mesajından sonra kullancıya işleme devam etmek isiyormu sordum

                if karar == "Evet" or karar == "evet": # eğer kullanıcı evet yazdıysa veya küçük harfle evet yazdıysa
                    bool1 = True # bool ture olduğu kullanıcı işleme devam edicek
                    break  # bu while döngüsünden çıkıcak tekrardan geçerli bilgi  girmesini sağlayacak

                elif karar == "Hayır" or karar == "hayır":  # eğer kullanıcı hayır yazdıysa veya küçük harflerle hayır yazdıysa
                    bool1 = False # bool false oluğunda kullanıcı işlemi sonladıracak
                    break  # bu while döngüsünden çıkacak anasayfaya gidecek

                else: # hata mesajından sorna geçerli bir bilgi girildiğinde akışa devam edicek
                    continue

            if bool1: # sonuç true olduğu zaman akış devam edicek
                continue

            else: # false olursa program durdurulacak
                break

        adres = str(input("Müşterinin İkamet Adresini giriniz: "))   # adres adında string değişken oluşturdum müşterinin adresini almak için

        musteriKayit = musteri_kayit(TC, ad_soyad, tel, adres) # gelen verileri parametre olarak müşteri kayıt sınıfına verdim
        Musteriler.append(musteriKayit) # Musteriler listesine ekle, müşteri bilgilerini müşteriler lsitesine ekle

        print("\n","-------------------------","\n","Müşteri Kaydı Tamamlandı", # koşullar sağlandıktan sonra printi çalıştır
        "\n","-------------------------")
        break # fonksiyonu durdur

def musteri_sil(TC): # müşteri silmek için fonksiyon oluşturdum

    if len(Musteriler) > 0: # listenini uzunluğu 0 büyük ise
        for musteri in Musteriler: # for döngüsü müşteriler listesini tek tek dolaşıcak

            if TC == musteri.TC: # Tc si eşit olan müşteri tcyi bulacak
                #print("{} isimli musterinin kaydi silinmisitir.".format(musteri.ad_soyad))
                print(f"{musteri.ad_soyad} isimli musterinin kaydi silinmisitir.")  # hangi müşterinin silindiğini göster
                Musteriler.remove(musteri) # müşteriler listesinden sil
                bool3 = True
                break # döngüyü durdur akışa devam et

            else: # müşteri tcsi eşleşmediğinde diğer tc leri kontrol et
                bool3 = False
                continue

        if not bool3: # bool3 false olursa print çalışacak.
            print("Bu TC'ye sahip bir musteri kayitlarda bulunamadi!")

    else: # eğer müşteriler listesinde tc ile şeleşen yoksa printi çalıştır.
        print("Kayitlarda herhangi bir musteri bulunmamaktadir.")

def Otomobil_Ekle(): # otomobil ekleme fonksiyonu

    while True:

        try:
            ID = int(input("Otomobil ID'sini giriniz: "))  # ID adında integer değer oluşturdum otomobil idsini almak için
            IDS = [i.ID for i in Tasitlar] # Taşıtların İDlerini IDS listesine ekliyoruz.

            if ID in IDS: # ID IDS listesinde varsa printi çalıştır.
                print(f"Zaten {ID} ID degerine sahip bir arac kayitlarda bulunmaktadir!")
                break

        except ValueError as error: # hata yakalndığında printi çalıştır
            print("Lutfen gecerli bir ID degeri giriniz!")

            while True:

                karar = input("Isleme devam etmek istiyor musunuz? (Evet-Hayir): ") # hata mesajından sonra kullancıya işleme devam etmek isiyormu sordum

                if karar == "Evet" or karar == "evet":  # eğer kullanıcı evet yazdıysa veya küçük harfle evet yazdıysa
                    bool1 = True  # bool ture olduğu kullanıcı işleme devam edicek
                    break # bu while döngüsünden çıkıcak tekrardan geçerli bilgi  girmesini sağlayacak

                elif karar == "Hayır" or karar == "hayır": # eğer kullanıcı hayır yazdıysa veya küçük harflerle hayır yazdıysa
                    bool1 = False # bool false oluğunda kullanıcı işlemi sonladıracak
                    break  # bu while döngüsünden çıkacak anasayfaya gidecek

                else: # hata mesajından sorna geçerli bir bilgi girildiğinde akışa devam edicek
                    continue

            if bool1: # sonuç true olduğu zaman akış devam edicek
                continue

            else:  # false olursa program durdurulacak
                break

        marka = str(input("Otomobilin Marka ve Modelini giriniz: "))   # marka adında string değer oluşturdum otomobil  markasını almak için

        plaka = str(input("Otomobilin Plakasını giriniz: "))  # plaka adında string değer oluşturdum otomobil plakasını almak için

        renk = str(input("Otomobilin Rengini giriniz: "))  # renk adında string değer oluşturdum otomobil rengini almak için

        try:
            fiyat = float(input("Otomobilin Fiyatını giriniz: ")) # fiyat adında float değer oluşturdum otomobil fiyatını almak için
        except ValueError as error: # hata yakalndığında printi çalıştır
            print("Lutfen gecerli bir fiyat degeri giriniz!")

            while True:

                karar = input("Isleme devam etmek istiyor musunuz? (Evet-Hayir): ") # hata mesajından sonra kullancıya işleme devam etmek isiyormu sordum

                if karar == "Evet" or karar == "evet": # eğer kullanıcı evet yazdıysa veya küçük harfle evet yazdıysa
                    bool1 = True # bool ture olduğu kullanıcı işleme devam edicek
                    break # bu while döngüsünden çıkıcak tekrardan geçerli bilgi  girmesini sağlayacak

                elif karar == "Hayir" or karar == "hayir":  # eğer kullanıcı hayır yazdıysa veya küçük harflerle hayır yazdıysa
                    bool1 = False # bool false oluğunda kullanıcı işlemi sonladıracak
                    break# bu while döngüsünden çıkacak anasayfaya gidecek

                else:  # hata mesajından sorna geçerli bir bilgi girildiğinde akışa devam edicek
                    continue

            if bool1: # sonuç true olduğu zaman akış devam edicek
                continue

            else: # false olursa program durdurulacak
                break

        otomobil = Otomobil(ID, marka, plaka, renk, fiyat) # Otomobil sınıfından otomobil isimli bir obje oluşturuyoruz
        Tasitlar.append(otomobil) # taşıtlar listesine otombili ekle
        print("\n","-------------------------","\n",
        "ID: ",ID,"\n",
        "Marka: ",marka,"\n",
        "Renk: ",renk,"\n",
        "Plaka: ",plaka,"\n",
        "Fiyat: ",fiyat,"\n",
        "Otomobil Eklendi",
        "\n","-------------------------")
        break

def otomobil_fiyat_guncelle(ID, YeniFiyat): # fiyat guncelleme fonksiyonu oluşturdum

    IDS = [i.ID for i in Tasitlar] # taştların idleri yeni bir listeye atandı

    if len(IDS) != 0: # eğer IDS listesinde herhangi bir araca ait ID var ise for bloğuna gir (Eğer IDS listesinin uzunluğu 0'a eşit değilse yani boş değilse for bloğuna gir)

        if ID in IDS: # Eğer müşterinin girdiği ID, IDS listesinde bulunuyorsa if koşulu sağlanır

            for tasit in Tasitlar: # Tasitlar listesindeki her bir elemanı tasit isimli degisken adi altinda çek

                if ID == tasit.ID: # Eğer müşterinin girdiği ID herhangi bir taşıtın ID değeri ile eşleşirse:
                    tasit.Fiyat = YeniFiyat # eşleşen aracın fiyatını güncelle
                    print("{} id numaralı taştın yeni fiyatı: {}".format(tasit.ID, YeniFiyat)) # müşteriye fiyatın güncellendiğini bildir
                    bool4 = True # kontrol mekanizmasi için hazırlanan booleanı True olarak ayarla

                else:
                    bool4 = False # kontrol mekanizmasi için hazırlanan booleanı False olarak ayarla
                    continue

            if bool4: # boolean true ise pas geç
                pass

        else: # ID değerinde arac bulunmadiysa müşteriye bildir
            print("Bu ID değerine sahip taşıt bulunamadı")

    else: # Eğer taşıt listesi boş ise print çalıştır
        print("Kayitlarda fiyat guncellemek icin herhangi bir arac bulunamadi!")

def Otomobil_kirala(ID,TC): # otomobil kiralamak için fonksiyon oluşturuyorum.

    global kasa # kasa değikenini fonksiyon içerisinde kullanabilmek için global keywordu ile çağırıyoruz
    IDS = [i.ID for i in Tasitlar]  # taştların idleri yeni bir listeye atandı
    TCS = [t.TC for t in Musteriler] # müşterilerin  tcleri yeni bir listeye atandı

    if len(TCS) != 0: # eğer TCS listesinin uzunluğu sıfıra eşit değilse yani liste boş değilse if bloğuna gir

        if TC in TCS: # eğer girilen TC, TCS listesinde bulunuyor ise for bloğuna gir

            for musteri in Musteriler: # Musteriler listesindeki her bir elemanı musteri ismiyle çağır

                if TC == musteri.TC: # eğer girilen TC Musteriler listesindeki herhangi bir müşterinin TC'si ile eşleşirse:

                    if len(IDS) != 0: # eğer IDS listesinin uzunluğu sıfıra eşit değilse yani liste boş değilse if bloğuna gir

                        if ID in IDS: # eğer girilen ID, IDS listesinde bulunuyor ise for bloğuna gir

                            for tasit in Tasitlar: # # Tasitlar listesindeki her bir elemanı tasit ismiyle çağır

                                if ID == tasit.ID: # eğer girilen ID Tasitlar listesindeki herhangi bir tasitin ID'si ile eşleşirse:

                                    kiralik_arac = kiraya_verilen_arac(tasit.ID,tasit.Marka,tasit.Plaka,tasit.Renk,musteri.TC,musteri.ad_soyad,musteri.tel,musteri.adres) # kiraya_verilen_arac sınıfından kiralik_arac isimli bir obje oluşturuyorum

                                    if len(kiraya_verilen_araclar) > 0: # kiraya_verilen_araclar listesinin uzunluğu sıfırdan büyük ise yani boş değilse for bloğuna gir

                                        for arac in kiraya_verilen_araclar: # kiraya_verilen_araclar listesindeki her bir elemanı arac ismiyle cagir

                                            if tasit.ID == arac.arac_id: # eğer secilen aracın ID değeri kiraya_verilen_araclar listesindeki herhangi bir arac isimli objenin ID değerine eşitse if blouğnu sağla
                                                print("Bu arac zaten kiralanmis durumda!")
                                                break

                                            else: # eğer eşleşmiyorsa else bloğunu sağla ve yeni bir araç kirala
                                                kiraya_verilen_araclar.append(kiralik_arac) # kiraya_verilen_araclar listesine kiralanan araci ekle
                                                kasa += tasit.Fiyat # kasaya para ekle
                                                print("\n","-------------------------","\n","Müşteri TC no: ",TC,"\n","Arac İD no:",ID,
                                                    "Aracınız kiraya verildi","\n","-------------------------")
                                                break

                                    else: # eğer kiraya_verilen_araclar listesi boş ise hic aracın kiraya verilmiş olup olmadığını kontrol etmeden direkt ekle
                                                kiraya_verilen_araclar.append(kiralik_arac)
                                                kasa += tasit.Fiyat
                                                print("\n","-------------------------","\n","Müşteri TC no: ",TC,"\n","Arac İD no:",ID,
                                                    "Aracınız kiraya verildi","\n","-------------------------")



                        else:
                            print("Kiraya vermek istediginiz arac bulunamadi!")

                    else:
                        print("Kayitlarda herhangi bir arac bulunmamaktadir!")

        else:
            print("Aradiginiz TC ile kayitli musteri bulunamadi!")

    else:
        print("Kayitlarda herhangi bir musteri bulunmamaktadir!")

def kiralanan_araclari_listele(): # kiralanan araçları listelemek için bir fonksiyon oluşturuyoruz

    if len(kiraya_verilen_araclar) > 0: # eğer kiraya_verilen_araclar listesinin uzunluğu sıfırdan büyük üse for döngüsüne gir
        for i in kiraya_verilen_araclar: # kiraya_verilen_araclar listesindeki bütün elemanları i isminde bir değişken olarak çağır
            print(f"""
====================================================
Kiraya Verilen Aracin ID: {i.arac_id}
Kiraya Verilen Aracin Markasi: {i.arac_marka}
Kiraya Verilen Arac Plakasi: {i.arac_plaka}
Kiraya Verilen Arac Rengi: {i.arac_renk}
Aracin Verildigi Kisinin TC: {i.kiraci_tc}
Aracin Verildigi Kisinin Ismi: {i.kiraci_isim}
Aracin Verildigi Kisinin Telefonu: {i.kiraci_tel}
Aracin Verildigi Kisinin Adresi: {i.kiraci_adres}
====================================================
"""
            )

    else:
        print("Kiraya verilmis herhangi bir arac bulunamamistir.")
        input("Devam etmek icin ENTER'a basiniz.")

def arac_teslim_al(ID): # araçları teslim almak için bir fonksiyon oluşturuyoruz

    IDS = [i.arac_id for i in kiraya_verilen_araclar] # kiraya verilen aracların ID'lerini IDS isimli bir listeye ekliyoruz

    if len(kiraya_verilen_araclar) > 0: # ''

        if ID in IDS:

            for araclar in kiraya_verilen_araclar:

                if ID == araclar.arac_id:
                    print(f"{ID} ID numarali arac {araclar.kiraci_isim}'den teslim alinmistir.")
                    kiraya_verilen_araclar.remove(araclar) # kiraya_verilen_araclar listesinden secilen araclar objesini sil
                    break

                else:
                    continue

        else:
            print("Verdiginiz ID degerinde kiralamis oldugunuz bir arac bulunmamaktadir!")

    else:
        print("Kiraya verilmis herhangi bir arac bulunmamaktadir!")

def musterileri_listele():

    for musterii in Musteriler:
        print("\n","-------------------------","\n",
        "MÜŞTERİ TC: ", musterii.TC, "\n",
        "Müşteri Ad Soyad: ",musterii.ad_soyad, "\n",
        "Müşteri Tel: ", musterii.tel, "\n",
        "Müsteri Adres: ", musterii.adres,"\n",
        "-------------------------")

def tasitlari_listele():

    for tasit in Tasitlar:
        print("\n","--------------------------------------------------","\n",
        "Taşıt ID: ", tasit.ID,"\n",
        "Taşıt Marka Model: ", tasit.Marka,"\n",
        "Taşıt Plaka No: ",tasit.Plaka,"\n",
        "Taşıt Fiyatı: ",tasit.Fiyat,"\n",
        "Taşıt Renk: ",tasit.Renk,"\n"
        "--------------------------------------------------",)
while True: # Programın ana döngüsünü oluşturuyoruz
    sys("cls") # cmd'ye cls komutunu göndererek ekranı temizliyoruz

    print("\n", "ARAÇ KİRALAMA PROGRAMI: ")
    print(
        "0: Programdan Çık",
        "1: Müşteri Ekle", "2: Musteri sil",
        "3: Müşterileri listele", "4: Otomobil ekle",
        "5: Taşıtları Listele", "6: Taşıt Kiraya Ver",
        "7: Taşıt Fiyatı Güncelle", "8: Kiraya Verilen Araclari Listele",
        "9: Arac Teslim Al", "10: Kasayı Göster",
        sep="\n")

    try:
        secim = int(input("Seçiminizi giriniz: "))

    except ValueError as error: # Program yanlış input girişinden dolayı ValueError hatası verirse try-except bloğu ile bu hatayı kontrol altına alıyoruz
        print("Lutfen gecerli bir secim giriniz!")
        input("Devam etmek icin ENTER'a basiniz.")
        continue

    if secim == 0:
        sys("cls")

        while True: # Olası buglardan kaçınmak için 'onay' isimli inputu ayrı bir while döngüsü içerisinde kullanıyoruz

            onay = input("Cikmak istediginize emin misiniz? (Evet-Hayir)")

            if onay == "Evet" or onay == "evet":
                bool2 = True
                break

            elif onay == "Hayir" or onay == "hayir":
                bool2 = False
                break

            else:
                continue

        if bool2: # Eğer bool2 isimli boolean yukarıda True olarak belirlenirse ana döngüyü break fonksiyonu ile kırarak programı sonlandır
            print("\n","--------------------------------------------------","\n",
        "Araç Kiralama Takip Otomasyonundan çıktınız.",
        "\n","--------------------------------------------------","\n")
            break

        else: # Eğer bool2 false dönerse ana döngüye devam et
            continue

    elif secim == 1:
        sys("cls")
        Musteri_Kayit() # Musteri_Kayit fonksiyonunu çalıştırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 2: # Müşteri silme fonksiyonunu çalıştırıyoruz
        sys("cls")

        try:
            musteri_tc = int(input("Kaydini silmek istediginiz musterinin TC'sini giriniz: "))
            musteri_sil(musteri_tc) # musteri_sil fonksiyonunu çağırıyoruz
            input("Devam etmek icin ENTER'a basiniz.")

        except ValueError as error: # try-except hata ayıklama işlemi
            print("Lutfen gecerli bir TC giriniz!")
            input("Devam etmek icin ENTER'a basiniz.")
            continue

    elif secim == 3: # Müşterileri listeleme işlemini gerçekleştiriyoruz
        sys("cls")
        musterileri_listele()
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 4: # Otomobil ekleme işlemini gerçekleştiriyoruz
        sys("cls")
        Otomobil_Ekle() # Otomobil_Ekle fonksiyonunu çağırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 5: # Taşıtları listeleme işlemini gerçekleştiriyoruz
        sys("cls")
        tasitlari_listele() # tasitlari_listele fonksiyonunu çağırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 6: # Otomobil kiralama işlemini gerçekleştiriyoruz
        sys("cls")
        ID = int(input("Kiraya verilen aracın ID değerini giriniz: "))
        TC = int(input("Kiraya vermek istediğiniz müşterinin TC no giriniz: "))
        Otomobil_kirala(ID,TC) # Otomobil_kirala fonksiyonunu çağırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 7: # Otomobillerin fiyatlarını güncelleme işlemini gerçekleştiriyoruz
        sys("cls")
        ID = int(input("Değişiklik yapmak istediğiniz aracın ID değerini giriniz: "))
        yeniFiyat = int(input("Aracın Yeni Fiyatını giriniz: "))
        otomobil_fiyat_guncelle(ID, yeniFiyat) # otomobil_fiyat_guncelle fonksiyonunu çağırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 8: # Kiralanan araçları listeleme işlemini gerçekleştiriyoruz
        sys("cls")
        kiralanan_araclari_listele() # kiralanan_araclari_listele fonksiyonunu çağırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 9: # Araç teslim alma işlemini gerçekleştiriyoruz
        sys("cls")
        arac_id = int(input("Teslim almak istediginiz aracin ID'sini giriniz: "))
        arac_teslim_al(arac_id) # arac_teslim_al fonksiyonunu çağırıyoruz
        input("Devam etmek icin ENTER'a basiniz.")

    elif secim == 10: # Kasa isimli değişkenin değerini yazdırıyoruz
        sys("cls")
        print("\n", "Kasa:", kasa)
        input("Devam etmek icin ENTER'a basiniz.")
