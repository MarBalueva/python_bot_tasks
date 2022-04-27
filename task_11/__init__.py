import struct

def create_d_structures(data, address):
    result = []
    for d_address in struct.unpack('>4I', data[address:address + 16]):
        d1 = struct.unpack('>Q', data[d_address:d_address + 8])[0]
        d2 = list(struct.unpack('>3B', data[d_address + 8:d_address + 11]))

        result.append({
            'D1': d1,
            'D2': d2
        })
    return result


def main(data):
    a1 =
    a2 = struct.unpack('>2s', data[26:28])[0].decode('ascii')
    a3 = struct.unpack('>H', data[28:30])[0]
    a4 = create_d_structures(data, 32)

    b1 = struct.unpack('>Q', data[4:12])[0]
    b2 = struct.unpack('>H', data[12:14])[0]
    b3 = struct.unpack('>I', data[14:18])[0]
    b4 = struct.unpack('>q', data[18:26])[0]

    c1 = struct.unpack('>H', data[b2:b2 + 2])[0]
    c2 = struct.unpack('>I', data[b2 + 2:b2 + 6])[0]
    c3 = struct.unpack('>2s', data[b2 + 6:b2 + 8])[0].decode('ascii')

    out_dict = {
        'A1': a1
        'A2': {
            'B1': b1,
            'B2': b2,
            'B3': b3,
            'B4': b4,
            'B5': {
                'C1': c1,
                'C2': c2,
                'C3': c3
            }
        },
        'A3': a3,
        'A4': a4
    }
    return out_dict

print (main(b'3CQCW\x02\x00m\x00\x00\x00|\x00\xb1\xdb\xe0\xf2\x1f\xaaU\x14\x9fN\x98'
 b'U\xce\xd5\x02\x00\x88\x00\xa3\xbd& \xc3\x90\x9d\x08\x00\x8a\x00W\xf6d\x1d2}'
 b';\x08\x00\x92\x00\x90\x95VZ\x08D\xa8\x02\x00\x9a\x00Z\x1d#_zh\xd3\x04'
 b'\x00\x9c\x00\xf9\n\xaa\xda\xea\x8b\xc7\x02\x00\xa0\x00h\xf1\x10\x94\x8a+'
 b'\xcf\x03\x00\xa2\x00\xf5n\x86\xb3.\x0f\xb7\x08\x00\xa5\x006qag\x8c\x94\x93I'
 b'!-L\xbe\xdc\x0cu\xceerwwH\x92\xd5\x94C:o\x00\r]B\xbc\xff"K\x85\x9a\xd5S '
 b'jM*\xbb\x16\x1e\x8e\x86#\xfd\x80V\x05\x06x\\\x11k\xa3\x92\x92\xd0\xf7NF'))
