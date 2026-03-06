import java.util.Scanner;

public class InputHelper {

    public static int readInt(String message) {

        Scanner scanner = new Scanner(System.in);

        System.out.print(message);

        int value = scanner.nextInt();

        return value;
    }

    public static String readText(String message) {

        Scanner scanner = new Scanner(System.in);

        System.out.print(message);

        String text = scanner.nextLine();

        return text;
    }
}