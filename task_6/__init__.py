s = {
    'ASP':
    {
        2008:
        {
            'SHEN':
            {
                1971: 0,
                1975: 1
            },
            'ORG': 2,
            'DYLAN':
            {
                1971: 3,
                1975: 4
            }
        },
        1972:
        {
            1971:
            {
                1971: 5,
                1975: 6
            },
            2016: 7,
            1967:
            {
                'SHEN': 8,
                'ORG': 9,
                'DYLAN': 10
            }
        }
    },
    'NINJA': 11
}


def main(path):
    s1 = s[path[1]]
    if path[1] == 'ASP':
        s2 = s1[path[3]]
        if path[3] == 2008:
            s3 = s2[path[2]]
            if path[2] == 'ORG':
                return s3
            else:
                return s3[path[0]]
        else:
            s3 = s2[path[4]]
            if path[4] == 1971:
                return s3[path[0]]
            elif path[4] == 2016:
                return s3
            elif path[4] == 1967:
                return s3[path[2]]
    elif path[1] == 'NINJA':
        return s1


print(main([1971, 'ASP', 'ORG', 1972, 1967]))
print(main([1975, 'ASP', 'DYLAN', 2008, 1967]))
print(main([1975, 'ASP', 'ORG', 2008, 1967]))
print(main([1975, 'ASP', 'ORG', 1972, 2016]))