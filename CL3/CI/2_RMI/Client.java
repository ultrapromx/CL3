import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Get the registry
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

            // Look up the remote object
            StringConcat stub = (StringConcat) registry.lookup("ConcatService");

            // Prompt user for input
            System.out.println("Enter first string:");
            String s1 = scanner.nextLine();
            System.out.println("Enter second string:");
            String s2 = scanner.nextLine();

            // Check for null input
            if (s1.isEmpty() || s2.isEmpty()) {
                System.out.println("Empty string(s) provided, cannot concatenate.");
            } else {
                // Call the remote method
                String response = stub.concatenate(s1, s2);
                System.out.println("Concatenated string: " + response);
            }
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        } finally {
            scanner.close();
        }
    }
}
