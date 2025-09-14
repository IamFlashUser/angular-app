package com.ganatan.starter;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class StarterAppApplication {
	
	public static void main(String[] args) {
		System.out.println(" [ganatan] >>>Lancement de l'application StarterAppApplication");		
		SpringApplication.run(StarterAppApplication.class, args);
	}

}
