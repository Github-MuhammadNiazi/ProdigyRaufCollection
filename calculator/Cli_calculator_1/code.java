package ProdigyRaufCollection.calculator.Cli_calculator_1;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Scanner;

public class code {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int choice = 0;
        do {
            System.out.println("Press any key to exit or enter to calculate again");
            choice = System.in.read();
            double result = 0;
            if (choice == 10) {
                System.out.println("Enter number :");
                float a = sc.nextFloat();
                System.out.println("Enter another number :");
                float b = sc.nextFloat();
                System.out.println("Enter operation(+,-,*,/) :");
                char operation = sc.next().charAt(0);
                if (operation == '+' || operation == '-' || operation == '*' || (operation == '/' && b != 0)) {
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
                            result = a / b;
                            break;
                        default:
                    }
                    DecimalFormat df = new DecimalFormat("0.##");
                    System.out.println("The result is :" + df.format(result));
                } else {
                    System.out.println("Incorrect choice");
                }
            }
        } while (choice == 10);
        sc.close();
    }
}
