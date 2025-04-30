package ProdigyRaufCollection.calculator.cli_calculator_2;

import java.io.IOException;
import java.text.DecimalFormat;
import java.util.Scanner;

public class PracFinal {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int choice = 10;
        char operation;
        boolean check;
        do {
            double result = 0;
            if (choice == 10) {
                float a = 0;
                float b = 0;
                operation = '0';
                do {
                    check = true;
                    try {
                        System.out.println("Enter number 1:");
                        a = sc.nextFloat();
                    } catch (NumberFormatException e) {

                        check = false;
                    } catch (Exception e) {
                        System.out.println("Enter number 1 again");
                        check = false;
                    }
                    sc.nextLine();
                } while (!check);
                do {
                    check = true;
                    try {
                        System.out.println("Enter 2nd number :");
                        b = sc.nextFloat();
                    } catch (NumberFormatException e) {
                        check = false;
                    } catch (Exception e) {
                        System.out.println("Enter a valid number!");
                        check = false;
                    }
                    sc.nextLine();
                } while (!check);
                do {
                    check = true;
                    try {
                        System.out.println("Enter your choice(+,-,/*)");
                        operation = sc.next().charAt(0);
                    } catch (Exception e) {
                        System.out.println("Please enter a valid character ");
                        check = false;
                    }
                    if ((operation != '+' && operation != '-') && (operation != '*' && operation != '/')) {
                        System.out.println("Select operation again ");
                        check = false;
                    }
                    sc.nextLine();
                } while (!check);
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
                System.out.println("Press any key to exit or enter to calculate again");
                choice = System.in.read();
            }
        } while (choice == 10);
        sc.close();
    }
}
