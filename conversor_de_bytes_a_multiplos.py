#convierte bytes a X multiplo, Kb, Mb, Gb, Tb

def bytes_a_multiplo(b):
    if b < 1024: return f"{b} B"
    if b < 1024**2: return f"{b/1024:.{2}f} KB"
    if b < 1024**3: return f"{b/1024**2:.{2}f} MB"
    if b < 1024**4: return f"{b/1024**3:.{2}f} GB"
    if b < 1024**5: return f"{b/1024**4:.{2}f} TB"

import time
for x in range(22):
    print(bytes_a_multiplo(5**x))
    time.sleep(1)
