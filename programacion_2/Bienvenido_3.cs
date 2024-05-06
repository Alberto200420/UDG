using System;

class Program
{
    static void Main()
    {
        string header = "Bienvenidos";
        string subtitle = "Videojuegos";

        // Impresión en dos líneas con formato
        Console.WriteLine("{0,-15} {1,-15}", header, subtitle);
        Console.WriteLine("================================");

        // Impresión de texto adicional con formato
        Console.WriteLine("{0,-15} {1,-15}", "Curso", "Nivel Básico");
        Console.WriteLine("{0,-15} {1,-15}", "Duración", "10 semanas");
        Console.WriteLine("{0,-15} {1,-15}", "Horario", "Martes y Jueves");
    }
}
