public class Book {

    private String title;
    private String author;
    private int year;
    private boolean borrowed;

    public Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
        this.borrowed = false;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getYear() {
        return year;
    }

    public boolean isBorrowed() {
        return borrowed;
    }

    public void borrow() {
        borrowed = true;
    }

    public void giveBack() {
        borrowed = false;
    }

    @Override
    public String toString() {

        String status;

        if (borrowed) {
            status = "Borrowed";
        } else {
            status = "Available";
        }

        return title + " | " + author + " | " + year + " | " + status;
    }
}