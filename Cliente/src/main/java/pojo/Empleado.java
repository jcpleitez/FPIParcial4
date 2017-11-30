package pojo;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown=true)
public class Empleado {
	
	private int activoEmpleado;	 
	private String apellidoEmpleado;
	private int idEmpleado;
	private int idSucursal;
	private String nombreEmpleado;
	private int telefonoEmpleado;
	
	public Empleado() {
		
	}

	public Empleado(int activoEmpleado, String apellidoEmpleado, int idEmpleado, int idSucursal, String nombreEmpleado,
			int telefonoEmpleado) {
		this.activoEmpleado = activoEmpleado;
		this.apellidoEmpleado = apellidoEmpleado;
		this.idEmpleado = idEmpleado;
		this.idSucursal = idSucursal;
		this.nombreEmpleado = nombreEmpleado;
		this.telefonoEmpleado = telefonoEmpleado;
	}

	public int getActivoEmpleado() {
		return activoEmpleado;
	}

	public void setActivoEmpleado(int activoEmpleado) {
		this.activoEmpleado = activoEmpleado;
	}

	public String getApellidoEmpleado() {
		return apellidoEmpleado;
	}

	public void setApellidoEmpleado(String apellidoEmpleado) {
		this.apellidoEmpleado = apellidoEmpleado;
	}

	public int getIdEmpleado() {
		return idEmpleado;
	}

	public void setIdEmpleado(int idEmpleado) {
		this.idEmpleado = idEmpleado;
	}

	public int getIdSucursal() {
		return idSucursal;
	}

	public void setIdSucursal(int idSucursal) {
		this.idSucursal = idSucursal;
	}

	public String getNombreEmpleado() {
		return nombreEmpleado;
	}

	public void setNombreEmpleado(String nombreEmpleado) {
		this.nombreEmpleado = nombreEmpleado;
	}

	public int getTelefonoEmpleado() {
		return telefonoEmpleado;
	}

	public void setTelefonoEmpleado(int telefonoEmpleado) {
		this.telefonoEmpleado = telefonoEmpleado;
	}

}
