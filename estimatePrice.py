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
		print(f"Warning while reading thetas: {e}")

	return 0.0, 0.0

def estimate_price(mileage, theta0, theta1):
	return theta0 + (theta1 * mileage)

def main():
	theta0, theta1 = load_thetas('thetas.csv')

	try:
		user_input = input("Enter a vehicle mileage: ").strip()
		if not user_input:
			print("Error: No mileage provided.")
			return

		mileage = float(user_input)
		if mileage < 0:
			print("Error: Mileage cannot be negative.")
			return

		price = estimate_price(mileage, theta0, theta1)

		if theta0 == 0.0 and theta1 == 0.0:
			print("Model not trained (theta0 = 0, theta1 = 0).")
			print("Estimated price: 0.0 €")
		else:
			estimated = max(0.0, price)
			print(f"Estimated price for {mileage:,.0f} km: {estimated:.2f} €")

	except ValueError:
		print("Error: Please enter a valid number.")
	except (KeyboardInterrupt, EOFError):
		print("\nProgram interrupted.")

if __name__ == '__main__':
	main()
