import csv
import sys
import matplotlib.pyplot as plt

def load_data(filepath='data.csv'):
	mileages = []
	prices = []
	try:
		with open(filepath, mode='r', encoding='utf-8') as f:
			reader = csv.reader(f)
			header = next(reader)
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


def graph(mileages, prices, theta0, theta1):
	plt.title("Linear Regression: Price vs Mileage")
	plt.xlabel("Kilométrage (km)")
	plt.ylabel("Prix (€)")
	plt.scatter(mileages, prices, color='red', marker='x', label="Données réelles")
	line_x = [min(mileages), max(mileages)]
	line_y = [theta0 + (theta1 * x) for x in line_x]

	plt.plot(line_x, line_y, color='black', label="Droite de régression")
	plt.legend()
	plt.grid(True)
	plt.show()

def main():
	mileages, prices = load_data('data.csv')
	theta0, theta1 = load_thetas('thetas.csv')
	graph(mileages, prices, theta0, theta1)

if __name__ == '__main__':
	main()
