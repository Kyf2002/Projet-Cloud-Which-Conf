# Projet-Cloud-Which-Conf
Projet de Cloud Computing

## But
Le but de ce projet est de realisé un script qui premet de faire une configuration automatique et optimale des ressources du domaine 0 (cpu, memoire...) à travers l'environnement xen.

## Prerequis
Pour réaliser notre projet on aura besoin d'un systeme d' exploitation de noyau linux. Nous avons choisi d'utiliser Ubuntu Server 20.04.

# Etapes de réalisation 
## Installer Python : 
Assurez-vous que Python est installé sur votre système en suivant les instructions d'installation pour votre système d'exploitation via la commande:
```bash
sudo apt update
sudo apt install python3
```
## Installation de Xen
Il existe essentiellement deux manières d'installer Xen sur un système d'exploitation à noyau Linux. La première consiste à le construire manuellement à partir des sources et la seconde consiste à installer des binaires pré-construits. Nous avons utilisé la deuxième méthode. Pour l'explication sur l'installation, consulter le lien suivant: https://github.com/djobiii2078/cloud_course_resources/tree/main/TP/TP1

## Modifier le script 
Ouvrez le script Python dans un éditeur de texte et ajustez les paramètres de configuration **dom0_memory_mb** et **dom0_vcpus** selon vos besoins. Vous pouvez également ajuster d'autres parties du script si nécessaire.

## Exécuter le script 
Une fois que vous avez enregistré les modifications, ouvrez un terminal ou une ligne de commande, accédez au répertoire où se trouve votre script Python et exécutez-le en tapant la commande suivante :
```bash
python nom_du_script.py
```
