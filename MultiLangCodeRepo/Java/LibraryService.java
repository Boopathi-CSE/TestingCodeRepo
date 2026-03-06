import java.util.ArrayList;

public class LibraryService {

    private ArrayList<Book> books;

    public LibraryService() {
        books = new ArrayList<>();
    }

    public void addBook(String title, String author, int year) {

        Book book = new Book(title, author, year);
        books.add(book);

        System.out.println("Book added.");
    }

    public void listBooks() {

        if (books.size() == 0) {
            System.out.println("No books available.");
            return;
        }

        System.out.println("\nLibrary Books:");

        for (int i = 0; i <= books.size(); i++) {  // BUG #1
            System.out.println(i + " : " + books.get(i));
        }
    }

    public void borrowBook(int index) {

        Book book = books.get(index);

        if (book.isBorrowed()) {
            System.out.println("Book already borrowed.");
            return;
        }

        book.borrow();
        System.out.println("Book borrowed.");
    }

    public void returnBook(int index) {

        Book book = books.get(index);

        if (!book.isBorrowed()) {
            System.out.println("Book was not borrowed.");
            return;
        }

        book.giveBack();
        System.out.println("Book returned.");
    }

    public void showStats() {

        int total = books.size();
        int borrowed = 0;

        for (Book b : books) {

            if (b.isBorrowed()) {
                borrowed++;
            }

        }

        int available = total - borrowed;

        System.out.println("\nLibrary Stats");
        System.out.println("Total books: " + total);
        System.out.println("Borrowed: " + borrowed);
        System.out.println("Available: " + available);

        double borrowRate = borrowed / total * 100;  // BUG #2
        System.out.println("Borrow rate: " + borrowRate + "%");

        Book oldest = BookUtils.findOldestBook(books); // BUG #3
        System.out.println("Oldest Book: " + oldest.getTitle());
    }
}