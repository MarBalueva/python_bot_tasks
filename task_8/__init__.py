def main(s: str):
    res = {}
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    s = s.replace("<%", "")
    s = s.replace("%>", "")
    s = s.replace("loc", "")
    s = s.replace("==>", "")
    s = s.replace("==>q(", "'")
    s = s[:-1]
    for el in s.split(";"):
        name = el[el.find("'", 0, len(el) - 1) + 1: len(el) - 1]
        number = el[:el.find("'", 0, len(el) - 1)]
        res[name] = int(number)
    return res

print(main("<% loc 5770 ==>'geati_97'; loc -3698==> 'geleen'; loc -8150 ==> \
'latibe_258'; loc 3260 ==> 'vexe_292';%>"))
print(main("<% loc -9597==> 'orza_531'; loc -5923 ==> 'rieser'; loc -1431 ==> \
'maat_691'; loc 7665 ==>'ladier_143'; %>"))