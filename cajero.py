#---SECCION: ENTRADA---

tipoMoneda = int(input("""Tipo de moneda (1: Bs, 2 : $)"""))
monto = int(input("""Monto a retirar : """))
tipoCuenta = int(input("""Tipo de cuenta(1 Ahorro, 2 Corriente)"""))

#---SECCION: VALIDACIONES---

if monto % 10 !=0:
    print(f"""Error: Monto no compatible con denominaciones disponibles""")
    exit()
    
elif tipoMoneda == 1 and monto > 10000:
    print("""Transaccion denegada: Excede limite diario""")
    exit()
    
elif tipoMoneda == 2 and monto > 500:
    print("""Transaccion denegada: Excede limite diario""")
    exit()
    
#---SECCION: COMISION---

comision = 0
if tipoCuenta == 2:
    comision = monto * 0.05

totalDebitar = monto + comision

#---SECCION: DESGlOSE (DIV y MOD)---

cant_100 = monto // 100
resto1 = monto % 100

cant_50 = resto1 // 50
resto2 = resto1 % 50

cant_20 = resto2 // 20
resto3 = resto2 % 20

cant_10 = resto3  // 10

#---SECCION:SIMBOLOS Y SALIDAD---:)

match tipoMoneda:
    case 1:
        simbolo = "Bs."
        print(f"""Retiro en Bolivares""")
    case 2:
        simbolo = "$"
        print(f"""Retiro en Dolares""")


print(f"""Billtes de 100: {cant_100}""")
print(f"""Billetes de 50: {cant_50}""")
print(f"""Billetes de 20: {cant_20}""")
print(f"""Billetes de 10: {cant_10}""")

print(f"""Total debitado: {totalDebitar} {simbolo}""")

