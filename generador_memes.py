import requests



class GeneradorMemes:
    def __init__(self):
        try:
            usuario_arriba = str(input("Ingresa el texto del meme en la parte de arriba: ")).strip()
            usuario_abajo = str(input("Ingresa el texto del meme en la parte de abajo: ")).strip()
            usuario_plantilla = input("Que plantilla deseas: ")
            if not usuario_arriba or not (usuario_abajo and usuario_plantilla):
                print("Los campos no pueden estar vacios.")
                return
            self.url = f"https://api.imgflip.com/caption_image?template_id={usuario_plantilla}&username=camilobautista&password=65787929Ja&text0={usuario_arriba}&text1={usuario_abajo}"
            respuesta = requests.get(self.url)
            peticion_json = respuesta.json()
            if peticion_json["success"]:
                link_meme = peticion_json["data"]["url"]
                print(f"Meme generado y listo para su uso: {link_meme}.")
            else:
                print("Error al generar el meme:", peticion_json["error_message"])
        except Exception as error:
            print(f"Error en el programa: {error}.")


if __name__ == "__main__":
    inicio = GeneradorMemes()
