import json,html
I=json.load(open('/workspace/imgs.json'))
T={d['t'][5:]:d for d in I}
def th(f):return T[f]['thumb'].split('?')[0]
def cp(f):return T[f]['page']
E_=html.escape
imgs=[
("百駿圖 卷","Eight Steeds? 否——A Hundred Steeds","1728（雍正六年）","國立故宮博物院（台北），故畫000916","A Hundred Steeds.jpg","https://digitalarchive.npm.gov.tw/Collection/Detail/3614?dep=P","公有領域（Commons）；故宮低階圖像開放使用","絹本設色 94.5×776.2 cm；《石渠寶笈初編》（御書房）著錄。"),
("百駿圖 稿本","One Hundred Horses (draft)","約1723–25","大都會藝術博物館（The Met）","One Hundred Horses (draft).jpg","https://www.metmuseum.org/art/collection/search/44632","Met Open Access 公有領域","與台北本構圖相符的白描稿，可看出「起稿—呈覽—成畫」流程。"),
("八駿圖 軸","Eight Steeds","約1723–35（雍正）","國立故宮博物院（台北），故畫000796","Eight Steeds.jpg","https://digitalarchive.npm.gov.tw/Collection/Detail/3574?dep=P","公有領域（Commons）；故宮低階圖像開放使用","款「臣郎世寧恭畫」仿宋體；《石渠寶笈續編》（重華宮）第四冊頁1864。"),
("郊原牧馬圖 卷（又稱八駿圖）","Herding Horses in the Countryside","雍正年間","故宮博物院（北京），新00154212","Herding Horses in the Countryside.jpg","https://www.dpm.org.cn/collection/paint/230375.html","公有領域（Commons）","故宮說明：背景樹石亦用明暗法，故判為雍正年間作品。"),
("十駿圖·霹靂驤","Ten Steeds: Pilixiang","1743","國立故宮博物院（台北）","Horse Pilixiang.jpg","https://digitalarchive.npm.gov.tw/Collection/Detail/13605?dep=P","公有領域（Commons）","同系列〈奔霄驄〉（1743）、〈如意驄〉（1748）見故宮數位典藏。右側連結為〈奔霄驄〉頁。"),
("十駿圖·紅玉座","Ten Steeds: Hongyuzuo","1748","國立故宮博物院（台北）","Horse Hongyuzuo.jpg","https://digitalarchive.npm.gov.tw/Collection/Detail/13620?dep=P","公有領域（Commons）","右側連結為同系列〈如意驄〉（1748）頁。"),
("愛烏罕四駿·超洱驄","Four Afghan Steeds (detail)","1763（乾隆二十八年）","國立故宮博物院（台北），故畫001049","Horse Chaoni'er.jpg","https://digitalarchive.npm.gov.tw/Collection/Detail?dep=P&id=3682","公有領域；故宮頁標 CC BY 4.0","乾隆嫌其「似則似矣遜古格」，命金廷標仿李公麟補畫牽馬人——中西畫格之爭的一手記錄。"),
("愛烏罕四駿·徠遠騮","Four Afghan Steeds (detail)","1763","國立故宮博物院（台北）","Horse Laiyuanliu.jpg","https://digitalarchive.npm.gov.tw/Collection/Detail?dep=P&id=3682","公有領域；故宮頁標 CC BY 4.0","畫上以滿、蒙、漢、回四體書馬名與尺寸。"),
("哈薩克貢馬圖 卷","Kazakhs Presenting Horses in Tribute","乾隆年間（Commons 標 Qing Dynasty）","法國吉美博物館（Musée Guimet）","Qazak pay tribute to Qianlong.jpg","https://commons.wikimedia.org/wiki/File:Qazak_pay_tribute_to_Qianlong.jpg","公有領域（Commons）","連結為 Commons 檔案頁（未查到可直連的吉美館藏品頁）。"),
("乾隆皇帝大閱圖 軸","The Qianlong Emperor in Ceremonial Armour on Horseback","1739（乾隆四年）","故宮博物院（北京）","The Qianlong Emperor in Ceremonial Armour on Horseback.jpg","https://www.dpm.org.cn/collection/paint/228806.html","公有領域（Commons）","帝王騎馬像——「肥馬」與皇權的典型。"),
]
imgs[0]=("百駿圖 卷","A Hundred Steeds")+imgs[0][2:]
trad=[
("龔開《駿骨圖》（俗稱瘦馬圖）","Emaciated Horse","宋末元初","大阪市立美術館（阿部コレクション）","Gong Kai, Emaciated Horse.jpg","https://dom.ocm.osaka/database/osaka-art-museum/128","公有領域（Commons）","題詩「今日有誰憐駿骨，夕陽沙岸影如山」（據台北故宮〈遺珠〉展頁）。瘦馬＝遺民自況的經典。"),
("韓幹《照夜白圖》","Night-Shining White","約750","大都會藝術博物館","唐 韓幹 照夜白圖 卷-Night-Shining White MET DP153679.jpg","https://www.metmuseum.org/art/collection/search/39901","CC0（Met Open Access）","杜甫譏「幹惟畫肉不畫骨」——肥瘦之辯的源頭。"),
]
def card(x):
  t,en,d,c,f,link,lic,note=x
  return f'''<figure class="card"><a href="{link}" target="_blank" rel="noopener"><img loading="lazy" src="{th(f)}" alt="{E_(t)}"></a>
<figcaption><b>{E_(t)}</b> <i>{E_(en)}</i><br><span class="m">{E_(d)} · {E_(c)}</span><br><span class="m">授權：{E_(lic)}</span><p>{E_(note)}</p>
<a href="{link}" target="_blank">館藏／出處頁</a> · <a href="{cp(f)}" target="_blank">高解析圖（Commons）</a></figcaption></figure>'''
def q(text,src,link):return f'<blockquote>{text}<cite>— <a href="{link}" target="_blank">{src}</a></cite></blockquote>'
W="https://zh.wikisource.org/wiki/"
S=[]
S.append(("一、郎世寧的馬：高解析公有領域圖像","教學用：同一位畫家從「百駿」群像到「十駿」單馬肖像，可讓學生比對中西畫法如何畫骨、畫肉、畫光。","".join(card(x) for x in imgs)+'<p class="note">另：〈十駿犬·霜花鷂〉軸（<a href="https://digitalarchive.npm.gov.tw/Collection/Detail/13639?dep=P" target="_blank">台北故宮數位典藏</a>）可與「十駿馬」對讀。<br>未找到：郎世寧本人明確題為「瘦馬」的作品；館方圖錄中的郎氏馬幾乎皆為肥健貢馬——「瘦馬」為《瘦馬行》一書的詮釋，宜在課上說明。</p>'))
S.append(("二、八駿與瘦馬的傳統","教學用：先講清「八駿」與「瘦馬」在中國畫史詩史裡的意思，學生才看得懂郎世寧接下的是什麼題目。",
q("天子之駿︰赤驥、盜驪、白義、踰輪、山子、渠黃、華騮、綠耳。","《穆天子傳》卷一（維基文庫）",W+"穆天子傳/卷一")+
'<p class="m">另見 <a href="https://ctext.org/mu-tianzi-zhuan/zh" target="_blank">中國哲學書電子化計劃·穆天子傳</a>；故宮博物院〈郊原牧馬圖〉說明亦引此八名及《拾遗记》另一說。</p>'+
q("東郊瘦馬使我傷，骨骼硉兀如堵牆。……見人慘澹若哀訴，失主錯莫無晶光。","杜甫〈瘦馬行〉（一作〈老馬〉），《全唐詩》卷217",W+"全唐詩/卷217")+
'<p class="note">《瘦馬行：郎世寧的中國經驗》書名即呼應杜甫此詩：官馬失主、被棄路旁——「瘦馬」作為被遺落的忠僕。（維基文庫另有<a href="'+W+'瘦馬行" target="_blank">李端同題詩</a>，勿混。）</p>'+
q("胡馬大宛名，鋒稜瘦骨成。竹批雙耳峻，風入四蹄輕。","杜甫〈房兵曹胡馬詩〉，《全唐詩》卷224",W+"全唐詩/卷224")+
q("弟子韓幹早入室，亦能畫馬窮殊相。幹惟畫肉不畫骨，忍使驊騮氣凋喪。","杜甫〈丹青引贈曹霸將軍〉",W+"丹青引贈曹霸將軍")+
'<p class="m">另見杜甫〈<a href="'+W+'韋諷錄事宅觀曹將軍畫馬圖" target="_blank">韋諷錄事宅觀曹將軍畫馬圖</a>〉（九馬圖，與「八駿」群馬構圖相關）。</p>'+
"".join(card(x) for x in trad)))
S.append(("三、一手文獻：石渠寶笈、活計檔、耶穌會書簡","教學用：讓學生看見畫是「奉旨活計」、被皇家著錄的，畫家同時是一位在宮中護教的修士。",
'<h3>《石渠寶笈》著錄</h3><ul><li>〈百駿圖〉：《石渠寶笈初編》（御書房）下冊頁1071——<a href="https://digitalarchive.npm.gov.tw/Collection/Detail/3614?dep=P" target="_blank">台北故宮著錄欄</a></li><li>〈八駿圖〉：《石渠寶笈續編》（重華宮）第四冊頁1864；鈐「石渠寶笈」「石渠定鑑」「寶笈重編」璽——<a href="https://digitalarchive.npm.gov.tw/Collection/Detail/3574?dep=P" target="_blank">台北故宮</a></li><li>〈愛烏罕四駿〉：《石渠寶笈續編》（寧壽宮）第六冊頁3052–3053——<a href="https://digitalarchive.npm.gov.tw/Collection/Detail?dep=P&id=3682" target="_blank">台北故宮</a></li><li>原書掃描：<a href="https://archive.org/details/02094634.cn" target="_blank">archive.org《欽定石渠寶笈續編》（七十）</a>等分冊（哈佛燕京藏本，可翻檢）。</li></ul><p class="note">未找到：維基文庫與 ctext 上可直接檢索的《石渠寶笈》郎世寧條目全文。</p>'+
'<h3>造辦處活計檔（經博物館與論文轉引）</h3>'+
q("乾隆二十八年(1763)九月二十六日交畫『愛烏罕四駿』手卷一卷，傳旨著交如意館配袱別樣子，發往蘇州織造廠，依從前做法照樣做來。","《活計檔》，轉引自台北故宮〈愛烏罕四駿〉研究說明（林莉娜）","https://digitalarchive.npm.gov.tw/Collection/Detail?dep=P&id=3682")+
q("着畫西洋畫人來圓明園畫古玩，不必着郎石（世）宁來，欽此。（雍正八年六月十三日）","曹天成〈郎世寧與他的中國合作者〉，《故宮博物院院刊》2012年第3期（PDF）","https://www.dpm.org.cn/Uploads/File/2018/06/15/u5b2371c0861e4.pdf")+
q("據清宮內務府檔案，雍正二年（1724）三月曾令郎世寧作百駿圖一卷。","台北故宮「神筆丹青」特展·圖成百駿","https://theme.npm.edu.tw/exh104/giuseppecastiglione/ch/page-4.html")+
'<p class="note">未找到：活計檔原檔的免費線上全文/影像（《清宮內務府造辦處檔案總匯》為2007年影印出版物）；以上均為權威轉引。</p>'+
'<h3>耶穌會書簡 Lettres édifiantes et curieuses（1780–81 年版，archive.org）</h3>'+
q("…que puisque Sounou leur père étoit mort, il falloit délibérer sur le traitement qu’on devoit faire à ses enfans…（雍正帝議處蘇努諸子）","第20卷，巴多明（Parennin）1726年8月24日北京書簡","https://archive.org/details/lettresdifiantes20jesu")+
q("Le Frère quitta son pinceau… il se mit à genoux… il tira de son sein notre mémorial enveloppé de soie jaune.… « je le lirai, soyez tranquille, et continuez de peindre. »（郎世寧放下畫筆跪呈護教奏摺）","第20卷 約頁358–359","https://archive.org/details/lettresdifiantes20jesu")+
q("Lettre du Frère Attiret… peintre au service de l’Empereur de la Chine, à M. d’Assaut. À Peking, le 1 novembre 1743.（王致誠記圓明園書簡）","第22卷","https://archive.org/details/lettresdifiantes22jesu")+
q("…ne sçavez-vous pas ce que j’ai fait pour Castiglione à sa septantième année ?（乾隆追憶為郎世寧做七十壽）","第24卷","https://archive.org/details/lettresdifiantes24jesu")+
'<p class="note">中譯本《耶穌會士中國書簡集》（大象出版社）受版權保護，未找到合法免費全文。法文引文按原 OCR 校正長s。</p>'))
links=[("神筆丹青—郎世寧來華三百年特展·展覽概述","國立故宮博物院 2015","https://theme.npm.edu.tw/exh104/giuseppecastiglione/ch/index.html"),
("神筆丹青·圖成百駿","國立故宮博物院","https://theme.npm.edu.tw/exh104/giuseppecastiglione/ch/page-4.html"),
("郎世寧與他的中國合作者（曹天成，即本書作者）","《故宮博物院院刊》2012-3，PDF","https://www.dpm.org.cn/Uploads/File/2018/06/15/u5b2371c0861e4.pdf"),
("通景畫與郎世寧遺產研究（李啟樂）","故宮博物院 PDF","https://www.dpm.org.cn/Uploads/File/2018/06/15/u5b237189e7e11.pdf"),
("畫馬和郎世寧的〈八駿圖〉","故宮博物院·講畫","https://www.dpm.org.cn/paints/talk/203420.html"),
("郎世寧繪畫中的顏料與設色（陳東和）","台北故宮研討會論文 PDF","https://theme.npm.edu.tw/seminar/10410/images/2/ch/2-1-3.pdf"),
("郎世寧與瓷器（余佩瑾）","《故宮學術季刊》32卷2期 PDF","https://www.npm.gov.tw/NewChineseArtDownload.ashx?bid=3853"),
("南院年度特展簡介：十駿犬","台北故宮 PDF","https://www.npm.gov.tw/NewChineseArtDownload.ashx?bid=3495"),
("遺珠—大阪市立美術館珍藏書畫（含龔開〈駿骨圖〉）","台北故宮 2021","https://theme.npm.edu.tw/exh110/HiddenGems/ch/page-2.html"),
("台北故宮 Open Data 開放資料","國立故宮博物院","https://theme.npm.edu.tw/opendata/")]
S.append(("四、權威研究與展覽頁","教學用：備課時的可靠背景，避免網路傳說；其中曹天成論文即《瘦馬行》作者的檔案功夫。","<ul>"+"".join(f'<li><a href="{u}" target="_blank">{E_(a)}</a> <span class="m">— {E_(b)}</span></li>' for a,b,u in links)+"</ul>"))
S.append(("五、可以做成課件的三個方向","僅據上列資料。",'''<ol><li><b>肥與瘦：一匹馬的兩種畫法</b>——以杜甫「幹惟畫肉不畫骨」為題，並排韓幹〈照夜白〉、龔開〈駿骨圖〉、郎世寧〈愛烏罕四駿〉，再讀乾隆「似則似矣遜古格」的評語，讓孩子用毛筆白描與明暗素描各畫一匹馬。</li>
<li><b>從八駿到百駿：構圖課</b>——由《穆天子傳》八駿名出發，對照〈八駿圖〉軸、〈郊原牧馬圖〉卷、〈百駿圖〉稿本與成品，講手卷的近大遠小與「起稿—呈覽—成畫」流程（活計檔：雍正二年命畫百駿）。</li>
<li><b>跪下的畫家：信仰與職分</b>——讀《書簡》中郎世寧放下畫筆跪呈奏摺、蘇努一家受禁的記載，配杜甫〈瘦馬行〉「失主錯莫無晶光」，討論在異鄉忠於呼召的人如何以手藝服事，並以「臣郎世寧恭畫」款識引入落款與印章課。</li></ol>'''))
body="".join(f'<section><h2>{h}</h2><p class="why">{w}</p>{c}</section>' for h,w,c in S)
open("index.html","w").write(f'''<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>郎世寧 · 瘦馬與八駿 資料彙編</title>
<style>body{{margin:0;background:#f3ead7;color:#3a2e22;font:16px/1.75 "Noto Serif CJK TC","Songti TC",serif}}
header{{padding:2.2em 1em 1.4em;text-align:center;border-bottom:3px double #8c3b2a;background:linear-gradient(#efe2c6,#f3ead7)}}
h1{{margin:0;font-size:1.7em;letter-spacing:.15em;color:#5a2a1c}}header p{{margin:.4em 0 0;color:#7a6650;font-size:.92em}}
.seal{{display:inline-block;border:2px solid #b0362a;color:#b0362a;padding:0 .3em;margin-top:.5em;font-size:.85em}}
main{{max-width:980px;margin:auto;padding:0 1em 3em}}section{{margin-top:2.2em}}h2{{color:#5a2a1c;border-left:5px solid #b0362a;padding-left:.5em;font-size:1.3em}}h3{{color:#6b4a2e;font-size:1.05em}}
.why{{background:#fbf5e6;border:1px dashed #c9b38a;padding:.4em .8em;color:#6b4a2e;font-size:.93em}}
section>figure.card{{display:inline-block;vertical-align:top;width:calc(50% - 1.2em);margin:.5em;background:#fbf6ea;border:1px solid #d8c7a3;box-shadow:0 1px 3px #0001}}
.card img{{width:100%;height:220px;object-fit:cover;display:block;background:#e7dcc3}}figcaption{{padding:.6em .8em;font-size:.9em}}figcaption i{{color:#7a6650}}figcaption p{{margin:.3em 0}}
.m{{color:#7a6650;font-size:.88em}}a{{color:#8c3b2a}}blockquote{{margin:1em 0;padding:.6em 1em;background:#fbf6ea;border-left:3px solid #c9b38a;font-size:1.02em}}cite{{display:block;font-size:.82em;color:#7a6650;margin-top:.3em;font-style:normal}}
.note{{font-size:.88em;color:#6b4a2e}}footer{{text-align:center;font-size:.8em;color:#7a6650;padding:2em 1em}}
@media(max-width:640px){{section>figure.card{{width:100%;margin:.6em 0}}h1{{font-size:1.35em}}}}</style></head><body>
<header><h1>郎世寧 · 瘦馬與八駿</h1><p>Giuseppe Castiglione（1688–1766）一手資料與公有領域圖像彙編<br>配讀：曹天成《瘦馬行：郎世寧的中國經驗》（中華書局 2017）</p><span class="seal">為聰偉整理</span></header>
<main>{body}</main><footer>所有連結於 2026-11-01 以 curl 檢查（403 保留、404 剔除）。圖像縮圖直連 Wikimedia Commons。</footer></body></html>''')
