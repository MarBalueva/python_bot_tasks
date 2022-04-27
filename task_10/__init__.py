def change(s):
    s = list(filter(None, s))
    for i in range(len(s)):
        if ' ' in s[i]:
            s[0] = s[i][s[i].index(' ') + 1:]
        elif s[i].count('.') == 1:
            s[i] += '0'
        else:
            s[i] = s[i].replace('.', '-')
    s2 = []
    for item in s:
        if item not in s2:
            s2.append(item)
    return s2


def main(s):
    for i in range(len(s)):
        s[i] = change(s[i])
    s = list(filter(None, s))
    s = sorted(s, key=lambda s_list: s_list[0].split()[-1])
    trans_s = [[s[j][i] for j in range(len(s))] for i in range(len(s[0]))]
    return trans_s


print(main([["В.Б. Лурамов", "0.50", "25.10.04", "25.10.04"], [None, None, None, None], ["М.Д. Табов", "0.29", "10.11.00", "10.11.00"],
           [None, None, None, None], ["Т.Ц. Могберг", "0.55", "04.08.04", "04.08.04"]]))
print(main([["Н.Л. Сунидов", "0.10", "05.01.01", "05.01.01"], [None, None, None, None],
            [None, None, None, None], ["А.Ш. Фобян", "0.65", "03.08.99", "03.08.99"],
            ["А.Г. Гудишиди", "0.77", "25.06.02", "25.06.02"], ["Д.Д. Руцодак", "0.25", "17.01.00", "17.01.00"]]))
