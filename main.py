import time
import generator
import keyboard

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


def determine_money_category(jumlah_uang: int):
	if jumlah_uang>=700000 and jumlah_uang<750000:
		return 1
	elif jumlah_uang>=750000 and jumlah_uang<=1000000:
		return 2
	elif jumlah_uang>=1000001 and jumlah_uang<=1500000:
		return 3
	elif jumlah_uang>=1500001 and jumlah_uang<=2000000:
		return 4
	elif jumlah_uang>=2000001 and jumlah_uang<=3000000:
		return 5
	else:
		return 6


# masukan jumlah data yang ingin dibuat
jumlah_data = int(input("Masukan jumlah data yang ingin di input: "))
generated_random_data = generator.random_data(jumlah_data=jumlah_data)

# konfirm data
print(f"[info] data yang di-generate sejumlah: {jumlah_data}")
print(f"[info] memulai eksekusi...")

url = "https://docs.google.com/forms/d/e/1FAIpQLSdhgiTXY-VGZEyspZODcHFmDK-LYsPqSfFIsoJBO2Q7bFUImQ/viewform"

job_done = 1

# memulai job
for data in generated_random_data:
	options = Options()
	options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
	browser = webdriver.Firefox(options=options)
	browser.get(url)

	# isi nama
	fill_name = browser.find_element(By.CLASS_NAME, "Xb9hP")
	ActionChains(browser).move_to_element(fill_name).click(fill_name).send_keys(data['nama']).perform()

	# isi gender
	if data['gender'] == "Pria":
		fill_gender = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div")
		fill_gender.click()
	else:
		fill_gender = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div")
		fill_gender.click()

	# isi umur
	umur = data['umur']
	if umur<21:
		fill_age = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div")
		fill_age.click()
	elif (umur>=21 and umur<=25):
		fill_age = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div")
		fill_age.click()
	elif (umur>=26 and umur<=30):
		fill_age = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[3]/label/div")
		fill_age.click()
	elif (umur>=31 and umur<=35):
		fill_age = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[4]/label/div")
		fill_age.click()
	else:
		fill_age = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[5]/label/div")
		fill_age.click()

	# isi pekerjaan
	pekerjaan = data['pekerjaan']
	if pekerjaan=="Homebrewers":
		fill_job = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div")
		fill_job.click()
	elif pekerjaan=="Cafe Owner":
		fill_job = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[2]/label/div")
		fill_job.click()
	elif pekerjaan=="Barista":
		fill_job = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[3]/label/div")
		fill_job.click()
	elif pekerjaan=="Roaster":
		fill_job = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label/div")
		fill_job.click()
	else:
		fill_job = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[5]/label/div")
		fill_job.click()
		pekerjaan_fill_textbox = browser.find_element(By.CLASS_NAME, "JGptt")
		ActionChains(browser).move_to_element(pekerjaan_fill_textbox).click(pekerjaan_fill_textbox).send_keys(pekerjaan).perform()

	# isi pendapatan
	pendapatan = determine_money_category(data['pendapatan'])
	fill_pendapatan = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[{pendapatan}]/label/div")
	fill_pendapatan.click()

	# isi pengeluaran
	pengeluaran = determine_money_category(data['pengeluaran'])
	fill_pengeluaran = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[{pengeluaran}]/label/div")
	fill_pengeluaran.click()


	# klik next page
	next_page = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span")
	next_page.click()


	# job per page
	for i in range(3):
		# job untuk page 1 sampai 3
		if i==0:
			print("[info] Page 1")
			choices = data['page_one']
		elif i==1:
			print("[info] Page 2")
			choices = data['page_two']
		elif i==2:
			print("[info] Page 3")
			choices = data['page_three']

		q1 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[{choices[0]}]/div[1]")
		q1.click()

		q2 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[{choices[1]}]/div[1]")
		q2.click()

		q3 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[{choices[2]}]/div[1]")
		q3.click()

		q4 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[{choices[3]}]/div[1]")
		q4.click()

		next_page = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
		next_page.click()

		time.sleep(3)

	# job page 4
	print("[info] Page 4")
	choices = data['page_four']
	q1 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/span/div/label[{choices[0]}]/div[1]")
	q1.click()

	q2 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[{choices[1]}]/div[1]")
	q2.click()

	q3 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[{choices[2]}]/div[1]")
	q3.click()

	q4 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[{choices[3]}]/div[1]")
	q4.click()

	next_page = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
	next_page.click()

	time.sleep(3)

	# job page 5
	print("[info] Page 5")
	choices = data['page_five']

	q1 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/span/div/label[{choices[0]}]/div[1]")
	q1.click()

	q2 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/span/div/label[{choices[1]}]/div[1]")
	q2.click()

	q3 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/span/div/label[{choices[2]}]/div[1]")
	q3.click()

	q4 = browser.find_element(By.XPATH, f"/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/span/div/label[{choices[3]}]/div[1]")
	q4.click()

	next_page = browser.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
	next_page.click()

	time.sleep(3)

	# job page 6
	# choices = data['page_six']
	print("[warning] skiping job at page 6.")

	# submit
	# --> Add confirmation
	print("[warning] sebelum disubmit bisa direview dulu hasil responnya.")
	print("press enter to continue...")
	keyboard.wait('enter')

	time.sleep(5)
	browser.quit()
	print(f"[info] job {job_done} OK")
	job_done += 1

print("[info] done.")