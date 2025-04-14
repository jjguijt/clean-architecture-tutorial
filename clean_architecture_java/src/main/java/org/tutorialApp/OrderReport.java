package org.tutorialApp;


import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.ArrayList;
import java.util.List;

class OrderReport {
    private static final String BASE_URL = "http://127.0.0.1:5000";

    public List<String> createReport() throws IOException, InterruptedException {
        List<String> reportLines = new ArrayList<>();
        HttpClient client = HttpClient.newHttpClient();

        // Fetch orders
        HttpRequest ordersRequest = HttpRequest.newBuilder()
                .uri(URI.create(BASE_URL + "/api/v1/get_orders"))
                .GET()
                .build();
        HttpResponse<String> ordersResponse = client.send(ordersRequest, HttpResponse.BodyHandlers.ofString());
        JSONArray orders = new JSONArray(ordersResponse.body());

        // Process each order
        for (int i = 0; i < orders.length(); i++) {
            JSONArray products = new JSONArray();
            double price = 0;
            JSONArray order = orders.getJSONArray(i);
            String orderId = order.getString(0);
            String customerName = order.getString(1);

            // Fetch order details
            HttpRequest orderRequest = HttpRequest.newBuilder()
                    .uri(URI.create(BASE_URL + "/api/v1/read_order/" + orderId))
                    .GET()
                    .build();
            HttpResponse<String> orderResponse = client.send(orderRequest, HttpResponse.BodyHandlers.ofString());

            if (orderResponse.statusCode() == 200) {
                JSONArray orderItems = new JSONArray(orderResponse.body());
                for (int j = 0; j < orderItems.length(); j++) {
                    JSONArray orderItem = orderItems.getJSONArray(j);
                    String productId = orderItem.getString(1);

                    int quantity = orderItem.getInt(2);

                    // Fetch product details
                    JSONObject product = getProduct(productId);
                    products.put(product);
                    price += quantity * product.getDouble("price_in_euros");
                }
            }

            // Generate report line
            StringBuilder productNames = new StringBuilder();
            for (int j = 0; j < products.length(); j++) {
                if (j > 0) productNames.append(", ");
                productNames.append(products.getJSONObject(j).getString("name"));
            }
            reportLines.add(String.format("Order %s for %s has price €%.2f and products: %s",
                    orderId, customerName, price, productNames));
        }

        return reportLines;
    }

    private JSONObject getProduct(String id) throws IOException, InterruptedException {
        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://127.0.0.1:5000/api/v1/get_product/" + id))
                .GET()
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        if (response.statusCode() == 200) {
            JSONArray productArray = new JSONArray(response.body());
            JSONObject product = new JSONObject();
            product.put("name", productArray.getString(1));
            product.put("price_in_euros", 0.01 * productArray.getDouble(2));
            return product;
        } else {
            throw new RuntimeException("Could not get product information from the database");
        }
    }
}
