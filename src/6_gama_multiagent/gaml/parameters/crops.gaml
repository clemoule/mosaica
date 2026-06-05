global {
  float available_surface <- 500.0;
  int nb_cultures <- 3;
  list<string> culture_names <- ["Blé", "Maïs", "Orge"];
  list<float> rendement_par_hectare <- [4.0, 6.0, 5.0];
  list<float> prix_par_ton <- [220.0, 160.0, 190.0];
  list<float> production_maximale <- [1500.0, 1800.0, 1200.0];
  list<float> surface_maximale <- [0.0, 0.0, 0.0];
  list<float> surface_allouee <- [0.0, 0.0, 0.0];
  float revenu_total <- 0.0;
}

action init_crop_parameters {
  loop i from:0 to:(nb_cultures - 1) {
    surface_maximale[i] <- production_maximale[i] / rendement_par_hectare[i];
  }
}
