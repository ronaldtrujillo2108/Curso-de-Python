import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime

def generate_certificates(excel_path, template_path, course_name, instructor_signature):
    """
    Genera certificados de participación personalizados a partir de un archivo Excel y una plantilla de Word.

    Args:
        excel_path (str): Ruta al archivo Excel que contiene los datos de los participantes.
        template_path (str): Ruta al documento de plantilla de Word.
        course_name (str): El nombre del curso.
        instructor_signature (str): El nombre a utilizar para la firma del instructor.
    """
    try:
        df = pd.read_excel(excel_path)
    except FileNotFoundError:
        print(f"Error: El archivo Excel no se encontró en '{excel_path}'")
        return
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return

    try:
        doc = DocxTemplate(template_path)
    except FileNotFoundError:
        print(f"Error: La plantilla de Word no se encontró en '{template_path}'")
        return
    except Exception as e:
        print(f"Error al cargar la plantilla de Word: {e}")
        return

    output_folder = "certificados_generados"
    import os
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    today_date = datetime.now().strftime("%d/%m/%Y")

    for index, row in df.iterrows():
        context = {
            'nombre_participante': row['Nombre'],
            'nombre_curso': course_name,
            'fecha_certificado': today_date,
            'firma_instructor': instructor_signature,
        }
        
        doc.render(context)
        
        output_filename = os.path.join(output_folder, f"Certificado_{row['Nombre'].replace(' ', '_')}.docx")
        doc.save(output_filename)
        print(f"Certificado generado para {row['Nombre']} en '{output_filename}'")

if __name__ == "__main__":
    excel_file = "Participantes.xlsx"
    word_template = "Certificado_Plantilla.docx"
    course = "Curso de Python Avanzado"
    instructor = "Dr. Armando Paredes"

    generate_certificates(excel_file, word_template, course, instructor)
    print("\nProceso de generación de certificados completado.")