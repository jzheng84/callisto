import datetime
import pandas as pd
import pdb



def main():
	# Read poopee and weight data.
	poopee_data = pd.read_csv('poopee.csv')
	weight_data = pd.read_csv('weight.csv')

	# Manually select date range for now.
	start_date = datetime.date(2021, 3, 24)
	num_days = 7

	idxs = []
	date = start_date
	num_poops = 0
	num_pees = 0
	num_misses = 0
	
	for i in range(num_days):
		month = date.month
		day = date.day

		date_str = ('%02d/%02d' % (month, day))
		df = poopee_data[poopee_data['Date'] == date_str]

		num_poops += (df['Type'] == 'poop').sum()
		num_pees += (df['Type'] == 'pee').sum()
		num_misses += (df['Location'] == 'floor').sum()

		date += datetime.timedelta(days=1)

	print('# poops: %d' % num_poops)
	print('# pees: %d' % num_pees)
	print('# misses: %d' % num_misses)
	print('miss rate: %f' % (num_misses / (num_poops + num_pees)))

if __name__ == '__main__':
	main()