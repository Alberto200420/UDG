using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int mes = 1;
        List<double> dinero = new List<double>();

        while (mes <= 12)
        {
            Console.Write($"Ingresa el dinero que ahorraras en el mes {mes}: ");
            double ahorro = Convert.ToDouble(Console.ReadLine());

            if (ahorro <= 0)
            {
                Console.WriteLine("Invalido");
                continue;
            }

            dinero.Add(ahorro);
            mes++;
        }

        Console.WriteLine($"Esto es el total que obtendras al final del año: {dinero.Sum()}");
    }
}
