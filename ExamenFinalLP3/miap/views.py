from django.shortcuts import render, HttpResponse, redirect


# Create your views here.


layout = """
    <h1> Examen Final LP3 | Emily Cañazaca </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Personas</a>
        </li>

    </ul>
    <hr/>
"""


def index(request):
    mensaje="""
        <h1>Inicio</h1>
    """
    return HttpResponse(layout + mensaje)


