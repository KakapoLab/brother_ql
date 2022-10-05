#!/usr/bin/python3
import urllib.parse
import urllib.request
import os


TEST_URL = "brotherprinter:name=Iron%20on%20labelfront&quantity=Default Title&url=https%3A%2F%2Fpingpenguinshopifyapp-orderdatabucket-1p52pbqdzvzuy.s3.eu-west-1.amazonaws.com%2Fpingpenguinuk.myshopify.com%2FOrder4901371379959%2Fline_items%2F12448607895799-Iron%2520on%2520label-Front.png%3FAWSAccessKeyId%3DASIAWGNPJXHHZSFE335X%26Expires%3D1665065999%26Signature%3DdZ%252Bmj0NLILGPm8Qk4aSh6h2CRUw%253D%26x-amz-security-token%3DIQoJb3JpZ2luX2VjEB8aCWV1LXdlc3QtMSJGMEQCIA9EbjapFDFzFepQmt92VYaqCmxYHl8cfNPFuyENALNNAiBx5hnsHT2zGr33rGpNZ0%252FrldV7yMYOZLuu%252BYuCLPTFCCrEAwjX%252F%252F%252F%252F%252F%252F%252F%252F%252F%252F8BEAEaDDQyNjEwNjI3MjIwNyIMUJkqE5LOPWreedcKKpgDbs%252FBS27jOiDgFEX26tBkyywrqRIJ9ClEALok3TXuhNhg1DPo%252BLCn5%252BQJQRglswvGSuCNi96SjBIdyI9R4maMpB4JJlpwdajD1C0FpfwKScl3LmiA7SDwxOQJzySEEJ1n7Ff73x25ui2VM8gWvGkOW4%252FPGRUSgOPIQoRpj%252FSie31s9GU7B7rC%252FDEOLiin4kJ0E53oMxS2q7aziq2zGqXcl2GMcXvLmbXqswRqr2LbEYg2Dfx50S7XSdB0vxk3yPhSiX5JcIbW1%252B0oM6LTmL0yCPTnI7FsaA2sCqmyBFb5VeFAxEbWD%252BJCNfcrNond3IiKtUKJEWF2OcrV0PeYva8g0aZZ1J1yJaoZ6rjFjf1jWQFaMgQE7RmY2YrS7C%252B%252FgQQcT51sznHZfH9m82bfFxpj%252FMy8A2OeYE9GJE2ebqr%252FaxXpVdWoDLYCY652vYkzWJBtU5Gojcspx6j2dvXbqwHm%252BwSGSnOHC861iwPOYDnX2QnuUBunCNWqkD2UOWsy275sH%252Fr0U7Fi53g%252BQrROxvX3%252FJBrzCuB5552MI2l9pkGOp8BZaS2CmHNDVtUOCjQl%252Fz0aQcFmnpavC6kCcTnpqD%252BJ9N8aqAaficfvs4AORmHklYweHkEwS5TB0bEkmJPkdnLJLVd3bbKd0v38GimTTkELNaIpsZ5HVsoQ%252BbTjyQiUa2Gh7QumbycFh7B6gSeS1HaHmBk2SZ839gIhvjtOTdFR5XK8aqCrMU7e7uDlCOj%252BSyv82GW1RNM2DhjZcUC7PRR"


protocol=''
parameters = ''
[protocol,parameters] = TEST_URL.split(':',1)
splitParameters = parameters.split('&')
options = {}
for parameterPair in splitParameters:
    [optionName,optionValue] = parameterPair.split('=')
    options[optionName] = optionValue


decodedUrl = urllib.parse.unquote(options['url'])

urllib.request.urlretrieve(decodedUrl, './thingsToPrint/' + options['name'] + '.png')


stream = os.popen('python3 ./cli.py')
output = stream.read()
print(output)

