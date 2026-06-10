#!/usr/bin/env python3
"""Generate CV PDF for Juan Pablo Castañeda Macías"""

from fpdf import FPDF

FONT_DIR = "/usr/share/fonts/noto/"

class CV(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Noto", "", FONT_DIR + "NotoSans-Regular.ttf")
        self.add_font("Noto", "B", FONT_DIR + "NotoSans-Bold.ttf")

    def section(self, title):
        self.set_font("Noto", "B", 14)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(30, 30, 30)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def body(self, text):
        self.set_font("Noto", "", 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def bullet(self, text):
        self.set_font("Noto", "", 10)
        self.set_text_color(50, 50, 50)
        self.set_x(15)
        self.multi_cell(175, 5, f"  - {text}")
        self.set_x(15)

    def project(self, name, tech, desc):
        self.set_font("Noto", "B", 11)
        self.set_text_color(30, 30, 30)
        self.cell(0, 6, name, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Noto", "", 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, tech, new_x="LMARGIN", new_y="NEXT")
        self.body(desc)
        self.ln(2)

    def entry(self, title, subtitle, bullets):
        self.set_font("Noto", "B", 11)
        self.set_text_color(30, 30, 30)
        self.cell(0, 6, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Noto", "", 10)
        self.set_text_color(80, 80, 80)
        self.cell(0, 5, subtitle, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        for b in bullets:
            self.bullet(b)
        self.ln(3)


pdf = CV()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)
pdf.add_page()

pdf.set_font("Noto", "B", 24)
pdf.set_text_color(20, 20, 20)
pdf.cell(0, 12, "Juan Pablo Castañeda Macías", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Noto", "", 13)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 7, "Ingeniería en Software - Estudiante", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(2)

pdf.set_font("Noto", "", 10)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 5, "maciasjuanpis18@gmail.com  |  github.com/JuanpaM1181", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)

# Perfil
pdf.section("Perfil")
pdf.body(
    "Estudiante de Ingeniería en Software con bases sólidas en estructuras de datos y "
    "experiencia en desarrollo backend, microservicios y videojuegos. Un año de experiencia "
    "profesional como programador en Bandprice, contribuyendo al desarrollo de 'The War in "
    "Chiapas', videojuego ganador del 1er lugar en Creativa GDL 2026 (categoría aceleración, "
    "$100,000 MXN). Enfocado en programación de UI, gestión de bases de datos, flujo de "
    "información y desarrollo de gameplay."
)

# Experiencia Laboral
pdf.section("Experiencia Laboral")
pdf.entry(
    "Programador",
    "Bandprice  |  The War in Chiapas  |  2025 - Presente (1 año)",
    [
        "Diseñé e implementé la interfaz de usuario del campamento, gestionando la base de datos interna del juego y el flujo de información entre módulos (reclutamiento, recursos, misiones)",
        "Formé parte de un equipo de 12+ personas cuyo juego ganó el 1er lugar en Creativa GDL 2026 (categoría aceleración, $100,000 MXN)",
        "El juego fue destacado en el Latin American Games Showcase 2024 y compartido por Hideo Kojima, generando cobertura en medios internacionales",
        "Contribuí a tareas de gameplay asignadas, asegurando la integración coherente entre UI, datos y mecánicas de juego",
    ]
)

# Educación
pdf.section("Educación")
pdf.set_font("Noto", "B", 11)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 6, "Ingeniería en Software", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Noto", "", 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5, "2023 - Presente", new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)

# Certificaciones
pdf.section("Certificaciones")
pdf.entry("English for IT 1", "Cisco Networking Academy - UPTapachula | Jun 2025", [])
pdf.entry("Conceptos básicos de redes", "Cisco Networking Academy | Jun 2025", [])
pdf.entry("Introducción al examen Packet Tracer", "Cisco Networking Academy | Mar 2025", [])

# Tecnologías
pdf.section("Tecnologías y Herramientas")

skills = [
    "Lenguajes: C#, JavaScript, Python, GML (Game Maker Language)",
    "Estructuras de datos: Pilas, colas, listas, árboles, grafos",
    "Backend: ASP.NET Core, Django, REST APIs, JWT",
    "Bases de datos: PostgreSQL, Entity Framework Core",
    "Infraestructura: Docker, Docker Compose, RabbitMQ",
    "Game Dev: Unity (C#), Game Maker Studio 2",
    "Herramientas: Git, Linux, Swagger/OpenAPI",
    "Documentación: Notion, Excel",
    "Datos: Procesamiento CSV",
    "Idiomas: Inglés B1 (English for IT certificate)",
]

for skill in skills:
    pdf.bullet(skill)

pdf.ln(2)

# Proyectos
pdf.section("Proyectos Destacados")

projects = [
    (
        "The War in Chiapas",
        "Game Maker Studio 2 / GML",
        "Videojuego stealth mexicano ganador del 1er lugar en Creativa GDL 2026. "
        "Programación de UI, bases de datos, flujo de información y gameplay asignado. "
        "Próximamente en Steam."
    ),
    (
        "FRIO.MX - Sistema de Microservicios",
        "C# ASP.NET Core, PostgreSQL, RabbitMQ, Docker",
        "Arquitectura de 3 microservicios (Auth, Game, Wallet) con comunicación asíncrona "
        "vía RabbitMQ, autenticación JWT, EF Core y API-first."
    ),
    (
        "LowPoly Water - Unity",
        "Unity, C#",
        "Shader/script procedural que genera agua lowpoly con vértices animados en Unity."
    ),
    (
        "dotnet-crud-api",
        "C# ASP.NET Core 9, EF Core InMemory, Swagger",
        "API REST minimalista con operaciones CRUD. Ejemplo práctico de Minimal API, "
        "Entity Framework Core y OpenAPI/Swagger."
    ),
]

for name, tech, desc in projects:
    pdf.project(name, tech, desc)

pdf.output("/home/juanpa/Projects/cv/assets/cv.pdf")
print("CV generado: assets/cv.pdf")
