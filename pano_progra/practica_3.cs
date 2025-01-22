using System;
using System.Collections.Generic;

class Program
{
    static List<string> dias = new List<string> { "Lunes", "Martes", "Miércoles", "Jueves", "Viernes" };
    static Dictionary<string, Dictionary<string, double>> datos = new Dictionary<string, Dictionary<string, double>>();

    static Dictionary<string, double> ObtenerValores(string nombre)
    {
        var valores = new Dictionary<string, double>();
        Console.WriteLine($"\nIngrese los valores para {nombre}:");
        foreach (string dia in dias)
        {
            double valor;
            while (true)
            {
                Console.Write($"{dia}: ");
                if (double.TryParse(Console.ReadLine(), out valor))
                {
                    valores[dia] = valor;
                    break;
                }
                else
                {
                    Console.WriteLine("Por favor, ingrese un número válido.");
                }
            }
        }
        return valores;
    }

    static (string, string, double) EncontrarMaximo(Dictionary<string, Dictionary<string, double>> datos)
    {
        double maxValor = double.NegativeInfinity;
        string maxNombre = "";
        string maxDia = "";

        foreach (var persona in datos)
        {
            foreach (var dia in persona.Value)
            {
                if (dia.Value > maxValor)
                {
                    maxValor = dia.Value;
                    maxNombre = persona.Key;
                    maxDia = dia.Key;
                }
            }
        }

        return (maxNombre, maxDia, maxValor);
    }

    static void Main(string[] args)
    {
        for (int i = 0; i < 5; i++)
        {
            Console.Write($"\nIngrese el nombre de la persona {i + 1}: ");
            string nombre = Console.ReadLine();
            datos[nombre] = ObtenerValores(nombre);
        }

        var (nombreMax, diaMax, valorMax) = EncontrarMaximo(datos);

        Console.WriteLine("\n=== Resultado ===");
        Console.WriteLine($"El valor más alto es: {valorMax}");
        Console.WriteLine($"Corresponde a: {nombreMax}");
        Console.WriteLine($"En el día: {diaMax}");
    }
}
