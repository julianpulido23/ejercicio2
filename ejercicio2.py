import tkinter as tk
from tkinter import ttk

class Curso:
    def __init__(self, nombre, profesor, horario):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []
        self.horario = horario
        self.evaluaciones = []

    def mostrar_info(self):
        info = f"Curso: {self.nombre}, Profesor: {self.profesor.nombre} {self.profesor.apellido}\n"
        info += "Estudiantes inscritos:\n"
        for estudiante in self.estudiantes:
            info += f"- {estudiante.nombre} {estudiante.apellido} (ID: {estudiante.id_estudiante})\n"
        info += self.horario.mostrar_info() + "\n"
        if self.evaluaciones:
            info += "Evaluaciones:\n"
            for evaluacion in self.evaluaciones:
                info += f"- Estudiante: {evaluacion.estudiante.nombre} {evaluacion.estudiante.apellido}, Nota: {evaluacion.nota}\n"
        return info

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        estudiante.cursos.append(self)

    def agregar_evaluacion(self, evaluacion):
        self.evaluaciones.append(evaluacion)


class Profesor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.asignaturas = []

    def mostrar_info(self):
        return f"Profesor: {self.nombre} {self.apellido}, Asignaturas: " + ", ".join([a.nombre for a in self.asignaturas])

    def cursos_dict(self):
        cursos_dict = {}
        for asignatura in self.asignaturas:
            for curso in asignatura.cursos:
                if curso.nombre not in cursos_dict:
                    cursos_dict[curso.nombre] = curso
        return cursos_dict


class Estudiante:
    def __init__(self, nombre, apellido, id_estudiante):
        self.nombre = nombre
        self.apellido = apellido
        self.id_estudiante = id_estudiante
        self.cursos = []

    def mostrar_info(self):
        return f"Estudiante: {self.nombre} {self.apellido} (ID: {self.id_estudiante}), Cursos: " + ", ".join([c.nombre for c in self.cursos])


class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.cursos = []
        profesor.asignaturas.append(self)

    def mostrar_info(self):
        return f"Asignatura: {self.nombre}, Profesor: {self.profesor.nombre} {self.profesor.apellido}"


class Evaluacion:
    def __init__(self, curso, estudiante, nota):
        self.curso = curso
        self.estudiante = estudiante
        self.nota = nota


class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def mostrar_info(self):
        return f"Horario: {self.dia} de {self.hora_inicio} a {self.hora_fin}"


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Cursos")

      
        style = ttk.Style()
        style.configure('App.TFrame', background='black')
        style.configure('App.TLabel', background='black', foreground='white')
        style.configure('App.TButton', background='black', foreground='white')
        style.configure('App.TEntry', background='black', foreground='white')
        style.configure('App.TText', background='black', foreground='white')
        style.configure('App.TCombobox', foreground='white')  

        self.create_widgets()

    def create_widgets(self):
        
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True)

        
        profesor1 = Profesor("Sebastian", "Sanchez")
        horario1 = Horario("Lunes", "08:00", "10:00")
        curso_espanol = Curso("Español", profesor1, horario1)
        curso_matematicas = Curso("Matemáticas", profesor1, horario1)

        
        estudiante1 = Estudiante("Julian", "Pulido", "001")
        estudiante2 = Estudiante("Ana", "Rodriguez", "002")
        estudiante3 = Estudiante("Carlos", "Gonzalez", "003")
        estudiante4 = Estudiante("María", "Lopez", "004")
        evaluacion1 = Evaluacion(curso_espanol, estudiante1, 5)
        evaluacion2 = Evaluacion(curso_matematicas, estudiante2, 4)
        curso_espanol.agregar_estudiante(estudiante1)
        curso_espanol.agregar_estudiante(estudiante3)
        curso_matematicas.agregar_estudiante(estudiante2)
        curso_matematicas.agregar_estudiante(estudiante4)
        curso_espanol.agregar_evaluacion(evaluacion1)
        curso_matematicas.agregar_evaluacion(evaluacion2)

        
        frame_elegir_curso = ttk.Frame(notebook, style='App.TFrame')
        notebook.add(frame_elegir_curso, text='Elegir Curso')

        ttk.Label(frame_elegir_curso, text='Elija un Curso:', style='App.TLabel').grid(row=0, column=0, padx=5, pady=5)
        self.cursos_combobox = ttk.Combobox(frame_elegir_curso, values=["Español", "Matemáticas"], style='App.TCombobox')  
        self.cursos_combobox.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(frame_elegir_curso, text='Mostrar Información', style='App.TButton', command=self.mostrar_informacion_curso).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        
        self.curso_text = tk.Text(frame_elegir_curso, wrap=tk.WORD, bg='black', fg='white', font=('Arial', 12))
        self.curso_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def mostrar_informacion_curso(self):
        nombre_curso = self.cursos_combobox.get()

        if nombre_curso == "Español":
            profesor1 = Profesor("Sebastian", "Sanchez")
            horario1 = Horario("Lunes", "08:00", "10:00")
            curso1 = Curso("Español", profesor1, horario1)
            estudiante1 = Estudiante("Julian", "Pulido", "001")
            estudiante3 = Estudiante("Carlos", "Gonzalez", "003")
            evaluacion1 = Evaluacion(curso1, estudiante1, 5)
            evaluacion3 = Evaluacion(curso1, estudiante3, 4)  
            curso1.agregar_estudiante(estudiante1)
            curso1.agregar_estudiante(estudiante3)
            curso1.agregar_evaluacion(evaluacion1)
            curso1.agregar_evaluacion(evaluacion3)

            
            self.curso_text.delete('1.0', tk.END)  
            self.curso_text.insert(tk.END, curso1.mostrar_info())

        elif nombre_curso == "Matemáticas":
            profesor2 = Profesor("Luis", "Gonzalez")
            horario2 = Horario("Martes", "10:00", "12:00")
            curso2 = Curso("Matemáticas", profesor2, horario2)
            estudiante2 = Estudiante("Ana", "Rodriguez", "002")
            estudiante4 = Estudiante("María", "Lopez", "004")
            evaluacion2 = Evaluacion(curso2, estudiante2, 4)
            evaluacion4 = Evaluacion(curso2, estudiante4, 3)  
            curso2.agregar_estudiante(estudiante2)
            curso2.agregar_estudiante(estudiante4)
            curso2.agregar_evaluacion(evaluacion2)
            curso2.agregar_evaluacion(evaluacion4)

            
            self.curso_text.delete('1.0', tk.END)  
            self.curso_text.insert(tk.END, curso2.mostrar_info())

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
