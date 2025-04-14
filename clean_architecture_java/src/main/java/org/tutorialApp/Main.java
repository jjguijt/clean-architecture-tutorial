package org.tutorialApp;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        OrderReport orderReport = new OrderReport();
        try {
            List<String> report = orderReport.createReport();
            for (String line : report) {
                System.out.println(line);
            }
        } catch (Exception e) {
            System.err.println("Error generating report: " + e.getMessage());
        }
    }
}