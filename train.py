import csv
import sys

def load_data(filepath='data.csv'):
	mileages = []
	prices = []
	try:
		with open(filepath, mode='r', encoding='utf-8') as f:
			reader = csv.reader(f)
			next(reader)
			for row in reader:
				if len(row) >= 2 and row[0].strip() and row[1].strip():
					mileages.append(float(row[0]))
					prices.append(float(row[1]))
	except FileNotFoundError:
		print(f"Erreur : le fichier '{filepath}' est introuvable.")
		sys.exit(1)
	except Exception as e:
		print(f"Erreur lors de la lecture de '{filepath}' : {e}")
		sys.exit(1)

	if not mileages:
		print("Erreur : le dataset est vide.")
		sys.exit(1)

	return mileages, prices

def train(mileages, prices, learning_rate, epochs):
	m = len(mileages)
	min_km = min(mileages)
	max_km = max(mileages)

	if max_km == min_km:
		print("Erreur : tous les kilométrages sont identiques.")
		sys.exit(1)

	norm_mileages = [(x - min_km) / (max_km - min_km) for x in mileages]

	theta0 = 0.0
	theta1 = 0.0

	print(f"Début de l'entraînement ({epochs} itérations, learning rate = {learning_rate})...")

	for _ in range(epochs):
		sum_errors_0 = 0.0
		sum_errors_1 = 0.0

		for i in range(m):
			prediction = theta0 + (theta1 * norm_mileages[i])
			error = prediction - prices[i]
			sum_errors_0 += error
			sum_errors_1 += error * norm_mileages[i]

		tmp_theta0 = learning_rate * (1 / m) * sum_errors_0
		tmp_theta1 = learning_rate * (1 / m) * sum_errors_1

		theta0 -= tmp_theta0
		theta1 -= tmp_theta1

	real_theta1 = theta1 / (max_km - min_km)
	real_theta0 = theta0 - (real_theta1 * min_km)

	return real_theta0, real_theta1

def save_thetas(theta0, theta1, filepath='thetas.csv'):
	try:
		with open(filepath, mode='w', encoding='utf-8') as f:
			f.write(f"{theta0},{theta1}\n")
		print(f"Paramètres sauvegardés avec succès dans '{filepath}'.")
	except Exception as e:
		print(f"Erreur lors de la sauvegarde : {e}")

def main():
	mileages, prices = load_data('data.csv')
	theta0, theta1 = train(mileages, prices, 0.1, 10000)
	print(f"\nRésultats de l'entraînement :")
	print(f"  theta0 (ordonnée à l'origine) : {theta0:.4f}")
	print(f"  theta1 (pente)                : {theta1:.6f}")
	save_thetas(theta0, theta1)

if __name__ == '__main__':
	main()
