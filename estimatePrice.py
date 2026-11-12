def load_thetas(filepath='thetas.csv'):
	try:
		with open(filepath, mode='r', encoding='utf-8') as f:
			line = f.readline().strip()
			if line:
				t0, t1 = line.split(',')
				return float(t0), float(t1)
	except FileNotFoundError:
		pass
	except Exception as e:
		print(f"Avertissement lors de la lecture des thetas : {e}")

	return 0.0, 0.0

def estimate_price(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def main():
	theta0, theta1 = load_thetas('thetas.csv')

	try:
		user_input = input("Entrez le kilométrage d'un véhicule : ").strip()
		if not user_input:
			print("Erreur : aucun kilométrage renseigné.")
			return

		mileage = float(user_input)
		if mileage < 0:
			print("Erreur : un kilométrage ne peut pas être négatif.")
			return

		price = estimate_price(mileage, theta0, theta1)

		if theta0 == 0.0 and theta1 == 0.0:
			print(f"Modèle non entraîné (theta0 = 0, theta1 = 0).")
			print(f"Prix estimé : 0.0 €")
		else:
			estimated = max(0.0, price)
			print(f"Prix estimé pour {mileage:,.0f} km : {estimated:.2f} €")

	except ValueError:
		print("Erreur : veuillez entrer un nombre valide.")
	except (KeyboardInterrupt, EOFError):
		print("\nProgramme interrompu.")

if __name__ == '__main__':
	main()
