from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        asunto = request.POST['asunto']
        mensaje = request.POST['mensaje']

        html_dinamico = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <title>Contacto OnlyFlans - {nombre}</title>
        </head>
        <body>
        <h1>Contacto OnlyFlans</h1>
        <form action="/contacto/" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" value="{nombre}" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" value="{email}" required>
            <br>
            <label for="asunto">Asunto:</label>
            <input type="text" id="asunto" name="asunto" value="{asunto}" required>
            <br>
            <label for="mensaje">Mensaje:</label>
            <textarea id="mensaje" name="mensaje" rows="5" cols="30" required>{mensaje}</textarea>
            <br>
            <button type="submit">Enviar</button>
        </form>
        
        </body>
        </html>
        """
         # Retornar respuesta HTML
        return HttpResponse(html_dinamico, content_type="text/html")
    else:
        # Generar HTML del formulario vacío
        html_dinamico = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <title>Contacto OnlyFlans</title>
        </head>
        <body>
        <h1>Contacto OnlyFlans</h1>
        <form action="/contacto/" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <br>
            <label for="asunto">Asunto:</label>
            <input type="text" id="asunto" name="asunto" required>
            <br>
            <label for="mensaje">Mensaje:</label>
            <textarea id="mensaje" name="mensaje" rows="5" cols="30" required></textarea>
            <br>
            <button type="submit">Enviar</button>
        </form>
        
        </body>
        </html>
        """
        return HttpResponse(html_dinamico, content_type="text/html")
def home(request):
        # (Opcional): Implementa la lógica para procesar el envío del formulario
        # (guardar datos, enviar email, etc.)

        # Generar HTML con los datos del formulario
        html_dinamico = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <title>Home  HolaMundo></title>
        </head>
        <body>
        <h1>HolaMundo</h1>
        </body>
        </html>
        """
    # Retornar respuesta HTML
        return HttpResponse(html_dinamico, content_type="text/html")
def about(request):
        # (Opcional): Implementa la lógica para procesar el envío del formulario
        # (guardar datos, enviar email, etc.)

        # Generar HTML con los datos del formulario
        html_dinamico = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="UTF-8">
        <title>About  HolaMundo</title>
        </head>
        <body>
        <h1>HolaMundo</h1>
        </body>
        </html>
        """
    # Retornar respuesta HTML
        return HttpResponse(html_dinamico, content_type="text/html")


