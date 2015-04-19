__author__ = 'volodya'
import urllib2

provinces = {'01':'22', '02':'24', '03':'23', '04':'25', '05':'03','06':'04','07':'08','08':'19','09':'20','10':'21','11':'09','13':'10','14':'11', '15':'12', '16':'13', '17':'14', '18':'15', '19':'16','21':'17', '22':'18', '23':'06', '24':'01', '25':'02', '26':'07', '27':'05'}

for key in provinces:
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + str(key) + ".txt"
    vhi_url = urllib2.urlopen(url)
    print(vhi_url)
    name = 'provinces/vhi_id_' + str(provinces[key]) + '.csv'
    out = open(name, 'wb')
    out.write(vhi_url.read())
    out.close()
print("VHI is downloaded")
