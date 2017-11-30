package com.example.demo;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown=true)
public class Miembro {
	private int activoMiembro;	 
	private String apellidoMiembro;
	private int idMiembro;
	private int idSucursal;
	private String nombreMiembro;
	private int telefonoMiembro;
	
	public Miembro() {
		
	}
	
	public Miembro(int activoMiembro, String apellidoMiembro, int idMiembro, int idSucursal, String nombreMiembro, int telefonoMiembro) {
		this.activoMiembro = activoMiembro;
		this.apellidoMiembro = apellidoMiembro;
		this.idMiembro = idMiembro;
		this.idSucursal = idSucursal;
		this.nombreMiembro = nombreMiembro;
		this.telefonoMiembro = telefonoMiembro;
	}

	public int getActivoMiembro() {
		return activoMiembro;
	}

	public void setActivoMiembro(int activoMiembro) {
		this.activoMiembro = activoMiembro;
	}

	public String getApellidoMiembro() {
		return apellidoMiembro;
	}

	public void setApellidoMiembro(String apellidoMiembro) {
		this.apellidoMiembro = apellidoMiembro;
	}

	public int getIdMiembro() {
		return idMiembro;
	}

	public void setIdMiembro(int idMiembro) {
		this.idMiembro = idMiembro;
	}

	public int getIdSucursal() {
		return idSucursal;
	}

	public void setIdSucursal(int idSucursal) {
		this.idSucursal = idSucursal;
	}

	public String getNombreMiembro() {
		return nombreMiembro;
	}

	public void setNombreMiembro(String nombreMiembro) {
		this.nombreMiembro = nombreMiembro;
	}


	public int getTelefonoMiembro() {
		return telefonoMiembro;
	}


	public void setTelefonoMiembro(int telefonoMiembro) {
		this.telefonoMiembro = telefonoMiembro;
	}
	
	
	
	
	
	
}