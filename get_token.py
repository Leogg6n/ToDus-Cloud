import os
from todus.client import ToDusClient2

phone = os.environ["TODUS_PHONE"]
client = ToDusClient2(phone_number=phone)

# Solicitar código de verificación
client.request_code()
print("✅ Código SMS enviado, revisa tu teléfono")

# Leer el código ingresado manualmente desde la consola de GitHub Actions
pin = input("Ingresa el código de 6 dígitos del SMS: ").strip()
client.validate_code(pin)

# Imprimir el token
print("\n" + "="*50)
print("TOKEN (cópialo y guárdalo en TODUS_PASSWORD):")
print(client.password)
print("="*50)
