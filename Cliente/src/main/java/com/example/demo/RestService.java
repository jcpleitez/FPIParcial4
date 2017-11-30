package com.example.demo;

import java.util.ArrayList;
import java.util.Arrays;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.example.demo.Miembro;

@Service
public class RestService {
	private RestTemplate restService;
	
	@Value("${restUrl}")
	private String apiUrl;
	
	private RestService() {
		restService = new RestTemplate();
	}
	
	public ArrayList<Miembro> getAllMiembros() {
		System.out.println(Arrays.asList(restService.getForObject(apiUrl+"miembros", Miembro[].class)));
		return new ArrayList<Miembro>(Arrays.asList(restService.getForObject(apiUrl+"miembros", Miembro[].class)));
	}
}
