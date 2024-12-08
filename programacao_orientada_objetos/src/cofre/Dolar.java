package cofre;

public class Dolar extends Moeda {
	public Dolar(double valor) {
		super(valor);
	}

	@Override
	void info() {
        System.out.println("Dolar: " + this.valor);
	}

	@Override
	double converter() {
		return this.valor * 6D;
	}
}
