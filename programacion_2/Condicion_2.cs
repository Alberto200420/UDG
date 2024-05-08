using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Ingrese tres números enteros para comparar:");

        // Leer tres números del teclado
        Console.Write("Ingrese el primer número: ");
        int num1 = int.Parse(Console.ReadLine());

        Console.Write("Ingrese el segundo número: ");
        int num2 = int.Parse(Console.ReadLine());

        Console.Write("Ingrese el tercer número: ");
        int num3 = int.Parse(Console.ReadLine());

        // Determinar el mayor, el medio y el menor
        int mayor = Math.Max(Math.Max(num1, num2), num3);
        int menor = Math.Min(Math.Min(num1, num2), num3);
        int medio = num1 + num2 + num3 - mayor - menor;

        // Imprimir el resultado
        Console.WriteLine($"El mayor número es: {mayor}");
        Console.WriteLine($"El número intermedio es: {medio}");
        Console.WriteLine($"El menor número es: {menor}");
    }
}
