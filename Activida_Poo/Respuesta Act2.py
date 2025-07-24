class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo  # 📝 Público
        self.autor = autor    # 👤 Público

        # 📄 Validación del número de páginas
        if numero_paginas < 10:
            print("🚨 Advertencia: El número de páginas era menor que 10. Se ajustó automáticamente a 10.")
            self.__numero_paginas = 10
        else:
            self.__numero_paginas = numero_paginas

        self.__prestado = False           # 📦 Privado, inicia en False
        self.__cantidad_prestamos = 0    # ✅ Contador de préstamos

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            self.__cantidad_prestamos += 1
            print(f"✅ El libro '{self.titulo}' ha sido prestado.")
        else:
            print("❌ El libro ya ha sido prestado.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print(f"🔄 El libro '{self.titulo}' ha sido devuelto.")
        else:
            print("⚠️ El libro no estaba prestado.")

    def mostrar_detalles(self):
        estado = "Prestado" if self.__prestado else "Disponible"
        print("📋 Detalles del libro:")
        print(f"  📖 Título: {self.titulo}")
        print(f"  👤 Autor: {self.autor}")
        print(f"  📄 Número de páginas: {self.__numero_paginas}")
        print(f"  📦 Estado: {estado}")
        print(f"  🔢 Veces prestado: {self.__cantidad_prestamos}")
