import jane

def test_hash_file():
    assert jane.crack('hashes.txt','wordlist.txt') == {'a53f3929621dba1306f8a61588f52f55': 'edward', 'e99a18c428cb38d5f260853678922e03': 'abc123', '40be4e59b9a2a2b5dffb918c0e86b3d7': 'welcome', 'c33367701511b4f6020ec61ded352059': '654321', 'aa47f8215c6f30a0dcdb2a36a9f4168e': 'daniel', 'eb0a191797624dd3a48fa681d3061212': 'master', 'f4f068e71e0d87bf0ad51e6214ab84e9': 'angel', 'fe546279a62683de8ca334b673420696': 'samsung', 'bf779e0933a882808585d19455cd7937': 'charlie', '21b72c0b7adc5c7b4a50ffcb90d92dd6': 'matrix', 'ee7d692412c833694f6341aa54fb5ad9': 'Failed!', 'b9e851d3be78ab9ed830f47fb5dec294': 'Failed!', '9b66f29e6a3bf8f78003c3642305b7fa': 'Failed!', '7037f707e8b53a3d183c1b0b5031e7c0': 'Failed!', '74309fe83c9bc17a25ca74e69c3cf049': 'Failed!'}



