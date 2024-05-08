using System;

class Program
{
    static void Main()
    {
        // Solicitar al usuario dos números
        Console.Write("Ingrese el primer número: ");
        double num1 = double.Parse(Console.ReadLine());

        Console.Write("Ingrese el segundo número: ");
        double num2 = double.Parse(Console.ReadLine());

        // Suma
        double suma = num1 + num2;
        Console.WriteLine($"La suma de {num1} y {num2} es: {suma}");

        // Resta
        double resta = num1 - num2;
        Console.WriteLine($"La resta de {num1} menos {num2} es: {resta}");

        // Multiplicación
        double multiplicacion = num1 * num2;
        Console.WriteLine($"La multiplicación de {num1} por {num2} es: {multiplicacion}");

        // División
        if (num2 != 0)
        {
            double division = num1 / num2;
            Console.WriteLine($"La división de {num1} entre {num2} es: {division}");
        }
        else
        {
            Console.WriteLine("No se puede dividir por cero.");
        }
    }
}
