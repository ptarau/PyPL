package puzzle;


public class Main {

    public static void main(String[] args) {
	// write your code here
        System.out.println("hello");
        Board board=new Board();
        for(int start=0; start<15; start++) {
            Solver solver = new Solver(0);
            Display disp = new Display();
            solver.run();
            disp.show();
        }

    }
}
