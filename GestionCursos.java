package gestioncursos;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

class Curso {
    String nombre;
    Profesor profesor;
    List<Estudiante> estudiantes;
    Horario horario;
    List<Evaluacion> evaluaciones;

    public Curso(String nombre, Profesor profesor, Horario horario) {
        this.nombre = nombre;
        this.profesor = profesor;
        this.estudiantes = new ArrayList<>();
        this.horario = horario;
        this.evaluaciones = new ArrayList<>();
    }

    public String mostrarInfo() {
        StringBuilder info = new StringBuilder("Curso: " + nombre + ", Profesor: " + profesor.nombre + " " + profesor.apellido + "\n");
        info.append("Estudiantes inscritos:\n");
        for (Estudiante estudiante : estudiantes) {
            info.append("- ").append(estudiante.nombre).append(" ").append(estudiante.apellido)
                .append(" (ID: ").append(estudiante.idEstudiante).append(")\n");
        }
        info.append(horario.mostrarInfo()).append("\n");
        if (!evaluaciones.isEmpty()) {
            info.append("Evaluaciones:\n");
            for (Evaluacion evaluacion : evaluaciones) {
                info.append("- Estudiante: ").append(evaluacion.estudiante.nombre).append(" ")
                    .append(evaluacion.estudiante.apellido).append(", Nota: ").append(evaluacion.nota).append("\n");
            }
        }
        return info.toString();
    }

    public void agregarEstudiante(Estudiante estudiante) {
        estudiantes.add(estudiante);
        estudiante.cursos.add(this);
    }

    public void agregarEvaluacion(Evaluacion evaluacion) {
        evaluaciones.add(evaluacion);
    }
}

class Profesor {
    String nombre;
    String apellido;
    List<Asignatura> asignaturas;

    public Profesor(String nombre, String apellido) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.asignaturas = new ArrayList<>();
    }
}

class Estudiante {
    String nombre;
    String apellido;
    String idEstudiante;
    List<Curso> cursos;

    public Estudiante(String nombre, String apellido, String idEstudiante) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.idEstudiante = idEstudiante;
        this.cursos = new ArrayList<>();
    }
}

class Asignatura {
    String nombre;
    Profesor profesor;
    List<Curso> cursos;

    public Asignatura(String nombre, Profesor profesor) {
        this.nombre = nombre;
        this.profesor = profesor;
        this.cursos = new ArrayList<>();
        profesor.asignaturas.add(this);
    }
}

class Evaluacion {
    Curso curso;
    Estudiante estudiante;
    int nota;

    public Evaluacion(Curso curso, Estudiante estudiante, int nota) {
        this.curso = curso;
        this.estudiante = estudiante;
        this.nota = nota;
    }
}

class Horario {
    String dia;
    String horaInicio;
    String horaFin;

    public Horario(String dia, String horaInicio, String horaFin) {
        this.dia = dia;
        this.horaInicio = horaInicio;
        this.horaFin = horaFin;
    }

    public String mostrarInfo() {
        return "Horario: " + dia + " de " + horaInicio + " a " + horaFin;
    }
}

public class GestionCursos extends JFrame {
    private JComboBox<String> cursosComboBox;
    private JTextArea cursoText;

    public GestionCursos() {
        setTitle("Gestión de Cursos");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new JPanel();
        panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));

        JLabel label = new JLabel("Elija un Curso:");
        panel.add(label);

        String[] cursos = {"Español", "Matemáticas"};
        cursosComboBox = new JComboBox<>(cursos);
        panel.add(cursosComboBox);

        JButton button = new JButton("Mostrar Información");
        button.addActionListener(e -> mostrarInformacionCurso());
        panel.add(button);

        cursoText = new JTextArea();
        cursoText.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(cursoText);
        panel.add(scrollPane);

        add(panel);
    }

    private void mostrarInformacionCurso() {
        String nombreCurso = (String) cursosComboBox.getSelectedItem();

        if ("Español".equals(nombreCurso)) {
            Profesor profesor1 = new Profesor("Sebastian", "Sanchez");
            Horario horario1 = new Horario("Lunes", "08:00", "10:00");
            Curso curso1 = new Curso("Español", profesor1, horario1);
            Estudiante estudiante1 = new Estudiante("Julian", "Pulido", "001");
            Estudiante estudiante3 = new Estudiante("Carlos", "Gonzalez", "003");
            Evaluacion evaluacion1 = new Evaluacion(curso1, estudiante1, 5);
            Evaluacion evaluacion3 = new Evaluacion(curso1, estudiante3, 4);
            curso1.agregarEstudiante(estudiante1);
            curso1.agregarEstudiante(estudiante3);
            curso1.agregarEvaluacion(evaluacion1);
            curso1.agregarEvaluacion(evaluacion3);

            cursoText.setText(curso1.mostrarInfo());
        } else if ("Matemáticas".equals(nombreCurso)) {
            Profesor profesor2 = new Profesor("Luis", "Gonzalez");
            Horario horario2 = new Horario("Martes", "10:00", "12:00");
            Curso curso2 = new Curso("Matemáticas", profesor2, horario2);
            Estudiante estudiante2 = new Estudiante("Ana", "Rodriguez", "002");
            Estudiante estudiante4 = new Estudiante("María", "Lopez", "004");
            Evaluacion evaluacion2 = new Evaluacion(curso2, estudiante2, 4);
            Evaluacion evaluacion4 = new Evaluacion(curso2, estudiante4, 3);
            curso2.agregarEstudiante(estudiante2);
            curso2.agregarEstudiante(estudiante4);
            curso2.agregarEvaluacion(evaluacion2);
            curso2.agregarEvaluacion(evaluacion4);

            cursoText.setText(curso2.mostrarInfo());
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            GestionCursos gestionCursos = new GestionCursos();
            gestionCursos.setVisible(true);
        });
    }
}