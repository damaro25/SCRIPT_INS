# SCRIPT_INS
Tutoriel : Mise en place dâ€™un Dashboard Symfony (PHP 8.1 + Apache + Doctrine)
1. PrÃ©configuration du serveur Apache pour PHP 8.1
Avant toute chose, assurez-vous que le module PHP-FPM est bien en place et fonctionnel.

ðŸ”§ Ã‰tapes Ã  suivre :

# 1.1 DÃ©marrer le service PHP-FPM pour PHP 8.1
sudo systemctl start php8.1-fpm

# 1.2 VÃ©rifier que le socket PHP-FPM existe
ls -l /run/php/php8.1-fpm.sock

# 1.3 Activer les modules nÃ©cessaires d'Apache
sudo a2enmod proxy_fcgi setenvif
sudo a2enmod rewrite

# 1.4 RedÃ©marrer Apache pour appliquer les modifications
sudo systemctl restart apache2


2. Configuration de lâ€™application Symfony
Lâ€™objectif ici est de configurer correctement les migrations Doctrine, indispensables Ã  la gestion de la base de donnÃ©es.

ðŸ“ Ã‰tapes Ã  suivre :

# 2.1 CrÃ©er le dossier pour les fichiers de migration
mkdir -p /var/www/gn_census/migrations

# 2.2 Ajouter un fichier vide pour versionner le dossier (optionnel mais utile)
touch /var/www/gn_census/migrations/.gitkeep

# 2.3 Vider le cache de Symfony pour repartir sur une base propre
php bin/console cache:clear

# 2.4 VÃ©rifier lâ€™Ã©tat actuel des migrations (doit rÃ©pondre sans erreur)
php bin/console doctrine:migrations:status

# 2.5 GÃ©nÃ©rer une nouvelle migration (si des entitÃ©s ont Ã©tÃ© crÃ©Ã©es ou modifiÃ©es)
php bin/console make:migration


Ã‰tapes suivantes possibles
Lancer le serveur local Symfony :

symfony serve
php bin/console doctrine:migrations:migrate


Activatin de php dans la configuration de VirtualHOST

    <FilesMatch \.php$>
    # Pour Apache 2.4.10+ avec PHP-FPM
      SetHandler "proxy:unix:/run/php/php8.1-fpm.sock|fcgi://localhost"
    </FilesMatch>




  

