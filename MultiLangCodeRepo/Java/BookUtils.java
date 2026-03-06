import java.util.ArrayList;

public class BookUtils {

    public static Book findOldestBook(ArrayList<Book> books) {

        Book oldest = null;

        for (Book b : books) {

            if (oldest == null) {
                oldest = b;
            } else {

                if (b.getYear() < oldest.getYear()) {
                    oldest = b;
                }

            }

        }

        return oldest;
    }
}