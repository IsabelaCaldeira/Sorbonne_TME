#!/bin/bash
CSV_FILE="blabla.csv"

# Vérifier que le fichier CSV existe
if [ ! -f "$CSV_FILE" ]; then
  echo "Fichier CSV introuvable : $CSV_FILE"
  exit 1
fi

# Demander VF/VO
read -p "Choisissez VF ou VO : " choix
choix=$(echo "$choix" | tr '[:lower:]' '[:upper:]')

# Validation de la choix
if [ "$choix" != "VF" ] && [ "$choix" != "VO" ]; then
  echo "Choix invalide. Utilisez VF ou VO."
  exit 1
fi

# Choisir colonne : VF -> 2, VO -> 3
col=2
[ "$choix" = "VO" ] && col=3

# Parcourir le CSV
OLDIFS=$IFS
IFS=','

while IFS=',' read -r animal cri_vf cri_vo; do
  # ignorer lignes vides ou mal formées
  [ -z "$animal" ] && continue

  # choisir le cri selon VF/VO
  if [ "$col" -eq 2 ]; then
    son="$cri_vf"
  else
    son="$cri_vo"
  fi

  # nettoyer espaces en début/fin
  animal=$(echo "$animal" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
  son=$(echo "$son" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')

  # si le modèle cowsay existe, l'utiliser, sinon afficher le message
  if cowsay -f "$animal" "" >/dev/null 2>&1; then
    cowsay -f "$animal" "$son"
  else
    echo "cowsay: modèle '$animal' introuvable — \"$son\""
  fi
done < "$CSV_FILE"

IFS=$OLDIFS