#!/usr/bin/env python3
"""Generate CV PDF for Juan Pablo Castañeda Macías"""

from fpdf import FPDF

FONT_DIR = "/usr/share/fonts/noto/"

class CV(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Noto", "", FONT_DIR + "NotoSans-Regular.ttf", uni=True)
        self.add_font("Noto", "B", FONT_DIR + "NotoSans-Bold.ttf", uni=True)

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
pdf.ln(4)

pdf.set_font("Noto", "", 10)
pdf.set_text_color(60, 60, 60)
pdf.cell(0, 5, "maciasjuanpis18@gmail.com  |  github.com/JuanpaM1181", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(8)

# Perfil
pdf.section("Perfil")
pdf.body(
    "Estudiante de Ingeniería en Software con experiencia en desarrollo backend, "
    "arquitectura de microservicios y desarrollo de videojuegos. Con un año de "
    "experiencia laboral como programador en el estudio Bandprice, trabajando en "
    "el desarrollo de 'The War in Chiapas' con Game Maker Studio 2. Experiencia en "
    "trabajo en equipo, documentación con Notion, procesamiento de datos (CSV) y "
    "Excel. Apasionado por el código limpio, las buenas prácticas y las "
    "tecnologías modernas."
)

# Experiencia Laboral
pdf.section("Experiencia Laboral")
pdf.set_font("Noto", "B", 11)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 6, "Programador - Bandprice", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Noto", "", 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5, "The War in Chiapas | 1 año | Game Maker Studio 2 / GML", new_x="LMARGIN", new_y="NEXT")
pdf.body(
    "Programación de UI, gestión de bases de datos, flujo de información "
    "y tareas asignadas de gameplay en Game Maker Studio 2."
)

# Educación
pdf.section("Educación")
pdf.set_font("Noto", "B", 11)
pdf.set_text_color(30, 30, 30)
pdf.cell(0, 6, "Ingeniería en Software", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Noto", "", 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 5, "En curso", new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)

# Tecnologías
pdf.section("Tecnologías y Herramientas")

skills = [
    "Lenguajes: C#, JavaScript, Python, GML (Game Maker Language)",
    "Backend: ASP.NET Core, Django, REST APIs, JWT",
    "Bases de datos: PostgreSQL, Entity Framework Core",
    "Infraestructura: Docker, Docker Compose, RabbitMQ",
    "Game Dev: Unity (C#), Game Maker Studio 2",
    "Herramientas: Git, Linux (Arch/Hyprland), Swagger/OpenAPI",
    "Documentación: Notion, Excel",
    "Datos: Procesamiento CSV",
    "Soft skills: Trabajo en equipo, comunicación técnica",
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
        "Videojuego stealth mexicano en pixel art. Desarrollo de mecánicas de sigilo, "
        "IA enemiga, gestión de recursos y sistema de misiones. Próximamente en Steam."
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
        "SumoBall - Juego 3D",
        "Unity, C#",
        "Juego 3D de supervivencia por oleadas con powerups y físicas."
    ),
    (
        "Re-Code",
        "Game Maker Language",
        "Videojuego integrador con diseño de niveles, físicas y gameplay en Game Maker."
    ),
    (
        "dotnet-crud-api",
        "C# ASP.NET Core 9, EF Core InMemory, Swagger",
        "API REST minimalista con operaciones CRUD para colección de videojuegos. "
        "Ejemplo práctico de Minimal API, Entity Framework Core y OpenAPI/Swagger."
    ),
]

for name, tech, desc in projects:
    pdf.project(name, tech, desc)

# Idiomas
pdf.section("Idiomas")
pdf.body("Español")
pdf.body("Inglés")

pdf.output("/home/juanpa/Projects/cv/assets/cv.pdf")
print("CV generado: assets/cv.pdf")
