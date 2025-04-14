package org.example001;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        double_number();
    }

    public static void double_number() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter a number..");
        int number = scanner.nextInt();
        int result = number * 2;
        System.out.println("The result is " + result);
    }
}