from cryptography.fernet import Fernet

def generar_clave(): return Fernet.generate_key().decode()

clave_generada = "Ki9BVUrfnXX5eHn2Pdz2cpAxR2GcHQtr4etPCJrpQPI="

def cifrar(data, clave): return Fernet(clave).encrypt(data.encode()).decode()

#print(cifrar("hola, como estás?", clave_generada))

mensaje_encrip = "gAAAAABmDgB08lKDSj0lMfLpZpz-r_v2GedFW86Xw3xgy7EOFXuXXGhORLAQEbCVo5SYBxYMmGlUQ-ITMtROi4aBe_ZtomMGqwOL-_mjAoAhV80Bh4mK2p4="

def decifrar(data, clave): return Fernet(clave).decrypt(data.encode()).decode()

print(decifrar(mensaje_encrip, clave_generada))

