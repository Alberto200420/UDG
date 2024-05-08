using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ingrese la edad de la persona para determinar si es mayor de edad:");

        // Leer la edad del teclado
        Console.Write("Ingrese la edad: ");
        int edad = int.Parse(Console.ReadLine());

        // Determinar si es mayor de edad
        if (edad >= 18)
        {
            Console.WriteLine("La persona es mayor de edad.");
        }
        else
        {
            Console.WriteLine("La persona es menor de edad.");
        }
    }
}
