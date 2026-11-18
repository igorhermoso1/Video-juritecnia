"""Mueve el índice de un MP4 (caja «moov») al principio del archivo para que el video
empiece a reproducirse en cuanto llega el primer trozo. No recomprime: la imagen y el
sonido quedan idénticos. Es lo mismo que «ffmpeg -c copy -movflags +faststart».

Uso:  python faststart.py entrada.mp4 salida.mp4
"""
import os, struct, sys

CONTENEDORES = {b'moov', b'trak', b'mdia', b'minf', b'stbl', b'edts', b'udta'}

def cajas(f, ini, fin):
    """Recorre las cajas entre ini y fin: devuelve (tipo, inicio, tamaño, cabecera)."""
    pos = ini
    while pos + 8 <= fin:
        f.seek(pos)
        tam, tipo = struct.unpack('>I4s', f.read(8)); cab = 8
        if tam == 1: tam = struct.unpack('>Q', f.read(8))[0]; cab = 16
        elif tam == 0: tam = fin - pos
        if tam < cab: raise ValueError(f'caja rota en {pos}')
        yield tipo, pos, tam, cab
        pos += tam

def parchear(moov, desplaza):
    """Suma «desplaza» a cada posición de trozo (stco 32 bits, co64 64 bits) dentro de moov."""
    def rec(ini, fin):
        pos = ini
        while pos + 8 <= fin:
            tam, tipo = struct.unpack('>I4s', moov[pos:pos+8]); cab = 8
            if tam == 1: tam = struct.unpack('>Q', moov[pos+8:pos+16])[0]; cab = 16
            if tipo in CONTENEDORES: rec(pos + cab, pos + tam)
            elif tipo in (b'stco', b'co64'):
                n = struct.unpack('>I', moov[pos+cab+4:pos+cab+8])[0]
                fmt, ancho = ('>I', 4) if tipo == b'stco' else ('>Q', 8)
                p = pos + cab + 8
                for _ in range(n):
                    v = struct.unpack(fmt, moov[p:p+ancho])[0] + desplaza
                    # shortcut: no convierte stco a co64; basta para archivos de menos de 4 GB
                    if tipo == b'stco' and v >= 2**32: raise ValueError('archivo de más de 4 GB: usa ffmpeg')
                    moov[p:p+ancho] = struct.pack(fmt, v); p += ancho
            pos += tam
    rec(8, len(moov))

def primeros_trozos(moov, n=5):
    """Primeras posiciones de trozo de cada pista (para la comprobación final)."""
    out = []
    i = 0
    while (i := moov.find(b'stco', i + 1)) != -1:
        cnt = struct.unpack('>I', moov[i+8:i+12])[0]
        out += [struct.unpack('>I', moov[i+12+4*k:i+16+4*k])[0] for k in range(min(n, cnt))]
    i = 0
    while (i := moov.find(b'co64', i + 1)) != -1:
        cnt = struct.unpack('>I', moov[i+8:i+12])[0]
        out += [struct.unpack('>Q', moov[i+12+8*k:i+20+8*k])[0] for k in range(min(n, cnt))]
    return out

def faststart(entrada, salida):
    tam_total = os.path.getsize(entrada)
    with open(entrada, 'rb') as f:
        lista = list(cajas(f, 0, tam_total))
        tipos = [c[0] for c in lista]
        if b'moov' not in tipos or b'mdat' not in tipos: raise ValueError('no parece un MP4')
        if tipos.index(b'moov') < tipos.index(b'mdat'):
            print(f'{entrada}: ya tenía el índice al principio, no hace falta tocarlo'); return False
        _, mpos, mtam, _ = lista[tipos.index(b'moov')]
        f.seek(mpos); moov = bytearray(f.read(mtam))
        viejos = primeros_trozos(moov)
        parchear(moov, mtam)
        with open(salida, 'wb') as g:
            escrito = False
            for tipo, pos, tam, _ in lista:
                if tipo == b'moov': continue
                if tipo == b'mdat' and not escrito: g.write(moov); escrito = True
                f.seek(pos); quedan = tam
                while quedan:
                    trozo = f.read(min(quedan, 8 << 20)); g.write(trozo); quedan -= len(trozo)
    # comprobación: los primeros trozos de cada pista apuntan a los mismos bytes que antes
    with open(entrada, 'rb') as a, open(salida, 'rb') as b:
        assert os.path.getsize(salida) == tam_total, 'el tamaño ha cambiado'
        nuevos = primeros_trozos(bytearray(moov))
        for v, n in zip(viejos, nuevos):
            a.seek(v); b.seek(n)
            assert a.read(64) == b.read(64), 'los datos no cuadran tras mover el índice'
        tipos_out = [c[0] for c in cajas(b, 0, tam_total)]
        assert tipos_out.index(b'moov') < tipos_out.index(b'mdat'), 'el índice no quedó delante'
    print(f'{salida}: listo, índice de {mtam/1e6:.1f} MB movido al principio')
    return True

if __name__ == '__main__':
    if len(sys.argv) != 3: sys.exit(__doc__)
    faststart(sys.argv[1], sys.argv[2])
