"""
基于
https://github.com/xBoyMinemc/dreamTool/blob/main/motd/fakeMotdpe.js
的python实现
"""

import logging

key_start = '0100000000'
motd_start = '1c000000006d2ac11d806c7ed9eec97c1f0'

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
    "19132",
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
    return bytes(out, encoding='utf_8')
