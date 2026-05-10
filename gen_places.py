#!/usr/bin/env python3
"""Generate places.json from RFC data"""
import json

def g(id, name, nameZh, city, cityZh, region, category, coordinates, tags, bestSeason="夏季", suitableFor=None):
    if suitableFor is None:
        suitableFor = ["family", "couple", "solo"]
    return {
        "id": id, "name": name, "nameZh": nameZh,
        "city": city, "cityZh": cityZh, "region": region,
        "category": category, "tags": tags,
        "coordinates": coordinates,
        "description": "",
        "bestSeason": bestSeason,
        "suitableFor": suitableFor,
        "photos": [], "photoUrl": "",
        "googleSearchUrl": f"https://www.google.com/search?q={name}&tbm=isch",
        "mapsUrl": f"https://www.google.com/maps/search/?api=1&query={name}@{coordinates[0]},{coordinates[1]}"
    }

places = [
    # Durrës (6)
    g("drs-beach-1","Durrës Beach","都拉斯海灘","Durrës","都拉斯","coastal","beach",[41.310,19.470],["kid-friendly","crowded","sunset"]),
    g("drs-amphitheater-1","Durrës Amphitheatre","都拉斯圓形劇場","Durrës","都拉斯","coastal","historic",[41.316,19.447],["history","architecture"]),
    g("drs-castle-1","Durrës Castle","都拉斯城堡","Durrës","都拉斯","coastal","historic",[41.308,19.443],["history","sunset"]),
    g("drs-roman-villa-1","Roman Villa of Durrës","都拉斯羅馬別墅","Durrës","都拉斯","coastal","historic",[41.312,19.450],["history","family"]),
    g("drs-bay-1","Durrës Bay","都拉斯灣","Durrës","都拉斯","coastal","scenic",[41.305,19.475],["sunset","instagram-worthy"]),
    g("drs-wetland-1","Kune-Vain Lagoon","庫內-瓦因瀉湖","Durrës","都拉斯","coastal","nature",[41.580,19.560],["bird-watching","secluded"]),

    # Vlorë (7)
    g("vlr-beach-1","Vlorë Beach","發羅海灘","Vlorë","發羅","coastal","beach",[40.466,19.485],["kid-friendly","sunset"]),
    g("vlr-karaburun-1","Karaburun Peninsula","卡拉伯倫半島","Vlorë","發羅","coastal","nature",[40.380,19.380],["hiking","secluded","mountain"]),
    g("vlr-sazan-1","Sazan Island","薩贊島","Vlorë","發羅","coastal","beach",[40.500,19.280],["diving","snorkeling","secluded"]),
    g("vlr-akrolli-1","Akrolli Coastal Tower","阿克羅利海岸塔","Vlorë","發羅","coastal","historic",[40.440,19.460],["history","instagram-worthy"]),
    g("vlr-dyrmishi-1","Dymishti Waterfall","迪米斯蒂瀑布","Vlorë","發羅","coastal","nature",[40.510,19.620],["nature","hiking"]),
    g("vlr-zvernec-1","Zvernec Island","茲維爾內茨島","Vlorë","發羅","coastal","scenic",[40.510,19.400],["instagram-worthy","sunset"]),
    g("vlr-narta-1","Narta Lagoon","納爾塔瀉湖","Vlorë","發羅","coastal","nature",[40.520,19.420],["bird-watching","secluded"]),

    # Sarandë (9)
    g("sar-beach-1","Sarandë Beach","希格拉海灘","Sarandë","希格拉","coastal","beach",[39.875,20.010],["kid-friendly","crowded","sunset"]),
    g("sar-ksamil-1","Ksamil Beach","克薩米爾海灘","Sarandë","希格拉","coastal","beach",[39.770,20.005],["instagram-worthy","sunset","kid-friendly"]),
    g("sar-ksamil-islands-1","Ksamil Islands","克薩米爾群島","Sarandë","希格拉","coastal","beach",[39.760,19.995],["snorkeling","diving","secluded"]),
    g("sar-butrint-1","Butrint Ancient City","布特林特古城","Sarandë","希格拉","coastal","historic",[39.745,20.030],["history","architecture"]),
    g("sar-blue-eye-1","The Blue Eye","藍眼泉","Sarandë","希格拉","coastal","nature",[39.890,20.130],["nature","hiking"]),
    g("sar-buka-1","Buna River Delta","布納河三角洲","Sarandë","希格拉","coastal","nature",[39.820,20.150],["nature","bird-watching"]),
    g("sar-kanali-1","Kanal Beach","運河海灘","Sarandë","希格拉","coastal","beach",[39.855,20.020],["kid-friendly","sunset"]),
    g("sar-hilo-1","Hilo Beach","希洛海灘","Sarandë","希格拉","coastal","beach",[39.865,20.035],["instagram-worthy","secluded"]),
    g("sar-mirror-1","Mirror Beach","鏡子海灘","Sarandë","希格拉","coastal","scenic",[39.780,20.015],["instagram-worthy","sunset"]),

    # Albanian Riviera (15)
    g("riv-himara-1","Himara Beach","希瑪拉海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.105,19.740],["kid-friendly","sunset"]),
    g("riv-himara-old-1","Himara Old Town","希瑪拉老城","Albanian Riviera","里維耶拉","riviera","city",[40.100,19.730],["architecture","history"]),
    g("riv-borsh-1","Borsh Beach","博爾什海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.060,19.690],["secluded","instagram-worthy"]),
    g("riv-dhermi-1","Dhermi Beach","德赫爾米海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.025,19.640],["sunset","instagram-worthy"]),
    g("riv-jale-1","Jale Beach","雅萊海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.015,19.620],["diving","snorkeling"]),
    g("riv-drimades-1","Drimades Beach","德里馬德斯海灘","Albanian Riviera","里維耶拉","riviera","beach",[39.980,19.600],["secluded","sunset"]),
    g("riv-himaranta-1","Himaranta Beach","希瑪蘭塔海灘","Albanian Riviera","里維耶拉","riviera","beach",[39.970,19.590],["kid-friendly"]),
    g("riv-vuno-1","Vuno Beach","武諾海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.010,19.580],["instagram-worthy","sunset"]),
    g("riv-pilur-1","Pilur Castle","皮魯爾城堡","Albanian Riviera","里維耶拉","riviera","historic",[40.055,19.650],["history","sunset"]),
    g("riv-qeparo-1","Qeparo Beach","切帕羅海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.040,19.670],["secluded"]),
    g("riv-sheshi-1","Porto Palermo Beach","波爾托帕拉莫海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.120,19.720],["sunset","architecture"]),
    g("riv-pasha-1","Pasha Liman Beach","帕夏港海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.080,19.750],["kid-friendly","sunset"]),
    g("riv-cape-1","Cape of Gjiri i Kritis","克里特角","Albanian Riviera","里維耶拉","riviera","scenic",[39.950,19.570],["instagram-worthy","sunset"]),
    g("riv-fterra-1","Fterra Beach","夫特拉海灘","Albanian Riviera","里維耶拉","riviera","beach",[40.030,19.620],["diving","secluded"]),
    g("riv-lukove-1","Lukovë Beach","盧科韋海灘","Albanian Riviera","里維耶拉","riviera","beach",[39.930,19.550],["instagram-worthy","secluded"]),

    # Tirana (9)
    g("tir-square-1","Skanderbeg Square","斯坎德培廣場","Tirana","地拉那","central","city",[41.327,19.818],["architecture","urban"]),
    g("tir-mosque-1","Et'hem Bey Mosque","埃特姆貝清真寺","Tirana","地拉那","central","city",[41.331,19.821],["architecture","history"]),
    g("tir-bunker-1","Bunker 21","21號地堡","Tirana","地拉那","central","city",[41.318,19.810],["instagram-worthy","history"]),
    g("tir-clock-1","Clock Tower of Tirana","地拉那鐘塔","Tirana","地拉那","central","city",[41.329,19.824],["architecture","sunset"]),
    g("tir-park-1","Grand Park of Tirana","大地拉那公園","Tirana","地拉那","central","nature",[41.315,19.800],["kid-friendly","family"]),
    g("tir-lake-1","Tirana Lake (Lake of Pazar)","帕扎爾湖","Tirana","地拉那","central","nature",[41.340,19.840],["hiking","family"]),
    g("tir-museum-1","National History Museum","國家歷史博物館","Tirana","地拉那","central","historic",[41.319,19.824],["history","family"]),
    g("tir-blloku-1","Blloku District","布洛庫區","Tirana","地拉那","central","city",[41.319,19.807],["food","urban","nightlife"]),
    g("tir-mount-dajt-1","Mount Dajti","達伊蒂山","Tirana","地拉那","central","nature",[41.360,19.910],["hiking","scenic","sunrise"]),

    # Gjirokastër (6)
    g("gji-castle-1","Gjirokastër Castle","吉諾卡斯特城堡","Gjirokastër","吉諾卡斯特","central","historic",[40.076,20.140],["history","architecture","sunset"]),
    g("gji-zagarotti-1","Zagarotti House","扎加羅蒂之家","Gjirokastër","吉諾卡斯特","central","historic",[40.072,20.135],["architecture","instagram-worthy"]),
    g("gji-old-town-1","Gjirokastër Old Town","吉諾卡斯特老城","Gjirokastër","吉諾卡斯特","central","city",[40.075,20.138],["architecture","instagram-worthy"]),
    g("gji-safary-1","Libohovë Palace","利博霍韋宮","Gjirokastër","吉諾卡斯特","central","historic",[40.050,20.160],["history","architecture"]),
    g("gji-sword-1","The Stone Sword of Gjirokastër","吉諾卡斯特石劍","Gjirokastër","吉諾卡斯特","central","scenic",[40.078,20.145],["instagram-worthy"]),
    g("gji-enclosed-1","Gjirokastër Enclosed City","封閉式山城","Gjirokastër","吉諾卡斯特","central","city",[40.070,20.130],["architecture","history"]),

    # Berat (6)
    g("ber-castle-1","Berat Castle","培拉特城堡","Berat","培拉特","central","historic",[40.325,19.950],["history","architecture","sunset"]),
    g("gor-bridge-1","Gorica Bridge","戈里察橋","Berat","培拉特","central","historic",[40.320,19.940],["architecture","instagram-worthy"]),
    g("ber-mangal-1","Mangalemi Quarter","曼加利米區","Berat","培拉特","central","city",[40.323,19.952],["architecture","instagram-worthy"]),
    g("ber-church-1","Church of St. Mary","聖母教堂","Berat","培拉特","central","historic",[40.326,19.948],["history","architecture"]),
    g("ber-kala-1","Kala River","卡拉河","Berat","培拉特","central","nature",[40.318,19.935],["nature","hiking"]),
    g("ber-hassan-1","Hassan Bey Mosque","哈桑貝清真寺","Berat","培拉特","central","city",[40.322,19.946],["architecture"]),

    # Shkodra (7)
    g("shk-rozafa-1","Rozafa Castle","羅扎法城堡","Shkodra","斯庫台","mountain","historic",[42.040,19.930],["history","architecture","sunset"]),
    g("shk-lake-1","Shkodra Lake","斯庫台湖","Shkodra","斯庫台","mountain","nature",[42.050,19.620],["bird-watching","family","kid-friendly"]),
    g("shk-lezha-1","Lezha Castle","萊扎城堡","Shkodra","斯庫台","mountain","historic",[41.750,19.630],["history"]),
    g("shk-vendor-1","Vendotëna Tower","溫多托納塔","Shkodra","斯庫台","mountain","historic",[42.070,19.870],["history","instagram-worthy"]),
    g("shk-river-1","Buna River","布納河","Shkodra","斯庫台","mountain","nature",[42.060,19.600],["boat","nature"]),
    g("shk-pema-1","Pema e Thatë","白楊大道","Shkodra","斯庫台","mountain","scenic",[42.045,19.910],["instagram-worthy","sunset"]),
    g("shk-bazaar-1","Shkodra Bazaar","斯庫台市集","Shkodra","斯庫台","mountain","city",[42.038,19.925],["food","urban"]),

    # Northern Mountains (15)
    g("nth-theth-1","Theth Village","特塞村","Northern Mountains","北部山區","mountain","nature",[42.380,19.810],["hiking","rural","alpine"]),
    g("nth-theth-church-1","Theth Church","特塞教堂","Northern Mountains","北部山區","mountain","historic",[42.382,19.813],["history","architecture"]),
    g("nth-valbona-1","Valbona Valley","瓦爾博納山谷","Northern Mountains","北部山區","mountain","nature",[42.420,19.880],["hiking","mountain","alpine"]),
    g("nth-valbona-pass-1","Valbona Pass","瓦爾博納山口","Northern Mountains","北部山區","mountain","scenic",[42.400,19.870],["hiking","sunrise"]),
    g("nth-koman-1","Koman Lake","科曼湖","Northern Mountains","北部山區","mountain","nature",[42.150,19.920],["hiking","boat","scenic"]),
    g("nth-koman-trail-1","Koman–Valbona Trail","科曼-瓦爾博納步道","Northern Mountains","北部山區","mountain","activity",[42.200,19.900],["hiking","alpine"]),
    g("nth-rrajca-1","Rrajca Lake","拉伊卡湖","Northern Mountains","北部山區","mountain","nature",[42.050,20.050],["hiking","secluded"]),
    g("nth-bogaj-1","Bogaj Mountain Pass","博加伊山口","Northern Mountains","北部山區","mountain","scenic",[42.350,19.840],["hiking","sunrise"]),
    g("nth-cedia-1","Çedia e Fratit","弗拉蒂峰","Northern Mountains","北部山區","mountain","scenic",[42.390,19.830],["hiking","sunrise"]),
    g("nth-kyr-1","Kyrë e Madhe","大基爾峰","Northern Mountains","北部山區","mountain","nature",[42.410,19.850],["hiking","alpine"]),
    g("nth-boge-1","Bogë Village","博格村","Northern Mountains","北部山區","mountain","nature",[42.480,19.800],["hiking","rural","skiing"]),
    g("nth-kukaj-1","Kukaj Waterfall","庫卡伊瀑布","Northern Mountains","北部山區","mountain","nature",[42.370,19.830],["nature","hiking"]),
    g("nth-don-1","Don Path","唐恩小徑","Northern Mountains","北部山區","mountain","activity",[42.395,19.815],["hiking","secluded"]),
    g("nth-pretash-1","Pretash Lake","普雷塔什湖","Northern Mountains","北部山區","mountain","nature",[42.440,19.860],["hiking","secluded"]),
    g("nth-vukaj-1","Vukaj Hot Springs","武凱溫泉","Northern Mountains","北部山區","mountain","nature",[42.350,19.820],["activity","family"]),

    # Extra (5)
    g("div-kruja-1","Kruja Castle","克魯亞城堡","Kruja","克魯亞","central","historic",[41.507,19.800],["history","architecture"]),
    g("div-divjakara-1","Divjakara Beach","迪維亞卡拉海灘","Divjakara","迪維亞卡拉","coastal","beach",[40.870,19.560],["kid-friendly","sunset"]),
    g("div-olive-1","Adriatic Olive Groves","亞得里亞橄欖林","Divjakara","迪維亞卡拉","coastal","scenic",[40.900,19.600],["instagram-worthy","sunset"]),
    g("div-leng-1","Lengar Cliff","倫格懸崖","Lengar","倫格","coastal","scenic",[40.350,19.450],["instagram-worthy","sunset"]),
    g("div-vas-1","Vashtemi Vineyard","瓦什泰米酒莊","Vashtemi","瓦什泰米","central","food",[40.100,20.180],["food","instagram-worthy"]),
]

data = {
    "version": "1.0",
    "tripInfo": {
        "destination": "阿爾巴尼亞",
        "startDate": "2026-07-01",
        "endDate": "2026-07-14",
        "base": "地拉那（阿爾巴尼亞定點深度遊）",
        "totalDays": 14
    },
    "places": places
}

with open('/home/node/.openclaw/workspace/albania-trip/places.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Generated {len(places)} places")
