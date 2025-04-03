Tutoriel : Mise en place d’un Dashboard Symfony (PHP 8.1 + Apache + Doctrine)
1. Préconfiguration du serveur Apache pour PHP 8.1
Avant toute chose, assurez-vous que le module PHP-FPM est bien en place et fonctionnel.

🔧 Étapes à suivre :

# 1.1 Démarrer le service PHP-FPM pour PHP 8.1
sudo systemctl start php8.1-fpm

# 1.2 Vérifier que le socket PHP-FPM existe
ls -l /run/php/php8.1-fpm.sock

# 1.3 Activer les modules nécessaires d'Apache
sudo a2enmod proxy_fcgi setenvif
sudo a2enmod rewrite

# 1.4 Redémarrer Apache pour appliquer les modifications
sudo systemctl restart apache2


2. Configuration de l’application Symfony
L’objectif ici est de configurer correctement les migrations Doctrine, indispensables à la gestion de la base de données.

📁 Étapes à suivre :

# 2.1 Créer le dossier pour les fichiers de migration
mkdir -p /var/www/gn_census/migrations

# 2.2 Ajouter un fichier vide pour versionner le dossier (optionnel mais utile)
touch /var/www/gn_census/migrations/.gitkeep

# 2.3 Vider le cache de Symfony pour repartir sur une base propre
php bin/console cache:clear

# 2.4 Vérifier l’état actuel des migrations (doit répondre sans erreur)
php bin/console doctrine:migrations:status

# 2.5 Générer une nouvelle migration (si des entités ont été créées ou modifiées)
php bin/console make:migration


Étapes suivantes possibles
Lancer le serveur local Symfony :

symfony serve
php bin/console doctrine:migrations:migrate


Activatin de php dans la configuration de VirtualHOST

    <FilesMatch \.php$>
    # Pour Apache 2.4.10+ avec PHP-FPM
      SetHandler "proxy:unix:/run/php/php8.1-fpm.sock|fcgi://localhost"
    </FilesMatch>




  

