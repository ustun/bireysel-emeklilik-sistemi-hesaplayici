from __future__ import division

def bes_vs_faiz(aylik_yatirilan_para=100, yillik_faiz=8.5, fon_getirisi=5):
    n_ay = 12 * 10;

    toplam_para = 0
    aylik_faiz_orani = yillik_faiz * 1e-2 / 12

    for i in range(1, n_ay):
        toplam_para = toplam_para * (1 + aylik_faiz_orani) + aylik_yatirilan_para

    print "faizle biriken para", int(toplam_para)
    print "getiri yuzde ", int(toplam_para / (n_ay * aylik_yatirilan_para) * 100.0 - 100)

    # bes: devlet katkisi olan, fon getirisi olmayan para
    bes_fon_getirisi_olmadan_toplam_para = aylik_yatirilan_para * n_ay * 1.25
    print "bes ile sadece devlet katkisiyla biriken para", int(bes_fon_getirisi_olmadan_toplam_para)
    print "getiri yuzde ", int(bes_fon_getirisi_olmadan_toplam_para / (n_ay * aylik_yatirilan_para) * 100.0 - 100)

    # bes: devlet katkisi ve fon getirisi olan para
    toplam_para = 0
    aylik_fon_getirisi_orani = fon_getirisi * 1e-2 / 12

    for i in range(1, n_ay):
        toplam_para = toplam_para * (1 + aylik_fon_getirisi_orani) + (aylik_yatirilan_para * 1.25)
    print "bes ile devlet katkisi ve fon getirisi olarak biriken para", int(toplam_para)
    print "getiri yuzde ", int(toplam_para / (n_ay * aylik_yatirilan_para) * 100.0 - 100)



def karsilastirmalar():
    for yillik_faiz in map(lambda x: x /2, range(10, 22)):
        for fon_getirisi in map(lambda x: x/2, range(5, 15)):
            print "Yillik faiz", yillik_faiz,
            print "Fon getirisi", fon_getirisi
            bes_vs_faiz(yillik_faiz=yillik_faiz, fon_getirisi=fon_getirisi)
