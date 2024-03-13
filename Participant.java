import java.io.*;
import java.net.*;
import java.util.*;

public class Participant {
    public static void main(String[] args) {
        try {
            String RESET = "\033[0m";  // Text Reset
            String BLACK = "\033[0;30m";   // BLACK
            String RED = "\033[0;31m";     // RED
            String GREEN = "\033[0;32m";   // GREEN
            String YELLOW = "\033[0;33m";  // YELLOW
            String BLUE = "\033[0;34m";    // BLUE
            String PURPLE = "\033[0;35m";  // PURPLE
            String CYAN = "\033[0;36m";    // CYAN
            String WHITE = "\033[0;37m";   // WHITE

            Socket socket = new Socket("localhost", 12345); // Connect to Coordinator (localhost) on port 12345
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            int port = socket.getLocalPort(); // Get the port address of the current participant
            System.out.println(CYAN + "Local Port Address: " + port + RESET); // Print the port address

            // Wait to receive PREPARE message from Coordinator
            System.out.println("\nWaiting for the PREPARE from the Coordinator...");
            String prepareMessage = in.readLine();
            if ("PREPARE".equals(prepareMessage)) {
                System.out.println(GREEN + "\nReceived PREPARE from the Coordinator." + RESET);
                Scanner scanner = new Scanner(System.in);
                System.out.print(YELLOW + "\nAre you ready to commit? (Enter READY or NOT_READY): " + RESET);
                String response = scanner.nextLine();
                out.println(response); // Send response to Coordinator
                System.out.println("\nSending " + response + " to the Coordinator.");
            }

            // Wait to receive decision from Coordinator
            String decision = in.readLine();
            if (decision.equals("ABORT")) {
                System.out.println(RED + "\nReceived decision from the Coordinator: " + decision + RESET);
            } else {
                System.out.println(GREEN + "\nReceived decision from the Coordinator: " + decision + RESET);
            }
            

            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
