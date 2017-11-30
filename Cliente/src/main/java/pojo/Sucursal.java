package pojo;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown=true)
public class Sucursal {
	private int activoSucursal;
	private String contrasenaSucursal;
	private String direccionSucursal;
	private int idSucursal;
	private String nombreSucursal;
	private int telefonoSucursal;
	private String userSucursal;
	
	
	public Sucursal() {
		
	}


	public Sucursal(int activoSucursal, String contrasenaSucursal, String direccionSucursal, int idSucursal,
			String nombreSucursal, int telefonoSucursal, String userSucursal) {
		this.activoSucursal = activoSucursal;
		this.contrasenaSucursal = contrasenaSucursal;
		this.direccionSucursal = direccionSucursal;
		this.idSucursal = idSucursal;
		this.nombreSucursal = nombreSucursal;
		this.telefonoSucursal = telefonoSucursal;
		this.userSucursal = userSucursal;
	}


	public int getActivoSucursal() {
		return activoSucursal;
	}


	public void setActivoSucursal(int activoSucursal) {
		this.activoSucursal = activoSucursal;
	}


	public String getContrasenaSucursal() {
		return contrasenaSucursal;
	}


	public void setContrasenaSucursal(String contrasenaSucursal) {
		this.contrasenaSucursal = contrasenaSucursal;
	}


	public String getDireccionSucursal() {
		return direccionSucursal;
	}


	public void setDireccionSucursal(String direccionSucursal) {
		this.direccionSucursal = direccionSucursal;
	}


	public int getIdSucursal() {
		return idSucursal;
	}


	public void setIdSucursal(int idSucursal) {
		this.idSucursal = idSucursal;
	}


	public String getNombreSucursal() {
		return nombreSucursal;
	}


	public void setNombreSucursal(String nombreSucursal) {
		this.nombreSucursal = nombreSucursal;
	}


	public int getTelefonoSucursal() {
		return telefonoSucursal;
	}


	public void setTelefonoSucursal(int telefonoSucursal) {
		this.telefonoSucursal = telefonoSucursal;
	}


	public String getUserSucursal() {
		return userSucursal;
	}


	public void setUserSucursal(String userSucursal) {
		this.userSucursal = userSucursal;
	}
		

}
