import java.util.Scanner;

public class LibraryApp {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        LibraryService service = new LibraryService();

        while (true) {
            System.out.println("\n==== Library Menu ====");
            System.out.println("1. Add Book");
            System.out.println("2. View Books");
            System.out.println("3. Borrow Book");
            System.out.println("4. Return Book");
            System.out.println("5. Show Statistics");
            System.out.println("0. Exit");

            System.out.print("Choose option: ");
            int choice = scanner.nextInt();
            scanner.nextLine();

            if (choice == 1) {

                System.out.print("Title: ");
                String title = scanner.nextLine();

                System.out.print("Author: ");
                String author = scanner.nextLine();

                System.out.print("Year: ");
                int year = scanner.nextInt();
                scanner.nextLine();

                service.addBook(title, author, year);

            } else if (choice == 2) {

                service.listBooks();

            } else if (choice == 3) {

                System.out.print("Enter book index: ");
                int index = scanner.nextInt();

                service.borrowBook(index);

            } else if (choice == 4) {

                System.out.print("Enter book index: ");
                int index = scanner.nextInt();

                service.returnBook(index);

            } else if (choice == 5) {

                service.showStats();

            } else if (choice == 0) {

                System.out.println("Exiting...");
                break;

            } else {

                System.out.println("Invalid choice");

            }
        }
    }
}