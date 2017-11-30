package com.example.demo;

import java.util.ArrayList;
import java.util.Arrays;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import pojo.Empleado;
import pojo.Miembro;
import pojo.Sucursal;
import pojo.TipoPago;

@Service
public class RestService {
	private RestTemplate restService;
	
	@Value("${restUrl}")
	private String apiUrl;
	
	private RestService() {
		restService = new RestTemplate();
	}
	
	public ArrayList<Sucursal> getAllSucusales() {
		return new ArrayList<Sucursal>(Arrays.asList(restService.getForObject(apiUrl+"sucursales", Sucursal[].class)));
	}
	
	public ArrayList<Miembro> getMiembrosSucusal(int idSucursal) {
		return new ArrayList<Miembro>(Arrays.asList(restService.getForObject(apiUrl+"miembros/sucursal/"+idSucursal, Miembro[].class)));
	}
	
	public Sucursal getSucursal(int idSucursal) {	
		return  restService.getForObject(apiUrl+"sucursales/"+idSucursal, Sucursal.class);
	}
	
	public ArrayList<Empleado> getEmpleados(int idSucursal) {
		return new ArrayList<Empleado>(Arrays.asList(restService.getForObject(apiUrl+"empleados/sucursal/"+idSucursal, Empleado[].class)));
	}

	public ArrayList<TipoPago> getTipoPago() {
		return new ArrayList<TipoPago>(Arrays.asList(restService.getForObject(apiUrl+"tipoPagos", TipoPago[].class)));
	}
}
