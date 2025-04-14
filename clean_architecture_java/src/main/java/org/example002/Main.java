package org.example002;

import java.time.LocalDate;
import java.time.LocalTime;

public class Main {
    public static void main(String[] args) {
        Order order = new Order();
        LocalDate expected_date = schedule_production_of_order(order);

        System.out.println("The expected production date is " + expected_date);
    }

    public static LocalDate schedule_production_of_order(Order order) {
        LocalTime currentTime = LocalTime.now();
        LocalTime cutoffTime = LocalTime.of(18, 0);
        LocalDate resultDate;

        Scheduler scheduler = new Scheduler();
        scheduler.schedule_order(order);

        // If we're past 6PM, we expect the order to be produced the next day.
        if (currentTime.isAfter(cutoffTime)) {
            resultDate = LocalDate.now().plusDays(1);
        } else {
            resultDate = LocalDate.now();
        }

        return resultDate;
    }
}