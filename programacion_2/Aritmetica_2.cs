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

        // Solicitar la operación deseada
        Console.WriteLine("Seleccione la operación a realizar:");
        Console.WriteLine("1. Suma");
        Console.WriteLine("2. Resta");
        Console.WriteLine("3. Multiplicación");
        Console.WriteLine("4. División");
        Console.Write("Ingrese el número de la operación deseada: ");

        int operacion = int.Parse(Console.ReadLine());

        double resultado;

        switch (operacion)
        {
            case 1:
                resultado = num1 + num2;
                Console.WriteLine($"El resultado de la suma es: {resultado}");
                break;

            case 2:
                resultado = num1 - num2;
                Console.WriteLine($"El resultado de la resta es: {resultado}");
                break;

            case 3:
                resultado = num1 * num2;
                Console.WriteLine($"El resultado de la multiplicación es: {resultado}");
                break;

            case 4:
                if (num2 != 0)
                {
                    resultado = num1 / num2;
                    Console.WriteLine($"El resultado de la división es: {resultado}");
                }
                else
                {
                    Console.WriteLine("No se puede dividir por cero.");
                }
                break;

            default:
                Console.WriteLine("Opción no válida.");
                break;
        }
    }
}
