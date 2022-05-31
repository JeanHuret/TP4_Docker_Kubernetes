import configdb
import modules.connexiondb as db
import modules.qcm as qcm
import modules.utilisateurs as utilisateurs

bdd = db.ConnexionDb(configdb.config)
connexion = bdd.connect()

choix_donnees = input('Choisir : 1 - Membre, 2 - Admin : ')
if choix_donnees == "1":
    questionnaire = qcm.Questionnaire(utilisateurs, connexion)
    membre = utilisateurs.Membre(qcm, connexion)
    choix = input('Choisir : 1 - Liste des QCM, 2 - Faire un QCM 3 - Modifier ses informations : ')
    if choix == "1":
        for un_machine in machine.listeMachines():
            print(un_machine)
    elif choix == "2":
        donnees_machines = machine.saisie_machine()
        print(machine.ajouterMachine(donnees_machines))
    elif choix == "3":
        identifiant = input('Nom de la machine')
        print(machine.voirMachine(identifiant))
    elif choix == "4":
        identifiant = input('Nom de la machine')
        donnees_machines = machine.saisie_machine()
        print(machine.modifierMachine(identifiant, donnees_machines))
    elif choix == "5":
        identifiant = input('Nom de la machine')
        print(machine.supprimerMachine(identifiant))
    elif choix == "6":
        id_machine = input('identifiant de la machine')
        id_application = input('identifiant de l\'application')
        print(machine.lierApplication(id_application,id_machine))
    else :
        print("Merci de saisir  un choix valide")
elif choix_donnees == "2":
    questionnaire = qcm.Questionnaire(utilisateurs, connexion)
    admin = utilisateurs.Admin(qcm, connexion)
    choix = input('Choisir : 1 - Liste des catégories,  2 - Ajouter un QCM, 3 - Voir un QCM, 4 - Modifier un QCM , 5 - Supprimer un QCM, 6 - Supprimer un membre : ')
    if choix == "1":
        for un_application in application.listeapplications():
            print(un_application)
    elif choix == "2":
        donnees_application = application.saisie_application()
        print(application.ajouterapplication(donnees_application))
    elif choix == "3":
        identifiant = input('Nom de l\'application')
        print(application.voirapplication(identifiant))
    elif choix == "4":
        for un_application in application.listeapplications():
            print(un_application[1])
        choix_app = input('Quelle application (nom) voulez vous modifier')
        app = application.voirapplication(choix_app)
        donnees_application = application.saisie_application(app)
        print(application.modifierapplication(donnees_application))
    elif choix == "5":
        identifiant = input('Nom de l\'application')
        print(application.supprimerapplication(identifiant))
    elif choix == "6":
        identifiant = input('Nom de l\'application')
        print(application.supprimerapplication(identifiant))
    else :
        print("Merci de saisir  un choix valide")
else :
    print("Merci de saisir  un choix valide")
