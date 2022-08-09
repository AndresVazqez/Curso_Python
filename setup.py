## Configuracion de paquetes distribuidos
## No se ha terminado de configurar debido a que el cmd no reconoce la ruta al disco d
## Si el paquete está dentro de otras carpetas se utilliza la nomenclatura del punto. Ej. paquete.otropaquete.dentrodepaquete
## Luegoi abrir cmd y ejecutar el comando python setup.py sdist.
## Para instalar el .tar generado en este ordenador o cualuiera, en la ruta del tar, ejecutar en cmd el comando pip3 install nombrePaquete.tar

from setuptools import setup

setup(
    name="paquetes",
    version="1.0",
    description="Distribucion de paquetes. Paquetes con calculos generales",
    author="Andres",
    author_email="aavsz0811@gmail.com",
    url="www.dododd.com",
    packages=["paquete", "paquete"]
)