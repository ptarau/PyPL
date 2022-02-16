package threads;

public class Producer implements Runnable {
    int who;
    CubbyHole ch;

    Producer(int who,CubbyHole ch) {
        this.who=who;
        this.ch=ch;
    }

    public void run() {
        for(int i=0; i<5;i++) {
            ch.put(who,i);
        }
    }
}
