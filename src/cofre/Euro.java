package cofre;

public class Euro extends Moeda {
	public Euro(double valor) {
		super(valor);
	}

	@Override
	void info() {
        System.out.println("Euro: " + this.valor);
	}

	@Override
	double converter() {
		return valor * 7D;
	}
}
