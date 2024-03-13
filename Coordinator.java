import java.io.*;
import java.net.*;
import java.util.*;

public class Coordinator {
    private static ServerSocket serverSocket;
    private static List<Socket> participants = new ArrayList<>();
    private static List<String> participantResponses = new ArrayList<>();
    private static int expectedParticipants;
    private static boolean preparePhase = false;

    public static final String RESET = "\033[0m"; 
    public static final String BLACK = "\033[0;30m";   // BLACK
    public static final String RED = "\033[0;31m";     // RED
    public static final String GREEN = "\033[0;32m";   // GREEN
    public static final String YELLOW = "\033[0;33m";  // YELLOW
    public static final String BLUE = "\033[0;34m";    // BLUE
    public static final String PURPLE = "\033[0;35m";  // PURPLE
    public static final String CYAN = "\033[0;36m";    // CYAN
    public static final String WHITE = "\033[0;37m";   // WHITE

    public static void main(String[] args) {
        try {
            serverSocket = new ServerSocket(12345); // Server socket listening on port 12345
            Scanner scanner = new Scanner(System.in);
            System.out.print(CYAN + "Enter the number of participants: " + RESET);
            expectedParticipants = scanner.nextInt();

            // Accept participants until expected number is reached
            System.out.println("Waiting for the Participants...");
            System.out.println();
            while (participants.size() < expectedParticipants) {
                Socket participant = serverSocket.accept();
                participants.add(participant);
                System.out.println(GREEN + "Participant " + participants.size() + " connected from: " + participant.getRemoteSocketAddress() + RESET);

                // If expected number of participants is reached, start prepare phase
                if (participants.size() == expectedParticipants && !preparePhase) {
                    preparePhase = true;
                    sendPrepareMessage();
                }
            }

            // Receive responses from participants
            receiveResponsesFromParticipants();

            // Make decision based on received responses
            makeDecision();

            // Close all connections
            closeConnections();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void sendPrepareMessage() {
        System.out.println("\nSending PREPARE message to all participants...");
        sendMessageToAll("PREPARE");
    }

    private static void sendMessageToAll(String message) {
        for (Socket participant : participants) {
            try {
                PrintWriter out = new PrintWriter(participant.getOutputStream(), true);
                out.println(message);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    private static void receiveResponsesFromParticipants() throws IOException {
        System.out.println();
        for (Socket participant : participants) {
            BufferedReader in = new BufferedReader(new InputStreamReader(participant.getInputStream()));
            String response = in.readLine();
            participantResponses.add(response);
            System.out.println(BLUE + "Received " + response + " response from participant: " + participant.getRemoteSocketAddress() + RESET);
        }
    }

    private static void makeDecision() {
        if (participantResponses.contains("NOT_READY")) {
            System.out.println(RED + "\nTransaction aborting..." + RESET);
            sendMessageToAll("ABORT");
        } else {
            System.out.println(GREEN + "\nTransaction COMMITING..." + RESET);
            sendMessageToAll("COMMIT");
        }
    }

    private static void closeConnections() {
        try {
            serverSocket.close();
            for (Socket participant : participants) {
                participant.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
