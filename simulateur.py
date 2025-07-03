# Simulateur de sérénité Harmoniq AI

# This CLI application interacts with the user in French
# to estimate time, energy, and money savings through automation.

import sys


def ask_tasks():
    print("\n🧩 Étape 1 – Tâches chronophages\n")
    options = [
        "Gérer mes e-mails",
        "Relancer mes clients",
        "Créer des devis ou factures",
        "Répondre à des formulaires",
        "Organiser mon agenda / mes rendez-vous",
        "Gérer des fichiers ou des bases de données",
        "Autre (précisez)"
    ]
    for idx, opt in enumerate(options, 1):
        print(f"{idx}. {opt}")
    selected = input("Sélectionne les numéros correspondants (séparés par des virgules) : ")
    others = ""
    if '7' in selected.split(','):
        others = input("Précise les autres tâches : ")
    return selected, others


def ask_hours():
    while True:
        try:
            hours = int(input("\n⏱ Étape 2 – Combien d’heures par semaine passes-tu sur ces tâches ? (1-30) : "))
            if 1 <= hours <= 30:
                return hours
        except ValueError:
            pass
        print("Merci de saisir un nombre entre 1 et 30.")


def ask_rate():
    while True:
        try:
            rate = float(input("\n💰 Étape 3 – Combien estimes-tu ta valeur horaire en €/h ? : "))
            if rate >= 0:
                return rate
        except ValueError:
            pass
        print("Merci de saisir un nombre valide (exemple : 40).")


def ask_stress():
    while True:
        try:
            stress = int(input("\n😵‍💫 Étape 4 – Ton niveau de stress (1=détendu·e, 5=épuisé·e) : "))
            if 1 <= stress <= 5:
                return stress
        except ValueError:
            pass
        print("Merci de choisir un niveau entre 1 et 5.")


def compute_pack(hours, stress):
    if hours < 5:
        return "Zen"
    if 5 <= hours <= 10 or stress >= 3:
        return "Sérénité"
    if hours > 10 and stress >= 4:
        return "Harmonie"
    return "Zen"


def main():
    ask_tasks()  # tasks are not used for computation but collected for future use
    hours = ask_hours()
    rate = ask_rate()
    stress = ask_stress()

    monthly_hours = hours * 4
    value = monthly_hours * rate
    pack = compute_pack(hours, stress)

    print("\n🌿 Merci pour ta sincérité.")
    print("Voici une estimation personnalisée de ce que l’automatisation pourrait t’apporter :\n")
    print(f"- ⏳ Heures récupérables/mois : {monthly_hours}")
    print(f"- 💸 Valeur du temps libéré : {value:.2f} €")
    print(f"- 😌 Charge mentale allégée : {stress} sur 5\n")

    print(f"🎁 Pack recommandé : {pack}\n")

    response = input("Souhaites-tu recevoir une fiche personnalisée avec nos conseils ? (O/N) : ")
    if response.strip().lower() == 'o':
        email = input("Parfait ! Indique ton e-mail pour la recevoir : ")
        print(f"Merci ! Nous t’enverrons ta fiche personnalisée à {email}.")
    else:
        print("Merci de ton intérêt. Nous restons à ta disposition si besoin. ✨")


if __name__ == "__main__":
    main()
