using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        List<double> valores = new List<double>();
        List<double> valoresNulos = new List<double>();

        Console.Write("Ingresa el limite superior: ");
        double limiteSuperior = Convert.ToDouble(Console.ReadLine());

        Console.Write("Ingresa el limite inferior: ");
        double limiteInferior = Convert.ToDouble(Console.ReadLine());

        if (limiteInferior < limiteSuperior)
        {
            double valorARevisar = double.PositiveInfinity;

            while (valorARevisar != 0)
            {
                Console.Write("Ingresa el valor a revisar (0 para terminar): ");
                valorARevisar = Convert.ToDouble(Console.ReadLine());

                if (valorARevisar == 0)
                    break;

                if (valorARevisar >= limiteSuperior || valorARevisar <= limiteInferior)
                {
                    valoresNulos.Add(valorARevisar);
                }
                else
                {
                    valores.Add(valorARevisar);
                }
            }

            Console.WriteLine("\nLos valores fuera de los limites: " + string.Join(", ", valoresNulos));
            Console.WriteLine("Los valores dentro de los limites: " + string.Join(", ", valores));
            Console.WriteLine("La suma de los valores dentro de los limites: " + valores.Sum());
        }
        else
        {
            Console.WriteLine("Error: El límite inferior debe ser menor que el límite superior.");
        }
    }
}
