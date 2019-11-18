package threads;

public class Consumer implements Runnable {
    int who;
    CubbyHole ch;
    Consumer(int who,CubbyHole ch) {
        this.who=who;
        this.ch=ch;
    }

    public void run() {
        for(int i=0; i<5;i++) {
            ch.get(who);
        }
    }
}
