import logging

key_start = '0100000000'
motd_start = '1c000000006d2ac11d806c7ed9eec97c1f00\
    ffff00fefefefefdfdfdfd12345678005d'

motd_array = [
    "MCPE",
    "IC inner - O - Powered By ...",
    "527",
    "0.8.9",
    "43",
    "2022",
    "9253910808818711583",
    "Test For IC mod in PE",
    "S",
    "1",
    "15555",
    "6661",
    ""
]


def summ_motd(data):
    logging.warning(data)
    data = ''.join(
        f'{element};'
        for element in motd_array
    )
    out = motd_start + data
    print(type(out))
    return bytes(out, encoding='utf_8')
