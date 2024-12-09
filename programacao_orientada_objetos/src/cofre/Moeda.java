package cofre;

public abstract class Moeda {
    double valor;
    public Moeda(double valor) {
        super();
        this.valor = valor;
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + (int)valor;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null) return false;
        if (getClass() != obj.getClass()) return false;
        Moeda other = (Moeda) obj;
        if (valor != other.valor) return false;
        return true;
    }

    abstract void info();
    abstract double converter();
}
