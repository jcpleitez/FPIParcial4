package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.CookieValue;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class Controlador {
	@Autowired
	RestService rest;
	
	@GetMapping("/index")
	public String getAllBrands(ModelMap model, @CookieValue("sucursal") String sucursal) {
		//model.addAttribute("lista",rest.getAllMiembros());
		System.out.println("Mi Cookie es :"+sucursal);
		return "index";
	}

	@GetMapping("/login")
	public String logIn(ModelMap model) {
		return "login";
	}
}
