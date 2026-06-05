action compute_optimal_cropping {
  init_crop_parameters;

  float surface_restante <- available_surface;
  list<bool> choix <- [false, false, false];
  list<float> densite_revenu <- [0.0, 0.0, 0.0];

  loop i from:0 to:(nb_cultures - 1) {
    densite_revenu[i] <- rendement_par_hectare[i] * prix_par_ton[i];
    surface_allouee[i] <- 0.0;
  }

  loop k from:0 to:(nb_cultures - 1) {
    int meilleur <- -1;
    float meilleur_valeur <- -1.0;

    loop i from:0 to:(nb_cultures - 1) {
      if (!choix[i] and densite_revenu[i] > meilleur_valeur) {
        meilleur <- i;
        meilleur_valeur <- densite_revenu[i];
      }
    }

    if (meilleur == -1) {
      break;
    }

    float allocation <- min(surface_restante, surface_maximale[meilleur]);
    surface_allouee[meilleur] <- allocation;
    surface_restante <- surface_restante - allocation;
    choix[meilleur] <- true;

    if (surface_restante <= 0.0) {
      break;
    }
  }

  revenu_total <- 0.0;
  loop i from:0 to:(nb_cultures - 1) {
    revenu_total <- revenu_total + surface_allouee[i] * rendement_par_hectare[i] * prix_par_ton[i];
  }
}

experiment optimization_test type: gui {
  init {
    compute_optimal_cropping;
  }

  output {
    display result {
      text "Plan d'optimisation des cultures";
      text "Surface disponible : " + available_surface + " ha";
      text "Revenu optimal : " + revenu_total + " €";
      loop i from:0 to:(nb_cultures - 1) {
        text culture_names[i] + " : " + surface_allouee[i] + " ha";
      }
    }
  }
}
