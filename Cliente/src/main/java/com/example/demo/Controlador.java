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
	public String getAll(ModelMap model, @CookieValue("sucursal") String sucursal) {
		int idSucursal = Integer.parseInt(sucursal);
		model.addAttribute("sucursal",rest.getSucursal(idSucursal));
		model.addAttribute("listaMiembros",rest.getMiembrosSucusal(idSucursal));
		System.out.println("Mi Cookie es :"+sucursal);
		return "index";
	}

	@GetMapping("/login")
	public String logIn(ModelMap model) {
		return "login";
	}
}
