import java.util.InputMismatchException;
import java.util.Random;
import java.util.Scanner;

public class NumberGame {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_PURPLE = "\u001B[35m";
    public static final String ANSI_CYAN = "\u001B[36m";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random r = new Random();
        int random_number = 0;
        int number = 0;
        boolean game_play = true;
        while (game_play) {
            clear();
            boolean number_choice = true;
            int count = 0;
            int score = 0;
            System.out.println(ANSI_CYAN + "Welcome to the Number guessing game!" + ANSI_RESET);
            System.out.println("_".repeat(20));
            String textBlock = """
                    RULES:
                        \u2022 The player needs to guess the random number generated.
                        \u2022 Three attempts will be given for each round.
                        \u2022 Score will be provided based on number of attempts.
                    """;
            System.out.println(textBlock);
            boolean isReady = true;
            while (isReady) {
                System.out.println("Are you ready?(yes/no)");
                String ready = sc.next();
                String lower_ready = ready.toLowerCase();
                if (lower_ready.equals("yes")) {
                    System.out.println(ANSI_GREEN + "Let's go!!" + ANSI_RESET);
                    System.out.println("_".repeat(20));
                    isReady = false;
                } else if (lower_ready.equals("no")) {
                    System.out.println(ANSI_RED + "It's alright.Let's do it some other time." + ANSI_RESET);
                    game_play = false;
                    break;
                } else {
                    System.out.println(ANSI_RED + "Please provide a valid choice." + ANSI_RESET);
                    isReady = true;
                }
            }
            if (!game_play) {
                break;
            }
            random_number = r.nextInt(100);

            while (number_choice && count < 3) {
                try {
                    System.out.println("Enter a integer between 1 to 100");
                    number = sc.nextInt();
                    if (number > 0 && number <= 100) {
                        int difference = Math.abs(number - random_number);
                        if (number == random_number) {
                            System.out.println(ANSI_GREEN + "Yay!Your guess was right!" + ANSI_RESET);
                            break;
                        } else if (number < random_number) {
                            System.out.println(ANSI_PURPLE + "Go higher." + ANSI_RESET);
                        } else {
                            System.out.println(ANSI_PURPLE + "Go lower." + ANSI_RESET);
                        }
                        if (difference <= 15 && difference > 5) {
                            System.out.println(ANSI_YELLOW + "You are close!" + ANSI_RESET);
                        } else if (difference <= 5 && difference > 2) {
                            System.out.println(ANSI_BLUE + "You are very close!" + ANSI_RESET);
                        } else if (difference <= 2) {
                            System.out.println(ANSI_CYAN + "You are almost there!" + ANSI_RESET);
                        } else {
                            System.out.println(ANSI_RED + "That was not even close!" + ANSI_RESET);
                        }
                        count++;
                    } else {
                        System.out.println(ANSI_RED + "Number not in range.Please provide input within range." + ANSI_RESET);
                    }
                } catch (InputMismatchException nm) {
                    System.out.println(ANSI_RED + "Input is not a valid number.Please provide valid integer" + ANSI_RESET);
                    sc.next();
                }

            }
            score = (3 - count) * 10;
            System.out.println("The score is " + ANSI_GREEN + score + ANSI_RESET);
            if (count == 3) {
                System.out.println("Maximum limits reached!Game Over.");
            }
            System.out.println("The random number generated is " + ANSI_BLUE + random_number + ANSI_RESET);
            System.out.println("Do you want to go for another round?(yes/no)");
            boolean game_choice = true;
            while (game_choice) {
                String given_choice = sc.next();
                String choice = given_choice.toLowerCase();
                if (choice.equals("yes")) {
                    game_play = true;
                    game_choice = false;
                } else if (choice.equals("no")) {
                    game_play = false;
                    game_choice = false;
                } else {
                    System.out.println(ANSI_RED + "Please provide a valid choice." + ANSI_RESET);
                    game_choice = true;
                }
            }

        }
        System.out.println(ANSI_PURPLE + "Thank you for playing!" + ANSI_RESET);
    }

    public static void clear() {
        System.out.println("*".repeat(20));
    }
}
