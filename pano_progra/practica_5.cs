using System;

class Program
{
    static void Main(string[] args)
    {
        // Define variables
        double a = 3;
        double b = 5;
        double c = 2;
        double d = 4;
        double x = 2.0;
        double y = 3.5;
        double z = 5.0;
        double w = 1.2;

        // Calculate each exercise
        double ejercicio1 = a * b / 2.0 + 1;
        double ejercicio2 = c / Math.Pow(x, a);
        double ejercicio3 = a / (b + c / (d + 1)) * (a + b - a) * Math.Pow(b, a) + c;
        double ejercicio4 = x / (b + c / (y + 1)) * (a + b - a) * Math.Pow(b, a) + w;
        double ejercicio5 = a + Math.Pow(b - c * (d - (a + b) * (c - c / d * a) / a + b * c) - Math.Pow(b, c), b);
        double ejercicio6 = z / x + b * w * (c - b) / a;

        // Print results
        Console.WriteLine($"Ejercicio 1: {ejercicio1}");      // Should be 8.5
        Console.WriteLine($"Ejercicio 2: {ejercicio2}");      // Should be 0.25
        Console.WriteLine($"Ejercicio 3: {ejercicio3}");      // Should be 2.0
        Console.WriteLine($"Ejercicio 4: {ejercicio4}");      // Should be 1.20
        Console.WriteLine($"Ejercicio 5: {ejercicio5}");      // Should be -79,235,165
        Console.WriteLine($"Ejercicio 6: {ejercicio6}");      // Should be -3.5
    }
}