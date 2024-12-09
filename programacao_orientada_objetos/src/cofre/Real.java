package cofre;

public class Real extends Moeda {
    public Real(double valor) {
        super(valor);
    }

    @Override
    void info() {
        System.out.println("Real: " + this.valor);
    }

    @Override
    double converter() {
        return valor * 1D;
    }
}
