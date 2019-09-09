import zlib
import tarfile
import io
import xml.etree.ElementTree
import json
import base64
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("archive")
args = arg_parser.parse_args()
with open(args.archive, 'rb') as f:
    f.seek(24)
    data = f.read()

tarstream = zlib.decompress(data)
tf = tarfile.open(fileobj=io.BytesIO(tarstream))
extracted = tf.extractfile('apps/org.fedorahosted.freeotp/sp/tokens.xml')

xmltree = xml.etree.ElementTree.parse(extracted)

for token in xmltree.findall('string'):
    name = token.get("name")
    token = json.loads(token.text)
    if not isinstance(token, dict):
        continue
    secret = base64.b32encode(
        bytes((x + 256) & 255 for x in token["secret"])).decode()

    label = token["label"]
    issuerExt = token["issuerExt"]
    params = {'secret': secret,
              'algorithm': token["algo"],
              'digits': token["digits"],
              'period': token["period"],
              'counter': token["counter"],
              'issuer': token["issuerInt"]
              }
    paramsStr = '&'.join([f'{k}={v}' for (k, v) in params.items()])
    url = f'otpauth://totp/{issuerExt}:{label}?{paramsStr}'

    try:
        import pyqrcode
        code = pyqrcode.create(url)
        code.svg(f'{issuerExt}-{label}.svg', scale=8)
    except ImportError:
        print(url)