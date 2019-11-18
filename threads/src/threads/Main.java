package threads;

public class Main {

    public static void main(String[] args) {
        System.out.println("starting");
        CubbyHole CH=new CubbyHole();
        Producer p1 = new Producer(1,CH);
        Producer p2 = new Producer(2,CH);
        Consumer c1 = new Consumer(1,CH);
        Consumer c2 = new Consumer(2,CH);
        Thread tp1=new Thread(p1);
        Thread tp2=new Thread(p2);
        Thread tc1=new Thread(c1);
        Thread tc2=new Thread(c2);
        tp1.start();
        tc1.start();
        tp2.start();
        tc2.start();

    }
}
