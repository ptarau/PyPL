package puzzle;

class Solver extends Object {
    Solver(int start) {
        this.start=start;
        System.out.println("starting solver: "+ start);
    }

    int start;

    void run() {
        System.out.println("running solver");
    }
}
