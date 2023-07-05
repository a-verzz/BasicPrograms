public class DiamondPattern {
    public static void printDiamond(int size) {
        int spaces = size - 1;
        int stars = 1;

        // Upper half of the diamond
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < stars; j++) {
                System.out.print("* ");
            }
            System.out.println();
            spaces--;
            stars++;
        }

        // Lower half of the diamond
        spaces = 1;
        stars = size - 1;
        for (int i = 0; i < size - 1; i++) {
            for (int j = 0; j < spaces; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < stars; j++) {
                System.out.print("* ");
            }
            System.out.println();
            spaces++;
            stars--;
        }
    }

    public static void main(String[] args) {
        int size = 5;
        printDiamond(size);
    }
}
