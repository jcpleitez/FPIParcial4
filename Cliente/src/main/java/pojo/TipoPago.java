package pojo;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown=true)
public class TipoPago {
	private String descripcionTipoPago;
	private int idTipoPago;
	private String nombreTipoPago;
	private double precioTipoPago;
	
	public TipoPago() {
		
	}
	
	public TipoPago(String descripcionTipoPago, int idTipoPago, String nombreTipoPago, double precioTipoPago) {
		this.descripcionTipoPago = descripcionTipoPago;
		this.idTipoPago = idTipoPago;
		this.nombreTipoPago = nombreTipoPago;
		this.precioTipoPago = precioTipoPago;
	}

	public String getDescripcionTipoPago() {
		return descripcionTipoPago;
	}

	public void setDescripcionTipoPago(String descripcionTipoPago) {
		this.descripcionTipoPago = descripcionTipoPago;
	}

	public int getIdTipoPago() {
		return idTipoPago;
	}

	public void setIdTipoPago(int idTipoPago) {
		this.idTipoPago = idTipoPago;
	}

	public String getNombreTipoPago() {
		return nombreTipoPago;
	}

	public void setNombreTipoPago(String nombreTipoPago) {
		this.nombreTipoPago = nombreTipoPago;
	}

	public double getPrecioTipoPago() {
		return precioTipoPago;
	}

	public void setPrecioTipoPago(double precioTipoPago) {
		this.precioTipoPago = precioTipoPago;
	}
	
	
	
}
