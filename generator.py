import random

def random_data(jumlah_data: int):
	genders = ["Pria", "Wanita"]

	jobs = ["Homebrewers", "Cafe Owner", "Barista", "Roaster"]
	job_weight = [4, 1, 2, 1]
	
	female_names = ["Anita", "Bunga", "Citra", "Dewi", "Eka", "Fitri", "Gita", "Hana",
		"Indah", "Jasmine", "Kartika", "Lina","Maya", "Nadia", "Oktavia", "Putri", "Ratna", 
		"Sari", "Tania", "Utami", "Wati", "Yuni", "Zahra", "Novi", "Rina", "Siti", "Winda", "Dita",
		"Erlina", "Mawar", "Lestari", "Vina", "Wahida", "Yani", "Wulan", "Lusi", "Siti", "Tina", 
		"Cika", "Sinta", "Siska", "Intan", "Dian"
	]

	male_names = [
    	"Adi", "Budi", "Candra", "Dwi", "Eko", "Fajar", "Hadi", "Indra", "Joko", "Krisna", "Lukman", "Mulya", "Nugroho", "Oscar", "Prasetyo", "Rudi", "Surya", "Tono", "Umar", "Wahyu", "Yoga", "Zainal",
    	"Andi", "Bayu", "Cahya", "Dian", "Endang", "Febri", "Hari", "Indra", "Jamal", "Kurnia", "Oka", "Putra", "Tito", "Usman", "Zaki","Bagus", "Cahyadi", "Erlangga", "Gilang", "Hanif", "Jaya", "Kusuma", "Lutfi", "Mita", "Nanda",
    	"Oktavian", "Rizki", "Tito", "Utomo", "Wira", "Zulkarnain", "Bagas", "Cahya", "Erlangga", "Fitra", "Gilang", "Hanif", "Ika", "Jaya", "Kusnadi",
    	"Nando", "Oktaviani", "Putu", "Rizky", "Umar", "Vita", "Yudha", "Bambang", "Faisal", "Handoko", "Jaya", "Krisna", "Miftah", "Okta", "Putu", "Rizky", "Utari", "Vino",
    	"Aji", "Bayu", "Dodi", "Edo", "Farhan", "Gani", "Hafid", "Indra", "Joko", "Kusuma", "Lutfi", "Miko", "Nanda", "Oki", "Prasetyo", "Qori", "Rudi", "Surya", "Tito", "Umar", "Wahyu", "Yoga", "Zainal",
    	"Adit", "Bagas", "Cakra", "Dedi", "Edo", "Faris"
	]


	data = []

	for _ in range(jumlah_data):
		gender = random.choice(genders)

		if gender=="Pria":
			name = random.choice(male_names)
		else:
			name = random.choice(female_names)
		
		age = random.randint(21,43)
		job = random.choices(jobs, job_weight)[0]
		income = random.randint(700000, 4000000)
		spending = random.randint(700000, min(income, 4000000))

		# Page 1
		page_one_choice = [
			random.randint(1,2),
			random.randint(1,2),
			random.randint(3,5),
			random.randint(3,5)
		]

		# Page 2
		page_two_choice = [
			random.randint(1,2),
			random.randint(2,3),
			random.randint(3,5),
			random.randint(4,5)
		]

		# Page 3
		page_three_choice = [
			random.randint(3,5),
			random.randint(1,2),
			random.randint(4,5),
			random.randint(4,5)
		]

		# Page 4
		page_four_choice = [
			random.randint(3,5),
			random.randint(4,5),
			random.randint(1,3),
			random.randint(2,4)
		]

		# Page 5
		page_five_choice = [
			random.randint(4,5),
			random.randint(3,5),
			random.randint(1,3),
			random.randint(1,2)
		]

		# Page 6
		page_six_choice = [
			random.randint(2,4),
			random.randint(2,4),
			random.randint(2,4),
			random.randint(1,2),
			random.randint(1,2),
			random.randint(2,4)
		]

		entry = {
			"nama": name,
			"gender": gender,
			"umur": age,
			"pekerjaan": job,
			"pendapatan": income,
			"pengeluaran": spending,
			"page_one": page_one_choice,
			"page_two": page_two_choice,
			"page_three": page_three_choice,
			"page_four":  page_four_choice,
			"page_five": page_five_choice,
			"page_six": page_six_choice
		}

		data.append(entry)

	return data