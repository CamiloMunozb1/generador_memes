import requests

class GeneradorMemes:
    def __init__(self):
        try:
            # Solicita al usuario los textos y la plantilla para el meme
            self.usuario_arriba = str(input("Ingresa el texto del meme en la parte de arriba: ")).strip()
            self.usuario_abajo = str(input("Ingresa el texto del meme en la parte de abajo: ")).strip()
            self.usuario_plantilla = input("Que plantilla deseas: ")
            
            # Verifica que los campos no estén vacíos
            if not self.usuario_arriba or not (self.usuario_abajo and self.usuario_plantilla):
                print("Los campos no pueden estar vacíos.")
                return
            
            # Inicializa variables necesarias para la búsqueda de la plantilla
            self.id_usuario = None
            self.url_busqueda = "https://api.imgflip.com/get_memes"

        except ValueError:
            print("Error de digitación, volver a intentar.")
        except Exception as error:
            print(f"Error en el programa: {error}.")

    def buscar_plantilla(self):
        try:
            # Realiza una petición a la API para obtener la lista de plantillas de memes disponibles
            respuesta_primaria = requests.get(self.url_busqueda)
            peticion_json = respuesta_primaria.json()

            if peticion_json["success"]:
                plantilla_id = peticion_json["data"]["memes"]
                
                # Busca la plantilla ingresada por el usuario ignorando mayúsculas y minúsculas
                for meme in plantilla_id:
                    if meme["name"].lower() == self.usuario_plantilla.lower():
                        self.id_usuario = meme["id"]
                        return True
            
            print("Plantilla no encontrada")
            return False
        
        except Exception as error:
            print(f"Error en el programa: {error}.")
    
    def generar_meme(self):
        try:
            # Construye la URL para generar el meme con la plantilla seleccionada y los textos proporcionados
            url = f"https://api.imgflip.com/caption_image?template_id={self.id_usuario}&username=YOUR_USERNAME&password=YOUR_PASSWORD&text0={self.usuario_arriba}&text1={self.usuario_abajo}"
            respuesta = requests.get(url)
            peticion_json = respuesta.json()

            if peticion_json["success"]:
                print(f"Meme generado y listo para su uso: {peticion_json['data']['url']}")
            else:
                print("Error al generar el meme:", peticion_json["error_message"])
                
        except Exception as error:
            print(f"Error en el programa: {error}.")

if __name__ == "__main__":
    inicio = GeneradorMemes()
    if inicio.buscar_plantilla():
        inicio.generar_meme()
