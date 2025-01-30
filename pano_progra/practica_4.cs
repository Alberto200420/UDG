using System;
using System.Collections.Generic;

class Program
{
    static void CalcularAhorro(int tiempoMeses, double restriccion)
    {
        HashSet<double> ahorroDiario = new HashSet<double>();
        int totalDias = tiempoMeses * 30;
        double totalAhorro = 0;

        for (int dia = 1; dia <= totalDias; dia++)
        {
            double cantidad;
            while (true)
            {
                Console.Write($"Día {dia}: ¿Cuánto ahorrarás hoy? ");
                if (double.TryParse(Console.ReadLine(), out cantidad) && !ahorroDiario.Contains(cantidad))
                {
                    ahorroDiario.Add(cantidad);
                    break;
                }
                else
                {
                    Console.WriteLine("Cantidad inválida o ya registrada, intenta nuevamente.");
                }
            }

            totalAhorro += cantidad;
            Console.WriteLine($"Día {dia}: Ahorro diario = ${cantidad}, Acumulado = ${totalAhorro:F2}");

            if (totalAhorro > restriccion)
            {
                Console.WriteLine("Restricción superada.");
                totalAhorro += totalAhorro * 0.046;
                Console.WriteLine($"Se agrega un 4.6% adicional. Nuevo total = ${totalAhorro:F2}");
                break;
            }
        }

        Console.WriteLine("\nResumen:");
        Console.WriteLine($"Ahorro total: ${totalAhorro:F2}");
        Console.WriteLine($"Restricción inicial: ${restriccion:F2}");
    }

    static void Main()
    {
        Console.Write("Ingrese el tiempo total de ahorro en meses: ");
        int tiempoMeses = int.Parse(Console.ReadLine());

        Console.Write("Ingrese el monto de restricción: ");
        double restriccion = double.Parse(Console.ReadLine());

        CalcularAhorro(tiempoMeses, restriccion);
    }
}
