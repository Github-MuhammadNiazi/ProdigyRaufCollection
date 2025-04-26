package ProdigyRaufCollection.calculator.Cli_calculator_1;

import java.text.DecimalFormat;
import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your choice....\n1.Enter\n2.Exit");
        int choice = sc.nextInt();
        do {
            double result = 0;
            if (choice == 1) {
                System.out.println("Enter number :");
                float a = sc.nextFloat();
                System.out.println("Enter another number :");
                float b = sc.nextFloat();
                System.out.println("Enter operation(+,-,*,/) :");
                char operation = sc.next().charAt(0);
                switch (operation) {
                    case '+':
                        result = a + b;
                        break;
                    case '-':
                        result = a - b;
                        break;
                    case '*':
                        result = a * b;
                        break;
                    case '/':
                        if (b != 0) {
                            result = a / b;
                        } else if (b == 0) {
                            System.out.println("Can't divide by zero");
                        }
                        break;
                    default:
                        System.out.println("Incorrect choice");
                }
                DecimalFormat df = new DecimalFormat("0.####");
                System.out.println("The result is :" + df.format(result));
                System.out.println("Enter your choice....\n1.Enter\n2.Exit");
                choice = sc.nextInt();
            }
        } while (choice != 2);
        if (choice == 2) {
            System.out.println("Thanks for using our calculator system");
        }
        sc.close();
    }
}
