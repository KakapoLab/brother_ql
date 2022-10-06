#!/usr/bin/python3
import urllib.parse
import urllib.request
import os
import platform

# Iron on
TEST_URL = "brotherprinter:name=Iron%20on%20labelfront&quantity=Default Title&url=https%3A%2F%2Fpingpenguinshopifyapp-orderdatabucket-1p52pbqdzvzuy.s3.eu-west-1.amazonaws.com%2Fpingpenguinuk.myshopify.com%2FOrder4901371379959%2Fline_items%2F12448607895799-Iron%2520on%2520label-Front.png%3FAWSAccessKeyId%3DASIAWGNPJXHH7IL24BVD%26Expires%3D1665074072%26Signature%3D2JP6mHRM%252BGh%252FWwz72SPTkHvbIiY%253D%26x-amz-security-token%3DIQoJb3JpZ2luX2VjECEaCWV1LXdlc3QtMSJIMEYCIQD7lmfskv3VO781%252B8ixZBQMxf17mj01LWZuveAQgyV4HAIhANHxgt7bmrsWZeyxawIKlepy6UTborgBO61HxVgvzCukKsQDCNr%252F%252F%252F%252F%252F%252F%252F%252F%252F%252FwEQARoMNDI2MTA2MjcyMjA3IgwYv75taexA0vGnRv4qmANJTlLmsapUYHmgm3avHl91%252FFSkbPMxWR52Lk1lpFUXLYdwEaSn%252B5wm3%252FWzFxNkxTeQmX0%252F140dbDaEcs7KhoUvKnOyjGEVGVRNl%252BNjXTCQ5Kh87RbyWvuj%252FXiiskBei%252B97xP%252BMbYmy4b0BFGWRb0N5coZWthp6ZVCF%252F2uHdZ8aZcN7RggslWLg%252F1%252Fwdu0OkWjDSILtEWJgOojjw8hTIAlyI5G2%252BiaRDDZgo0RDTLRdUFFNVkdnuI5jcdTbHx0ZHPs2OOrK8hhlsWe7QhOhI87m6Z2AGXjg6mDGnd%252FuFL5DYfyGUglPyby8B2b4rs97Iqid26ZSPX0WJtbFUMEFeLcYcDdemI91XzAV%252Fpxq0fLiQE8R4amABc6oLk85U45nDUjpFysw7feLutwADJItcWIqiA8Hm2TrBkxEs4SaOj0vyqCPrd3wTC0dY5rY8Z%252B3vPqzKwIxRl%252BcKeYSTLuaJjMdotAyhzx2DgATLWOTDF6%252BZYgGl5HHmSXx0NYTLsOfdGNVW6b6oe8aCbMZiAagqruuWkpk%252BR7LbmIw5%252BD2mQY6nQEZfyBAw%252FaF7UBHrP5AxnbRtFe8weFKnIpbsBGWjhIYaztp54cxlrvgXiaQBpfXtWUJ5zq9yNcBmoXwIHHk2CPBb9Sz5m44D0UBS9ujKZ1sN1lJ%252BhZNywDY8pbE22Oo8YPGt9XDQzw4T5f11KoxGcZhCUAzvSbTxfNSOiZ%252F84LLz3BbU8odBzbfukuqaa4VjoDRCSe4cP%252B%252Bnayjf0Dq"
# Sticker
#TEST_URL = "brotherprinter:name=Small%20washable%20stickerfront&quantity=6&url=https%3A%2F%2Fpingpenguinshopifyapp-orderdatabucket-1p52pbqdzvzuy.s3.eu-west-1.amazonaws.com%2Fpingpenguinuk.myshopify.com%2FOrder4901371379959%2Fline_items%2F12448607928567-Small%2520washable%2520sticker-Front.png%3FAWSAccessKeyId%3DASIAWGNPJXHHZSFE335X%26Expires%3D1665065999%26Signature%3DUQe9gow32huwhxHsABvxNPRdoVo%253D%26x-amz-security-token%3DIQoJb3JpZ2luX2VjEB8aCWV1LXdlc3QtMSJGMEQCIA9EbjapFDFzFepQmt92VYaqCmxYHl8cfNPFuyENALNNAiBx5hnsHT2zGr33rGpNZ0%252FrldV7yMYOZLuu%252BYuCLPTFCCrEAwjX%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAEaDDQyNjEwNjI3MjIwNyIMUJkqE5LOPWreedcKKpgDbs%252FBS27jOiDgFEX26tBkyywrqRIJ9ClEALok3TXuhNhg1DPo%252BLCn5%252BQJQRglswvGSuCNi96SjBIdyI9R4maMpB4JJlpwdajD1C0FpfwKScl3LmiA7SDwxOQJzySEEJ1n7Ff73x25ui2VM8gWvGkOW4%252FPGRUSgOPIQoRpj%252FSie31s9GU7B7rC%252FDEOLiin4kJ0E53oMxS2q7aziq2zGqXcl2GMcXvLmbXqswRqr2LbEYg2Dfx50S7XSdB0vxk3yPhSiX5JcIbW1%252B0oM6LTmL0yCPTnI7FsaA2sCqmyBFb5VeFAxEbWD%252BJCNfcrNond3IiKtUKJEWF2OcrV0PeYva8g0aZZ1J1yJaoZ6rjFjf1jWQFaMgQE7RmY2YrS7C%252B%252FgQQcT51sznHZfH9m82bfFxpj%252FMy8A2OeYE9GJE2ebqr%252FaxXpVdWoDLYCY652vYkzWJBtU5Gojcspx6j2dvXbqwHm%252BwSGSnOHC861iwPOYDnX2QnuUBunCNWqkD2UOWsy275sH%252Fr0U7Fi53g%252BQrROxvX3%252FJBrzCuB5552MI2l9pkGOp8BZaS2CmHNDVtUOCjQl%252Fz0aQcFmnpavC6kCcTnpqD%252BJ9N8aqAaficfvs4AORmHklYweHkEwS5TB0bEkmJPkdnLJLVd3bbKd0v38GimTTkELNaIpsZ5HVsoQ%252BbTjyQiUa2Gh7QumbycFh7B6gSeS1HaHmBk2SZ839gIhvjtOTdFR5XK8aqCrMU7e7uDlCOj%252BSyv82GW1RNM2DhjZcUC7PRR"
labelSize = 'pt18'

protocol=''
parameters = ''
[protocol,parameters] = TEST_URL.split(':',1)
splitParameters = parameters.split('&')
options = {}
for parameterPair in splitParameters:
    [optionName,optionValue] = parameterPair.split('=')
    options[optionName] = optionValue


decodedUrl = urllib.parse.unquote(options['url'])
tempFilename = './thingsToPrint/' + options['name'] + '.png'

urllib.request.urlretrieve(decodedUrl, './thingsToPrint/' + options['name'] + '.png')

commandString = 'python3 ./brother_ql/cli.py '

if platform.system() == 'Darwin' : 
    commandString +=  "-b network -m PT-P900W -p tcp://192.168.86.52 print -c --no-cut -l " + labelSize 
else :
    commandString +=  "-b linux_kernel -m PT-P900W  -p /dev/usb/lp1 print -c --no-cut -l " + labelSize 

quantityToPrint = 1 
if options['quantity'].isnumeric():   
    quantityToPrint = int(options['quantity'])

for _ in range(quantityToPrint): 
    commandString += ' ' + tempFilename

print("executing command "+ commandString)
stream = os.popen(commandString)
output = stream.read()
print(output)

